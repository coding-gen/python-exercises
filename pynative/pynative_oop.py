#! /usr/bin/python3

"""
Author: Genevieve LaLonde

Python Object Oriented Programming coding exercise from: 
https://pynative.com/python-object-oriented-programming-oop-exercise
"""

FLEET_CAR_COLOR = 'blue'


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
		self.color = FLEET_CAR_COLOR


	def __str__(self):
		items = vars(self)
		l =[f"{key}: {items[key]}" for key in items]
		s = "\n".join(l)
		return s

	def fare(self):
		return self.capacity * 100


class Bus(Vehicle):
	# Bus object inherits the parent Vehicle class.
	def __init__(self, name, max_speed=80, mileage=2000, capacity=50):
		super(Bus, self).__init__(name, max_speed, mileage, capacity)


	def fare(self):
		# Additional bus maintenance fee
		return super().fare() * 1.1


class Car(Vehicle):
	pass


def main():
	modelX = Vehicle('modelX', 240, 18)
	print(f"vehicle modelX: \n{modelX}")
	school_bus = Bus("School Volvo", 180, 12)
	print(f"\nvehicle school bus: \n{school_bus}")
	print(f"\nThe fare for the school bus: \n{school_bus.fare()}")
	print(f"A school bus is a {type(school_bus)}.")
	print(f"It also counts as a {Bus.__bases__}.")


if __name__ == '__main__':
	main()

