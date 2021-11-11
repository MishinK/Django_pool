#!/usr/bin/python3
# coding: utf-8

from os import close


class Text(str):
    def __str__(self):
        return super().__str__().replace('>', '&gt;').replace('<', '&lt;').replace('"', '&quot;').replace('\n', '\n<br />\n')

class Elem:
	class ValidationError(Exception):
		def __init__(self):
			Exception.__init__(self, "Error")
	
	def set_indent_level(self, elem):
		if isinstance(elem, Elem):
			elem.indent_level += 1
			if len(elem.content) and isinstance(elem.content[0], Elem):
				elem.set_indent_level(elem.content[0])
		return self.indent_level
	
	def tag_start(self):
		if self.tag_type == 'double':
			return "<" + self.tag + self.__make_attr() + ">"
		return "<" + self.tag + self.__make_attr() + " />"
	
	def tag_end(self):
		if self.__make_content() != '':
			return "  " * (self.indent_level - 1) + "</" + self.tag + ">"
		return "</" + self.tag + ">"

	def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
		self.tag = tag
		self.attr = attr
		self.content = []
		if content != None:
			self.add_content(content)
		if tag_type =='double':
			self.tag_type = tag_type
		else:
			self.tag_type = 'simple'
		self.indent_level = 1
			
	def __str__(self):
		if self.tag_type == 'double':
			result = self.tag_start() + self.__make_content() + self.tag_end()
		elif self.tag_type == 'simple':
			result =  self.tag_start() + self.__make_content()
		return result
		
	def __make_attr(self):
		result = ''
		for pair in sorted(self.attr.items()):
			result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
		return result
	
	def __make_content(self):
		if len(self.content) == 0:
			return ''
		result = '\n'
		for elem in self.content:
			result += '  ' * self.set_indent_level(elem) + str(elem) + '\n'
		return result
		
	def add_content(self, content):
		if not Elem.check_type(content):
			raise Elem.ValidationError
		if type(content) == list:
			self.content += [elem for elem in content if elem != Text('')]
		elif content != Text(''):
			self.content.append(content)
			
	@staticmethod
	def check_type(content):
		return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))

if __name__ == '__main__':
	html = Elem(tag = 'html')
	head = Elem(tag = 'head')
	head.add_content(Elem(tag = 'title', content=Text("Hello ground!")))
	body = Elem(tag = 'body')
	body.add_content(Elem(tag = 'h1', content=Text("Oh no, not again!")))
	body.add_content(Elem(tag = 'img', tag_type = 'simple', attr = {'src': "http://i.imgur.com/pfp3T.jpg"}))
	html.add_content([head, body])
	print(str(html))
	with open("my.html", "w") as Html_file:
		Html_file.write(str(html))
