class Message:
    msg = {
        "battle": "Keck, it's the same moviemon!",
        "movieball": "Ahah, again a movieball!",
        "movieradar": "Surprise! movieradar!)",
        "none": "",
    }

    def __init__(self, key):
        self.key = key
        self.log = Message.msg.get(key, "WRONG KEY!")
        self.ammount = 1

    def __str__(self):
        if self.ammount >= 2 and not self.key == "none":
            return f"{self.log} ✖{self.ammount}"
        return self.log

    def __call__(self, key, single=False):
        if key == self.key and not single:
            self.ammount += 1
        else:
            self.ammount = 1
        self.key = key
        self.log = Message.msg.get(key, f"wrong key! key:{key}")