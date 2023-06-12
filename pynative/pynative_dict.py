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


def extract_keys(keys, d):
	return {key: d[key] for key in keys}


def delete_keys(keys, d):
	for key in keys:
		if key in d:
			d.pop(key)
	return d


def check_existence(d, v):
	return v in d.values()


def rename_key(d, old_k, new_k):
	d[new_k] = d.pop(old_k)
	return d


def min_valued_key(d):
	# Order by the values, and return the smallest valued dict key.
	return min(d, key=d.get) 


def salary_update(d, name, salary):
	# Here we assume name is a primary key, due to the simplicity of the data structure
	for record in d.values():
		if record['name'] == name:
			record['salary'] = salary
	return d


def dict_create_fromkeys(d):
	return dict.fromkeys(d.keys())


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
	test(
		extract_keys, 
		5,
		"Exctracting keys {} from dict {}.",
		{'name': 'Kelly', 'salary': 8000},
		["name", "salary"],
		{"name": "Kelly", "age":25,  "salary": 8000,  "city": "New york"}
		)
	test(
		delete_keys, 
		6,
		"Deleting keys {} from dict {}.",
		{'city': 'New york', 'age': 25},
		["name", "salary"],
		{"name": "Kelly", "age":25,  "salary": 8000,  "city": "New york"}
		)
	test(
		check_existence,
		7, 
		"The dict {} contains the value {}: ",
		True,
		{'a': 100, 'b': 200, 'c': 300},
		200
		)
	test(
		rename_key,
		8, 
		"In dict {} renaming key `{}` to `{}`.",
		{'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'},
		{
		"name": "Kelly",
		"age":25,
		"salary": 8000,
		"city": "New york"
		},
		'city', 
		'location'
		)
	test(
		min_valued_key,
		9,
		"The class with the least students out of: {}",
		'Math',
		{
		'Physics': 82,
		'Math': 65,
		'History': 75
		}
		)
	test(
		salary_update,
		10,
		"Updating {} so that {} has salary: {}.",
		{
			'emp1': {'name': 'Jhon', 'salary': 7500},
			'emp2': {'name': 'Emma', 'salary': 8000},
			'emp3': {'name': 'Brad', 'salary': 8500}
		},
		{
			'emp1': {'name': 'Jhon', 'salary': 7500},
			'emp2': {'name': 'Emma', 'salary': 8000},
			'emp3': {'name': 'Brad', 'salary': 500}
		},
		'Brad',
		8500
		)

	test(
		dict_create_fromkeys,
		11, 
		"Creating empty dict from the keys of {}",
		{'name': None, 'age': None, 'salary': None, 'city': None},
		{
			"name": "Kelly",
			"age": 25,
			"salary": 8000,
			"city": "New york"
			}
		)



if __name__ == '__main__':
	main()

