from os import environ

SECRET_KEY = "RUSH01"

MAP_SIZE = (20, 20)
SCREEN_SIZE = (10, 8)
SCREEN_OFFSET = (-5, -5)

PLAYER_INIT_POS = (0, 0)
PLAYER_INIT_MOVBALL = 40

OMDB_URL = "http://www.omdbapi.com/"

OMDB_API_KEY = (
    "2562735f"
    if environ.get("OMDB_API_KEY") is None
    else environ.get("OMDB_API_KEY")
)

IMDB_LIST = [
	"tt0091064",
    "tt4680182",
    "tt2231461",
    "tt0100814",
    "tt5688868",
    "tt4374286",
    "tt0069005",
    "tt0100260",
    "tt0089469",
    "tt0055894",
    "tt1396484",
    "tt0065163",
    "tt0090190",
    "tt0084745",
    "tt0457430",
    "tt0093177",
    "tt0083907",
    "tt5884052",
    "tt3794354",
    "tt7504864",
    "tt1415872",
    "tt7904362",
    "tt1788453",
    "tt0468492",
    "tt5034838",
    "tt0078748",
    "tt0087363",
    "tt0073195",
    "tt8235660",
    "tt0118615",
    "tt0105643",
    "tt1844770",
    "tt0329101",
    "tt0372873",
    "tt1934381",
    "tt1270797",
    "tt3967856",
    "tt0317676",
    "tt1489946",
    "tt1714203",
    "tt5639976",
    "tt6644200",
    "tt0198781",
]
