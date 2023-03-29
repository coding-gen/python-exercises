#! /usr/bin/python3

"""
Author: Genevieve LaLonde

Python Dataset coding exercise from: 
# https://pynative.com/python-data-structure-exercise-for-beginners/
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


def odds_n_evens_merge(l1, l2):
	"""
	Return a list of odd-index elements of l1
	and even-index elements of l2.
	"""
	if args.verbose:
		print("\nMerging every other element of 2 lists.")
		print(f'Original lists: {l1} and {l2}')

	l3 = []
	for i in range(max(len(l1), len(l2))):
		if i % 2 == 0:
			l3.append(l2[i])
		else:
			l3.append(l1[i])
	print(f"Result: {l3}")
	return l3


def odds_n_evens_cat(l1, l2):
	"""
	Return a list of the concatenation of odd-index elements of l1
	and then even-index elements of l2.
	"""
	if args.verbose:
		print("\nOdd elements of first list, followed by even elements of second.")
		print(f'Original lists: {l1} and {l2}')
	l3 = l1[1::2]
	l3 += l2[0::2]
	print(f"Result: {l3}")
	return l3


def jumpin_around(l1):
	# remove the item present at index 4 and add it to the 2nd position and at the end
	if args.verbose:
		print("\nMove element from index 4 to 2 and copy it to the end.")
		print(f'List originally: {l1}')
	temp = l1.pop(4)
	l1 = l1[:2] + [temp] + l1[2:] + [temp]
	print(f"Result: {l1}")
	return l1


def reversed_thirds(l1):
	#Slice list into 3 equal chunks and reverse each chunk
	if args.verbose:
		print("\nReverse each third of a list.")
		print(f'List originally: {l1}')
	result = l1[len(l1)//3-1::-1]
	result += l1[2 * len(l1)//3-1:len(l1)//3-1:-1]
	result += l1[:2 * len(l1)//3-1:-1]
	print(f'Result: {result}')
	return result


def count_distinct(l):
	# Count the occurrence of each element of a list
	if args.verbose:
		print("\nCount of distinct elements of a list.")
		print(f'List: {l}')
	d = {}
	for element in l:
		if element in d:
			d[element] += 1
		else:
			d[element] = 1
	print(f'Result: {d}')
	return d


def couples(l1, l2):
	# Pair up the elements of 2 lists as tuples in a set.
	if args.verbose:
		print("\nPairing up these lists: ")
		print(l1, l2)
	if len(l1) != len(l2):
		print("Lists must be the same length.")
	s = set(zip(l1, l2))
	print(f"Result: {s}")
	return s


def test(function, exercise, result, *given):
	assert result == function(*given), f"Failure exercise {exercise}."


def main():
	test(odds_n_evens_merge, '1a', [4, 6, 12, 12, 20, 18, 28], [3, 6, 9, 12, 15, 18, 21], [4, 8, 12, 16, 20, 24, 28])
	test(odds_n_evens_cat, '1b', [6, 12, 18, 4, 12, 20, 28], [3, 6, 9, 12, 15, 18, 21], [4, 8, 12, 16, 20, 24, 28])
	test(jumpin_around, '2', [34, 54, 11, 67, 89, 43, 94, 11], [34, 54, 67, 89, 11, 43, 94])
	test(reversed_thirds, '3', [11, 45, 8, 23, 14, 12, 78, 45, 89], [8, 45, 11, 12, 14, 23, 89, 45, 78])
	test(reversed_thirds, '3', [11, 45, 8, 23, 14, 12], [45, 11, 23, 8, 12, 14])
	test(count_distinct, '4', {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}, [11, 45, 8, 11, 23, 45, 23, 45, 89])
	test(couples, '5', {(7, 49), (2, 4), (4, 16), (8, 64), (6, 36), (3, 9), (5, 25)}, [2, 3, 4, 5, 6, 7, 8], [4, 9, 16, 25, 36, 49, 64])
	"""
	test(jumpin_around, '6', , )
	test(jumpin_around, '7', , )
	test(jumpin_around, '8', , )
	"""


if __name__ == '__main__':
	main()





