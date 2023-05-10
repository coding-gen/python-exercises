#! /usr/bin/python3

"""
Author: Genevieve LaLonde

Python Dataset coding exercise from: 
https://pynative.com/python-functions-exercise-with-solutions/
"""

import argparse


parser = argparse.ArgumentParser(description='A set of simple data structure exercises in python.')
parser.add_argument('-v',
	'--verbose',
	default = False,
	dest='verbose',
	action='store_true',
	help='Output details of exercises.')
args = parser.parse_args()


def print_2_args(name, age):
	# Take 2 args, print their value.
	if args.verbose:
		print("\nReceived these arguments.")
	print(f"Name: {name}, Age: {age}")
	return (name, age)


def print_many_args(*arguments):
	# Print a variable amount of args.	
	if args.verbose:
		print("\nReceived these arguments.")
	for arg in arguments:
		print(f"arg: {arg}")
	return (arguments)


def calculation(a, b):
	# Return the addition and subtraction of 2 numbers in 1 result.
	if args.verbose:
		print("\nCalculating on these arguments.")
		print(a, b)
	print(f"Result: {a + b, a - b}")
	return a + b, a - b


def show_employee(name, salary=9000):
	# Display the name and salary of an employee. Default salary=9000.
	print(f"Name: {name}, Salary: {salary}")
	return name, salary


def outer_addition(a, b):
	# Create an outer and inner function. 
	# The inner function adds the parameters.
	# The outer function adds 5 more.
	if args.verbose:
		print(f"\nAdding 3 times {b}, and 5 to {a}.")
	def inner_addition(x, y):
		return x + y

	add_once = inner_addition(a, b)
	add_twice = inner_addition(add_once, b)
	add_thrice = inner_addition(add_twice, b)
	result = inner_addition(add_thrice, 5)

	print(f"Result: {result}")
	return result


def recur_addition(n):
	if n == 1:
		return 1
	return n + recur_addition(n - 1)


def recur_addition_wrapper(n):
	# Calculate the sum of numbers from 0 to n recursively.
	if args.verbose:
		print(f"\nCalculating sum from 0 to {n}.")
	result = recur_addition(n)
	print(f"Result: {result}")
	return result


def evens(n, m):
	# Generate a list of even numbers between n and m.
	if args.verbose:
		print(f"\nEven numbers from {n} to {m}.")
	result = list(range(n, m, 2))
	print(f"Result: {result}")
	return result

def max_item(l):
	# Return the max item of the list.
	if args.verbose:
		print(f"\nMax item in list: {l}.")
	m = l[0]
	for item in l:
		if item > m:
			m = item
	result = m
	print(f"Result: {result}")
	return result


def test_tuple(function, exercise, result, *given):
	r = function(*given)
	assert result[0] == r[0], f"Failure exercise {exercise}: min wrong." 
	assert result[1] == r[1], f"Failure exercise {exercise}: max wrong."
	assert sum(result[2]) == sum(r[2]), f"Failure exercise {exercise}."
	assert len(result[2]) == len(r[2]), f"Failure exercise {exercise}."


def test(function, exercise, result, *given):
	assert result == function(*given), f"Failure exercise {exercise}."


def main():
	# Usage: test(function_name, exercise_number, expected_result, input[s])

	test(print_2_args, 1, ('Rebecca', 24), 'Rebecca', 24)
	test(print_many_args, 2, ('Rebecca', 24), 'Rebecca', 24)
	test(print_many_args, 2, ('Annie', 781, 'b2', 'Jemima', 7.24), 'Annie', 781, 'b2', 'Jemima', 7.24)
	test(calculation, 3, (50, 30), 40, 10)
	test(show_employee, 4, ("Ben", 12000), "Ben", 12000)
	test(show_employee, 4, ("Jessa", 9000), "Jessa")
	test(outer_addition, 5, 28, 2, 7)
	test(recur_addition_wrapper, 6, 55, 10)
	# exercise 7 was dumb.
	test(evens, 8, [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28], 4, 30)
	test(max_item, 9, 24, [4, 6, 8, 24, 12, 2])


if __name__ == '__main__':
	main()





