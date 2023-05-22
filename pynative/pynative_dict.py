#! /usr/bin/python3

"""
Author: Genevieve LaLonde

Python Dictionary coding exercises from: 
https://pynative.com/python-dictionary-exercise-with-solutions/
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


def dict_create(keys, values):
	# Create a dictionary from 2 lists.
	return dict(zip(keys, values))


def dict_merge(d1, d2):
	# Merge 2 dicts.
	d1.update(d2)
	return d1


def get_history(d):
	# Get the value of key ‘history’ from the below dict
	return d['class']['student']['marks']['history']


def dict_default_create(keys, values={"designation": 'Developer', "salary": 8000}):
	# Initialize a dictionary with default values
	return dict.fromkeys(keys, values)


def test(function, exercise, message, result, *given):
	if args.verbose:
		print(f"\nExercise {exercise}")
		print(message.format(*given))
	function_result = function(*given)
	print(f"Result: {function_result}")
	assert result == function_result, f"Failure exercise {exercise}."


def main():
	# Usage: test(function_name, exercise_number, expected_result, input[s])

	test(
		dict_create, 
		1, 
		"Zipping {} and {} into a dict.",
		{'Ten': 10, 'Twenty': 20, 'Thirty': 30}, 
		['Ten', 'Twenty', 'Thirty'], [10, 20, 30]
		)
	test(
		dict_merge, 
		2, 
		"Merging {} and {}",
		{'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}, 
		{'Ten': 10, 'Twenty': 20, 'Thirty': 30}, 
		{'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
		)
	test(
		get_history, 
		3,
		"Determining Mike's grade in history class.",
		80,
		{"class": {"student": {"name": "Mike","marks": {"physics": 70,"history": 80}}}}
		)
	test(
		dict_default_create, 
		4,
		"Initializing new employees database for employees {}.",
		{'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}},
		['Kelly', 'Emma']
		)


if __name__ == '__main__':
	main()

