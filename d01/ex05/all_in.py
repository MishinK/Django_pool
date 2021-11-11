#coding=utf8
import sys

def get_key(d, val):
    for k, v in d.items():
        if v.lower() == val.lower():
            return k

def get_val(d, key):
    for k, v in d.items():
        if k.lower() == key.lower():
            return v

def capital_city(state):
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
	if (get_val(states, state)):
		return(capital_cities[get_val(states, state)])

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
	if (get_key(capital_cities, capital)):
		return(get_key(states, get_key(capital_cities, capital)))

def all_in(str):
	lst_str = str.split(',')
	for elem in lst_str:
		name = elem.strip(" ")
		if (name != ''):
			if (capital_city(name)):
				print("{0} is the capital of {1}".format(capital_city(name), state(capital_city(name))))
			elif (state(name)):
				print("{0} is the capital of {1}".format(capital_city(state(name)), state(name)))
			else:
				print("{0} is neither a capital city nor a state".format(name))

if __name__ == '__main__':
    if (len(sys.argv) == 2):
        all_in(sys.argv[1])