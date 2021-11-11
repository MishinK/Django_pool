#!/usr/bin/python3
# coding: utf-8

import elem

class Html(elem.Elem):
	def __init__(self, content = None, attr = {}):
		elem.Elem.__init__(self, tag = 'html', attr=attr, content=content)

class Head(elem.Elem):
	def __init__(self, content = None, attr = {}):
		elem.Elem.__init__(self, tag = 'head', attr=attr, content=content)

class Body(elem.Elem):
	def __init__(self, content = None, attr = {}):
		elem.Elem.__init__(self, tag = 'body', attr=attr, content=content)

class Title(elem.Elem):
	def __init__(self, content = None, attr = {}):
		elem.Elem.__init__(self, tag = 'title', attr=attr, content=content)

class Meta(elem.Elem):
	def __init__(self, content = None, attr = {}):
		elem.Elem.__init__(self, tag = 'meta', attr=attr, content=content, tag_type='simple')

class Img(elem.Elem):
	def __init__(self, content = None, attr = {}):
		elem.Elem.__init__(self, tag = 'img', attr=attr, content=content, tag_type='simple')

class Table(elem.Elem):
	def __init__(self, content = None, attr = {}):
		elem.Elem.__init__(self, tag = 'table', attr=attr, content=content)

class Th(elem.Elem):
	def __init__(self, content = None, attr = {}):
		elem.Elem.__init__(self, tag = 'th', attr=attr, content=content)

class Tr(elem.Elem):
	def __init__(self, content = None, attr = {}):
		elem.Elem.__init__(self, tag = 'tr', attr=attr, content=content)

class Td(elem.Elem):
	def __init__(self, content = None, attr = {}):
		elem.Elem.__init__(self, tag = 'td', attr=attr, content=content)

class Ul(elem.Elem):
	def __init__(self, content = None, attr = {}):
		elem.Elem.__init__(self, tag = 'ul', attr=attr, content=content)

class Ol(elem.Elem):
	def __init__(self, content = None, attr = {}):
		elem.Elem.__init__(self, tag = 'ol', attr=attr, content=content)

class Li(elem.Elem):
	def __init__(self, content = None, attr = {}):
		elem.Elem.__init__(self, tag = 'li', attr=attr, content=content)

class H1(elem.Elem):
	def __init__(self, content = None, attr = {}):
		elem.Elem.__init__(self, tag = 'h1', attr=attr, content=content)

class H2(elem.Elem):
	def __init__(self, content = None, attr = {}):
		elem.Elem.__init__(self, tag = 'h2', attr=attr, content=content)

class H3(elem.Elem):
	def __init__(self, content = None, attr = {}):
		elem.Elem.__init__(self, tag = 'h3', attr=attr, content=content)

class P(elem.Elem):
	def __init__(self, content = None, attr = {}):
		elem.Elem.__init__(self, tag = 'p', attr=attr, content=content)

class Div(elem.Elem):
	def __init__(self, content = None, attr = {}):
		elem.Elem.__init__(self, attr=attr, content=content)

class Span(elem.Elem):
	def __init__(self, content = None, attr = {}):
		elem.Elem.__init__(self, tag = 'span', attr=attr, content=content)

class Hr(elem.Elem):
	def __init__(self, content = None, attr = {}):
		elem.Elem.__init__(self, tag = 'hr', attr=attr, content=content, tag_type='simple')

class Br(elem.Elem):
	def __init__(self, content = None, attr = {}):
		elem.Elem.__init__(self, tag = 'br', attr=attr, content=content, tag_type='simple')

if __name__ == '__main__':
	print( Html( [Head(), Body()] ) )
	print( Html( [Head( Title(elem.Text("Hello ground!")) ), Body( [H1(elem.Text("Oh no, not again!")), Img(attr={"src": "http://i.imgur.com/pfp3T.jpg"})])] ) )