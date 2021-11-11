from django.conf import settings
import random

def clip(value, cliprange: tuple):
    assert cliprange[0] <= cliprange[1], "invalid cliprange"
    return max(cliprange[0], min(value, cliprange[1]))

class Camera:
    def __init__(self, size, offset):
        self.width, self.height = size
        self.offset_x, self.offset_y = offset

    def render(self, map, x, y):
        width, height = len(map[0]), len(map)
        px = clip(x + self.offset_x, (0, width - self.width))
        py = clip(y + self.offset_y, (0, height - self.height))
        screen = [[0] * self.width for _ in range(self.height)]
        for sy, j in enumerate(range(py, py + self.height)):
            for sx, i in enumerate(range(px, px + self.width)):
                screen[sy][sx] = map[j][i]
        return screen

class Engine:

    def __init__(self, size, screen, offset, playerpos, movball, total_moviemons, my_moviemons, premap=None,):
        self.width, self.height = size
        self.map = premap
        self.px, self.py = playerpos
        self.movball = movball
        self.state = None
        self.camera = Camera(screen, offset)
        self.map[self.py][self.px].content = "@"
        self.total_moviemons = total_moviemons
        self.my_moviemons = my_moviemons

    def move(self, x, y):
        if 0 <= self.px + x <= self.width - 1:
            self.px += x
        if 0 <= self.py + y <= self.height - 1:
            self.py += y
        self.update()

    def render(self):
        return self.camera.render(self.map, self.px, self.py)

    def add(self, pos, content):
        self.map[pos[0]][pos[1]].append(content)

    def __coll(self, target):
        if self.map[self.py][self.px].content == target:
            self.map[self.py][self.px].content = ""
            self.map[self.py][self.px].seen = 0
            return True

    def collisioncheck(self):
        if self.__coll("movieball"):
            self.movball += 1
            self.state = "movieball"
        if self.__coll("movieradar"):
            radar(self.map, (self.px, self.py))
            self.state = "movieradar"
        if self.__coll("moviemon"):
            self.state = "battle"

    def spawn(self, func, mbprob, amount):
        if random.randint(1, mbprob) == 1:
            func(
                self.map,
                self.height,
                self.width,
                (self.px, self.py),
                random.randint(1, amount),
            )

    def visit(self):
        self.map[self.py][self.px].visit()
        for y in self.map:
            for x in y:
                x.update()
                if x.content == "@":
                    x.content = ""
        self.map[self.py][self.px].content = "@"

    def update(self):
        self.collisioncheck()
        self.visit()
        self.spawn(populate_movieball, 10, 3)
        self.spawn(populate_movieradar, 20, 1)
        if random.randint(1, 4) == 1:
            map_moviemons = 0
            for y in self.map:
                for x in y:
                    if x.content == "moviemon":
                        map_moviemons += 1
            if map_moviemons <= self.total_moviemons - self.my_moviemons:
                self.spawn(populate_moviemon, 5, 1)

class Tile:
    def __init__(self, content: str = None):
        self.content = content
        self.seen = 0
        self.heat = 0
        self.rgb(152, 161, 154, 4, 3, 3)

    def __str__(self):
        return self.content

    def visit(self, heat=16):
        self.heat += heat

    def rgb(self, r, g, b, mulr, mulg, mulb):
        self.r = r - mulr * self.heat
        self.g = g - mulg * self.heat
        self.b = b - mulb * self.heat

    def update(self):
        self.heat = clip(self.heat, (-16, 16))
        if self.heat > 0:
            self.heat -= 1
        elif self.heat < 0:
            self.heat += 1
        self.rgb(152, 161, 154, 4, 3, 3)


def radar(mmap, ppos):
    import math

    def rangeint(x1, y1, x2, y2):
        return int(
            math.sqrt(math.pow(abs(x2 - x1), 2) + math.pow(abs(y2 - y1), 2))
        )

    offset = (-3, -3)
    x, y = ppos[0] + offset[0], ppos[1] + offset[1]
    radmap = [
        "..###..",
        ".#####.",
        "#######",
        "#######",
        "#######",
        ".#####.",
        "..###..",
    ]
    for i in range(7):
        for j in range(7):
            if radmap[i][j] == "#":
                a, b = max(x + i, 0), max(y + j, 0)
                try:
                    mmap[b][a].heat = -20 + 4 * rangeint(ppos[0], ppos[1], a, b)
                    if mmap[b][a].content:
                        mmap[b][a].seen = 1
                except Exception as e:
                    pass


def init_map(width, height, moviemons):
    mmap = [[Tile() for _ in range(width)] for _ in range(height)]
    ppos = settings.PLAYER_INIT_POS
    height, width = len(mmap), len(mmap[0])
    mmap = populate_moviemon(mmap, height, width, ppos, moviemons)
    mmap = populate_movieball(mmap, height, width, ppos)
    return mmap


def spawn_to_map(mmap, ppos, x, y, content, i):
    if (x, y) != ppos and not mmap[y][x].content and not mmap[y][x].heat:
        mmap[y][x].content = content
        mmap[y][x].seen = 0
        return i + 1
    return i


def populate_moviemon(mmap, height, width, ppos, total):
    i = 0
    while 1:
        x, y = random.randint(0, width - 1), random.randint(0, height - 1)
        i = spawn_to_map(mmap, ppos, x, y, "moviemon", i)
        if i >= total:
            break
    return mmap


def populate_movieradar(mmap, height, width, ppos, total=None):
    i = 0
    for _ in range(100):
        x, y = random.randint(0, width - 1), random.randint(0, height - 1)
        i = spawn_to_map(mmap, ppos, x, y, "movieradar", i)
        if i >= total:
            break


def populate_movieball(mmap, height, width, ppos, total=None):
    i = 0
    if not total:
        density = 10 * random.randint(9, 11) / 10
        total = int((density / 100) * height * width)
    for _ in range(10000):
        x, y = random.randint(0, width - 1), random.randint(0, height - 1)
        i = spawn_to_map(mmap, ppos, x, y, "movieball", i)
        if i >= total:
            return mmap
    return mmap


def get_suitable(num, mondct, lo, lovar, hi, hivar):
    res, lonow, hinow = dict(), 0, 0
    for mid, mm in mondct.items():
        if mm.rating <= lovar and lonow < lo and len(res) < num:
            res[mid] = mm
            lonow += 1
        if mm.rating >= hivar and hinow < hi and len(res) < num:
            res[mid] = mm
            hinow += 1
    left = num - len(res)
    for _ in range(1000):
        k = random.choice(list(mondct.keys()))
        if k not in res.keys():
            res[k] = mondct[k]
            left -= 1
        if left <= 0:
            break
    return res

