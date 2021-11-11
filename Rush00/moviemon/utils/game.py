from django.conf import settings
from Rush00.settings.moviemon import IMDB_LIST
import os, shutil, requests, pickle, random
from typing import Dict, List, Tuple
from moviemon.utils.moviemon import Moviemon
from moviemon.utils.other import *


def make_save_dir():
    if not os.path.isdir("saved_game"):
        os.mkdir("saved_game")

def save_session_data(data):
    make_save_dir()
    try:
        with open("saved_game/session.bin", "wb") as f:
        	pickle.dump(data, f)
        	return data
    except:
        return None

def load_session_data():
    try:
        with open("saved_game/session.bin", "rb") as f:
        	data = pickle.load(f)
        	return data
    except:
        return None

def load_slot_info():
    try:
        if os.path.isfile("saved_game/slots.bin"):
            with open("saved_game/slots.bin", "rb") as f:
                return pickle.load(f)
        return {}
    except:
        return {}


def save_slot(slot):
	data = load_session_data()
	slots = load_slot_info()
	if data is not None:
		try:
			score = "{}/{}".format(len(data["captured_list"]), len(data["moviemon"]))
			sl = "{}".format(slot)
			if slots.get(sl, None) and os.path.isfile(slots[sl]["file"]):
				os.remove(slots[sl]["file"])
			file = "saved_game/slot{}_{}_{}.mmg".format(slot, len(data['captured_list']), len(data['moviemon']))
			with open(file, "wb") as f:
				pickle.dump(data, f)
			slots[sl] = {
                "score": score,
                "file": file,
            }
			with open("saved_game/slots.bin", "wb") as f:
				pickle.dump(slots, f)
			return True
		except:
			pass
	return False


def load_slot(slot):
	slots = load_slot_info()
	slot = slots.get(slot, None)
	if slot is not None:
		try:
			shutil.copy(slot["file"], "saved_game/session.bin")
			return True
		except:
			pass
	return False


class GameData:
    def __init__(self) -> None:
        self.pos: Tuple[int, int] = settings.PLAYER_INIT_POS
        self.movieballCount: int = settings.PLAYER_INIT_MOVBALL		
        self.captured_list: List[str] = []
        self.map:List[List[Tile]] = []		
        self.moviemon: Dict[str, Moviemon] = {}

    def get_movie(self, moviemon_id):
        return self.moviemon[moviemon_id]

    def get_random_movie(self):
        id_list = [m for m in self.moviemon.keys() if not m in self.captured_list]
        return random.choice(id_list)

    def get_strength(self) -> int:
        ratings = sorted([self.moviemon[i].rating for i in self.load(load_session_data()).captured_list], reverse=True)
        if ratings:
            numsend = min(6, len(ratings))
            return int(sum(ratings[:numsend]) / numsend)
        else:
            return 1

    def dump(self):
        return {
            "pos": self.pos,
            "captured_list": self.captured_list,
            "moviemon": self.moviemon,
            "movieballCount": self.movieballCount,
            "map": self.map,
        }

    @staticmethod
    def load(data):
        result = GameData()
        result.pos = data["pos"]
        result.captured_list = data["captured_list"]
        result.moviemon = data["moviemon"]
        result.movieballCount = data["movieballCount"]
        result.map = data["map"]
        return result

    @staticmethod
    def load_default_settings():
        result = GameData()
        DB_LIST = settings.IMDB_LIST
        for id in DB_LIST:
            params = {"apikey": settings.OMDB_API_KEY, "i": id}
            try:
                data = requests.get(settings.OMDB_URL, params=params).json()
                result.moviemon[id] = Moviemon(
                    data["Title"],
                    data["Year"],
                    data["Director"],
                    data["Poster"],
                    float(data["imdbRating"]),
                    data["Plot"],
                    data["Actors"],
                )
            except Exception as e:
                assert e
        x, y = settings.MAP_SIZE
        total = min(
            int(x * y * random.randint(7, 11) / 80),
            len(result.moviemon.keys()),
        )
        result.moviemon = get_suitable(
            total,
            result.moviemon,
            max(3, int(total / 3)),
            4,
            max(3, int(total / 3)),
            7,
        )
        result.map = init_map(
            *settings.MAP_SIZE,
            int(random.uniform(0.5, 1) * len(result.moviemon)),
        )
        return result

