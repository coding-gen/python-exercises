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
	if args.verbose:
		print(f"\nZipping [keys] and [values] into a dict.")
	result = dict(zip(keys, values))
	print(f"Result: {result}")
	return result


def dict_merge(d1, d2):
	# Merge 2 dicts.
	if args.verbose:
		print(f"\nMerging {d1} and {d2}.")
	d1.update(d2)
	print(f"Result: {d1}")
	return d1


def test(function, exercise, result, *given):
	assert result == function(*given), f"Failure exercise {exercise}."


def main():
	# Usage: test(function_name, exercise_number, expected_result, input[s])

	test(dict_create, 1, {'Ten': 10, 'Twenty': 20, 'Thirty': 30}, ['Ten', 'Twenty', 'Thirty'], [10, 20, 30])
	test(
		dict_merge, 
		2, 
		{'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}, 
		{'Ten': 10, 'Twenty': 20, 'Thirty': 30}, 
		{'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
		)



if __name__ == '__main__':
	main()

