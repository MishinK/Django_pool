#coding=utf8
import sys, os, re

def read_file():
	try:
		with open("settings.py", 'r') as config_file:
			sett = config_file.read()
			with open(sys.argv[1], "r") as template_file:
				result = template_file.read()
				lines = sett.split('\n')
				for line in lines:
					name, val = line.split('=')
					name = name.strip()
					val = val.strip(" ").strip('"')
					result = re.sub('\{' + name + '\}', val, result)
				return result
	except IOError:
		print("Error opening")

def create_html(info):
	if info:
		try:
			with open("myCV.html", "w") as Html_file:
				Html_file.write(info)
		except IOError:
			print("Error writing")

if __name__ == '__main__':
	if len(sys.argv) == 2 and re.search('\.template$', sys.argv[1]) is not None:
		if not os.path.isfile(sys.argv[1]):
			print("{0} file not found".format(sys.argv[1]))
		elif not os.path.isfile("settings.py"):
			print("{0} file not found".format("settings.py"))
		else:
			create_html(info = read_file())
	else:
		print("one file expected, must be a _name_.template")