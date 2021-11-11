#coding=utf8
class HotBeverage:
	def __init__(self, name = "hot beverage", price = 0.30):
		self.name = name
		self.price = price
	def description(self):
		return  "Just some hot water in a cup."
	def __str__(self):
		return """\
name : %s
price : %0.2f
description : %s
""" % (self.name, self.price, self.description())

class Coffee(HotBeverage):
	def __init__(self):
		HotBeverage.__init__(self, name = "coffee", price = 0.40)
	def description(self):
		return "A coffee, to stay awake."

class Tea(HotBeverage):
	def __init__(self):
		HotBeverage.__init__(self, name = "tea")

class Chocolate(HotBeverage):
	def __init__(self):
		HotBeverage.__init__(self, name = "chocolate", price = 0.50)
	def description(self):
		return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
	def __init__(self):
		HotBeverage.__init__(self, name = "cappuccino", price = 0.45)
	def description(self):
		return "Un po’ di Italia nella sua tazza!"

if __name__ == "__main__":
	print(HotBeverage(), Coffee(), Tea(), Chocolate(), Cappuccino(), sep = '', end = '')