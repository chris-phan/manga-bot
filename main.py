import os, asyncio, asyncpraw, nextcord, re
from dotenv import load_dotenv
from os import system
from nextcord import Intents, Embed, Color, ButtonStyle
from nextcord.ui import Button, View
from nextcord.ext import commands
from config import MANGA_UPDATE_FREQ, SUBREDDIT_NAMES, REGEX_LIST, MANGA_KEYS
from db import Database

load_dotenv()
database = Database()

intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

reddit = asyncpraw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    user_agent=os.getenv("USER_AGENT"),
)


@bot.command(name="test")
async def test(ctx):
    print(database.get("OPM"))
    await ctx.send("Hello world!")


@commands.cooldown(1, 10, commands.BucketType.user)
@bot.command(name="manga")
async def manga(ctx):
    await update_manga()


async def update_manga():
    # while True:
    subreddits_to_check = []
    for i in range(len(SUBREDDIT_NAMES)):
        sr = await reddit.subreddit(SUBREDDIT_NAMES[i])
        subreddits_to_check.append([sr, REGEX_LIST[i], MANGA_KEYS[i]])

    print("Checking for updates")
    for i in range(len(subreddits_to_check)):
        sr, regex, key = subreddits_to_check[i]
        await check_sub(sr, regex, key)
        print(f"{key} done")

    channel = bot.get_channel(int(os.getenv("GENERAL_CHN")))
    await channel.send("Done scanning")

    # await asyncio.sleep(MANGA_UPDATE_FREQ)


async def check_sub(sr, regex, key):
    channel = bot.get_channel(int(os.getenv("MANGA_CHN")))
    sub_to_send = None

    async for sub in sr.hot(limit=5):
        if "pre" in sub.title.lower() or "leak" in sub.title.lower():
            continue
        elif re.search(regex, sub.title):
            if key not in database.keys():
                database.update(key, sub.title)
                sub_to_send = sub
            elif database.get(key) != sub.title:
                scanned_ch_num = [int(s) for s in sub.title.split() if s.isdigit()][0]
                prev_ch_num = [
                    int(s) for s in database.get(key).split() if s.isdigit()
                ][0]

                print(f"scanned_ch_num: {scanned_ch_num}, prev_ch_num: {prev_ch_num}")

                if scanned_ch_num > prev_ch_num:
                    sub_to_send = sub
                    database.update(key, sub.title)

    if sub_to_send != None:
        await channel.send(f"{sub_to_send.title}\n{sub_to_send.url}")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = Embed(
            title=f"Slow down!",
            description=f"Try again in {error.retry_after:.2f}s",
            color=Color.red(),
        )
        await ctx.send(embed=em)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    await update_manga()


if __name__ == "__main__":
    bot.run(os.getenv("TOKEN"))
