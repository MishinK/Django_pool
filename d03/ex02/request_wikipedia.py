#!/usr/bin/env python3
import sys
import requests
import dewiki
import json

def get_wiki_info_to_file(page: str):
		try:
			URL = "https://en.wikipedia.org/w/api.php"
			PARAMS = {
				"action": "parse",
				"page": page,
				"format": "json", 
				"prop": "wikitext",
				"redirects": True
				}
			req = requests.Session().get(url=URL, params=PARAMS)
			res = dewiki.from_string(req.json()["parse"]["wikitext"]["*"]).replace('\n\n', '\n')
			with open(dewiki.from_string(page).replace(' ', '_') + '.wiki', 'w') as f:
				f.write(res)
		except Exception as e:
			print("Error:", e)

def main():
	if len(sys.argv) != 2:
		exit('Program requires at least one argument.')
	else:    
		get_wiki_info_to_file(sys.argv[1])

if __name__ == '__main__':
	main()