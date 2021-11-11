#!/usr/bin/python3
# coding: utf-8

from elem import Text, Elem
from elements import *

class Page:
	def __init__(self, elem):
		self.elem = elem
	
	def __str__(self):
		if isinstance(self.elem, Html):
			return '<!DOCTYPE html>\n' + str(self.elem)
		return str(self.elem)
	
	def write_to_file(self, filename):
		with open(filename, "w") as Html_file:
			Html_file.write(str(self))

	@staticmethod
	def check_type(content):
		return (isinstance(content, elem.Elem) or type(content) == elem.Text or
                (type(content) == list and all([type(elem) == elem.Text or
                                                isinstance(elem, elem.Elem)
                                                for elem in content])))
	def is_valid(self):
		if not Page.check_type(self.elem):
			return False
		for el in self.elem.content:
			if isinstance(el, Elem):
				if not Page(el).is_valid():
					return False
		if isinstance(self.elem, Html):
			if len(self.elem.content) != 2 or (not isinstance(self.elem.content[0], Head))\
                or (not isinstance(self.elem.content[1], Body)):
				return False
		if isinstance(self.elem, Head):
			if len(self.elem.content) != 1 or (not isinstance(self.elem.content[0], Title)):
				return False
		if isinstance(self.elem, Body) or isinstance(self.elem, Div):
			for el in self.elem.content:
				if (not isinstance(el, H1)) and (not isinstance(el, H2)) and (not isinstance(el, Div)) and (not isinstance(el, Table)) and (not isinstance(el, Ul)) and (not isinstance(el, Ol))\
                	and (not isinstance(el, Span)) and (not isinstance(el, Text)):
						return False
		if isinstance(self.elem, Title) or isinstance(self.elem, H1) or isinstance(self.elem, H2) or isinstance(self.elem, Li) or \
            isinstance(self.elem, Th) or isinstance(self.elem, Td):
			if len(self.elem.content) != 1 or (not isinstance(self.elem.content[0], Text)):
				return False
		if isinstance(self.elem, P):
			for el in self.elem.content:
				if not isinstance(el, Text):
					return False
		if isinstance(self.elem, Span):
			for el in self.elem.content:
				if not isinstance(el, Text) and not isinstance(el, P):
					return False
		if isinstance(self.elem, Ul) or isinstance(self.elem, Ol):
			for el in self.elem.content:
				if not isinstance(el, Li):
					return False
				if len(self.elem.content) == 0: 
					return False
		if isinstance(self.elem, Tr):
			if len(self.elem.content) == 0 or \
				(not isinstance(self.elem.content[0], Td)  and not isinstance(self.elem.content[0], Th)):
				return False
			if isinstance(self.elem.content[0], Td):
				for el in self.elem.content:
					if not isinstance(el, Td):
						return False
			if isinstance(self.elem.content[0], Th):
				for el in self.elem.content:
					if not isinstance(el, Th):
						return False
		if isinstance(self.elem, Table):
				for el in self.elem.content:
					if not isinstance(el, Tr):
						return False
		return True
	
if __name__ == '__main__':
	
	page = Page(Html( [Head( Title(elem.Text("Hello ground!")) ), Body(H1(Text("Oh no, not again!"))) ] ) )
	if page.is_valid() == True:
		print(page)
	
	page = Page(Html( [Head( Title(elem.Text("Hello ground!")) ), Body([H1(elem.Text("Oh no, not again!")), Img(attr={"src": "http://i.imgur.com/pfp3T.jpg"})])] ))
	if page.is_valid() == True:
		print(page)
	
	page = Page(Html( [Head( Title(elem.Text("Hello ground!")) ), Body([H1(elem.Text("Oh no, not again!")), Div(Table())])] ))
	if page.is_valid() == True:
		print(page)

	page = Page(Html( [Head( Title(elem.Text("Hello ground!")) ), Body([H1(elem.Text("Oh no, not again!")), Div(Table(Tr([Td(), Tr()])))])] ))
	if page.is_valid() == True:
		print(page)
	
	page = Page(Html( [Head( Title(elem.Text("Hello ground!")) ), Body( [H1(elem.Text("Oh no, not again!")), Div( Table( Tr( [Td(Text("1")), Td(Text("1"))] ))) ] )] ))
	if page.is_valid() == True:
		print(page)