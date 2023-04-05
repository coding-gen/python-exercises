#! /usr/bin/python3

"""
Author: Genevieve LaLonde

Python Dataset coding exercise from: 
# https://pynative.com/python-functions-exercise-with-solutions/
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


def test_tuple(function, exercise, result, *given):
	r = function(*given)
	assert result[0] == r[0], f"Failure exercise {exercise}: min wrong." 
	assert result[1] == r[1], f"Failure exercise {exercise}: max wrong."
	assert sum(result[2]) == sum(r[2]), f"Failure exercise {exercise}."
	assert len(result[2]) == len(r[2]), f"Failure exercise {exercise}."


def test(function, exercise, result, *given):
	assert result == function(*given), f"Failure exercise {exercise}."


def main():
	test(print_2_args, 1, ('Rebecca', 24), 'Rebecca', 24)
	test(print_many_args, 2, ('Rebecca', 24), 'Rebecca', 24)
	test(print_many_args, 2, ('Annie', 781, 'b2', 'Jemima', 7.24), 'Annie', 781, 'b2', 'Jemima', 7.24)


if __name__ == '__main__':
	main()





