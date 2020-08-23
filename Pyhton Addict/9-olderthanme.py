class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def compare_age(self, other):
        self.other = other 
        if self.age > other.age:
            print("{} is younger than {}".format(self.name, other.name))
        elif self.age < other.age:
            print("{} is older than {}".format(self.name, other.name))
        else:
            print("{} is the same age {}".format(self.name, other.name))

p1 = Person("Samuel", 24)
p2 = Person("Joel", 36)
p3 = Person("Lily", 24)

p1.compare_age(p2)
p2.compare_age(p1)
p1.compare_age(p3)
print(p1.name)

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def compare_age(self, other):
		if self.age>other.age:
			return "{} is younger than me.".format(other.name)
		elif self.age<other.age:
			return "{} is older than me.".format(other.name)
		else:
			return "{} is the same age as me.".format(other.name)

p1 = Person("Samuel", 24)
p2 = Person("Joel", 36)
p3 = Person("Lily", 24)

print(p1.compare_age(p2))
print(p2.compare_age(p1))
print(p1.compare_age(p3))