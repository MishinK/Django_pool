#coding=utf8
import random, beverages

class CoffeeMachine:
	def __init__(self):
		self.served = 0
	class EmptyCup(beverages.HotBeverage):
		def __init__(self):
			beverages.HotBeverage.__init__(self, name = "empty cup", price = 0.90)
		def description(self):
			return "An empty cup?! Gimme my money back!"
	class BrokenMachineException(Exception):
		def __init__(self):
			Exception.__init__(self, "This coffee machine has to be repaired.")
	def repair(self):
		self.served = 0
	def serve(self, hot_beverage_class):
		if not issubclass(hot_beverage_class, beverages.HotBeverage):
			raise Exception("Error, parameter must be a class derived from HotBeverage")
		if (self.served >= 10):
			raise self.BrokenMachineException()
		else:
			self.served += 1
			if random.randrange(0, 2):
				return hot_beverage_class()
			else:
				return self.EmptyCup()

if __name__ == "__main__":
	cf = CoffeeMachine()
	for i in range(3):
		try:
			print(cf.serve(beverages.Coffee))
			print(cf.serve(beverages.Tea))
			print(cf.serve(beverages.Chocolate))
			print(cf.serve(beverages.Cappuccino))
		except Exception as e:
			print(e)
	cf.repair()
	for i in range(3):
		try:
			print(cf.serve(beverages.Coffee))
			print(cf.serve(beverages.Tea))
			print(cf.serve(beverages.Chocolate))
			print(cf.serve(beverages.Cappuccino))
		except Exception as e:
			print(e)

