#!/usr/bin/python3
#coding=utf8
import sys

def parse_line(line: str):
    el = line.split("=")
    result = dict((value.strip().split(":") for value in el[1].split(",")))
    result["name"] = el[0].strip()
    return result


def main():
	HTML = """
<!DOCTYPE html>
	<html lang="en">
		<head>
			<meta charset="UTF-8">
			<meta name="viewport" content="width=device-width, initial-scale=1.0">
			<title>periodic_table</title>
			<style>
				h4 {{text-align: center;}}
				table{{border-collapse: collapse;}}
				ul {{ list-style:none;
					padding-left:0px;}}
			</style>
		</head>
		<body>
			<table>
			{table_body}
			</table>
		</body>
	</html>
"""
	TEMPLATE = """
<td style="border: 1px solid black; padding:10px">
	<h4>{name}</h4>
		<ul>
			<li>No {number}</li>
			<li>{small}</li>
			<li>{molar}</li>
			<li>{electron} electron</li>
		</ul>
	</td>
"""
	body = "<tr>"
	with open("periodic_table.txt", "r") as f:
		periodic_table = [(parse_line(line)) for line in f.readlines()]
		pos = 0
		for dic in periodic_table:
			if pos > int(dic["position"]):
				body += "</tr>\n<tr>\n"
				pos = 0
			for i in range(pos, int(dic["position"]) - 1):
				body += "<td>\n</td>\n"
			pos = int(dic["position"])
			body += TEMPLATE.format(
            	name=dic["name"],
            	number=dic["number"],
            	small=dic["small"],
            	molar=dic["molar"],
            	electron=dic["electron"],
        	)
		body += "</tr>\n"
		with open("periodic_table.html", "w") as f2:
			f2.write(HTML.format(table_body=body))

if __name__ == '__main__':
    main()