class Pizza:
	count=0
	def __init__(self, ingredients):
		self.ingredients=ingredients
		Pizza.count+=1
		self.order_number=Pizza.count
	@classmethod
	def garden_feast(cls):
		ingredients=["spinach", "olives", "mushroom"]
		return cls(ingredients)
	@classmethod
	def meat_festival(cls):
		ingredients=["beef", "meatball", "bacon"]
		return cls(ingredients)
	@classmethod
	def hawaiian(cls):
		ingredients=["ham", "pineapple"]
		return cls(ingredients)
p2 = Pizza.garden_feast()
p1 = Pizza(["bacon", "parmesan", "ham"])
print(p2.__dict__)

print(p1.ingredients)
print(p1.__dict__)
p3 = Pizza.hawaiian()
print(p3.ingredients, p3.order_number)