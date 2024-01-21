# Manga updates:
MANGA_UPDATE_FREQ = 3600  # manga update every _ seconds
# Ex: Chapter 123 [English]
OPM_REGEX = "^Chapter \d+ \[English\]$"
# Ex: Jujutsu Kaisen Chapter 123 Links + Discussion
JJK_REGEX = "^Jujutsu Kaisen.* \d+"
# Ex: Chapter 123 Official Release - Links and Discussion
MHA_REGEX = "^Chapter \d+ Official Release"
# Ex: [DISC] Chainsaw Man - Ch. 123 links
CSM_REGEX = "^\[DISC\] Chainsaw Man.* \d+"
# Ex: Boruto: Two Blue Vortex Chapter 1 - Links and Discussion
BOR_REGEX = "^Boruto:.*Chapter \d+"
# Ex: Chapter 123 -- Discussion
HXH_REGEX = "^Chapter \d+.*Discussion$"
# Ex: Versus Chapter 123 [English]
VRS_REGEX = "Versus Chapter \d+.*"
# Ex: [DISC] Blue Lock - Chapter 123
BLK_REGEX = "\[DISC\] Blue Lock.* \d+"
# Ex: The JOJOLands - Chapter 123
JOJO_REGEX = "The JOJOLands - Chapter \d+"


"""
  To add a new manga, add the subreddit to SUBREDDIT_NAMES. Then add a new
  regex and key to REGEX_LIST and MANGA_KEYS respectively

  HXH has been removed since it's been privated and is causing an error
  Add it back later
    SUBREDDIT_NAMES: "HunterXHunter"
    REGEX_LIST: "HXH_REGEX"
    MANGA_KEYS: "HXH"
"""
SUBREDDIT_NAMES = [
    "OnePunchMan",
    "Jujutsushi",
    "BokuNoHeroAcademia",
    "ChainsawMan",
    "Boruto",
    "BlueLock",
    "VersusSeries",
    "StardustCrusaders",
]

REGEX_LIST = [
    OPM_REGEX,
    JJK_REGEX,
    MHA_REGEX,
    CSM_REGEX,
    BOR_REGEX,
    BLK_REGEX,
    VRS_REGEX,
    JOJO_REGEX,
]

MANGA_KEYS = ["OPM", "JJK", "MHA", "CSM", "BOR", "BLK", "VRS", "JOJO"]
