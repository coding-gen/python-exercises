#! /usr/bin/python3

"""
Author: Genevieve LaLonde

Python Object Oriented Programming coding exercise from: 
https://pynative.com/python-object-oriented-programming-oop-exercise
"""

class Vehicle:
	# Vehicle class without any variables nor methods
	pass


class Vehicle:
	# create a Vehicle class with max_speed and mileage instance attributes.
	def __init__(self, name, max_speed=120, mileage=0, capacity=5):
		self.name = name
		self.max_speed = max_speed
		self.mileage = mileage
		self.capacity = capacity


	def __str__(self):
		items = vars(self)
		l =[f"{key}: {items[key]}" for key in items]
		s = "\n".join(l)
		return s


class Bus(Vehicle):
	# Bus object inherits the parent Vehicle class.
	def __init__(self, name, max_speed=80, mileage=2000, capacity=50):
		super(Bus, self).__init__(name, max_speed, mileage, capacity)



def main():
	modelX = Vehicle('modelX', 240, 18)
	print(f"vehicle modelX: \n{modelX}")
	school_bus = Bus("School Volvo", 180, 12)
	print(f"\nvehicle school bus: \n{school_bus}")


if __name__ == '__main__':
	main()

