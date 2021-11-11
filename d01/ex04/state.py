#coding=utf8
import sys

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

def state(capital):
	states = {
  			"Oregon" : "OR",
			"Alabama" : "AL",
			"New Jersey" : "NJ",
			"Colorado" : "CO"
	}
	capital_cities = {
			"OR" : "Salem",
			"AL" : "Montgomery",
			"NJ" : "Trenton",
			"CO": "Denver"
	}
	if capital in capital_cities.values():
			print(get_key(states, get_key(capital_cities, capital)))
	else:
			print("Unknown capital city")

if __name__ == '__main__':
    if (len(sys.argv) == 2):
        state(sys.argv[1])