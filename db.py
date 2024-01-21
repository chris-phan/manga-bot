from config import MANGA_KEYS


class Database:
    def __init__(self):
        self.db = self.__read_disk()

    def __read_disk(self):
        f = open("data.txt", "r")
        data = {}
        for l in f:
            s = l.split(": ")
            key = s[0]
            val = ": ".join(s[1:])
            data[key] = val.strip()

        f.close()
        return data

    def update(self, key, val):
        if key not in MANGA_KEYS:
            return

        self.db[key] = val
        f = open("data.txt", "w")
        for k, v in self.db.items():
            f.write(f"{k}: {v}\n")

        f.close()

    def keys(self):
        return list(self.db.keys())

    def values(self):
        return list(self.db.values())

    def get(self, key):
        return self.db.get(key, None)


if __name__ == "__main__":
    db = Database()
    db.update("OPM", "3")
    db.update("MHA", "aid")
