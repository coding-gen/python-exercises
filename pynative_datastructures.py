#! /usr/bin/python3

"""
Python Dataset coding exercise from: 
# https://pynative.com/python-data-structure-exercise-for-beginners/
"""

def odds_n_evens_merge(l1, l2):
	"""
	Return a list of odd-index elements of l1
	and even-index elements of l2.
	"""
	print("Merging every other element of 2 lists.")
	print(f'Original lists: {l1} and {l2}')

	l3 = []
	for i in range(max(len(l1), len(l2))):
		if i % 2 == 0:
			l3.append(l2[i])
		else:
			l3.append(l1[i])
	print(l3)
	print()
	return l3


def odds_n_evens_cat(l1, l2):
	"""
	Return a list of the concatenation of odd-index elements of l1
	and then even-index elements of l2.
	"""
	print("Odd elements of first list, followed by even elements of second.")
	print(f'Original lists: {l1} and {l2}')
	l3 = l1[1::2]
	l3 += l2[0::2]
	print(l3)
	print()
	return l3


def jumpin_around(l1):
	# remove the item present at index 4 and add it to the 2nd position and at the end
	print("Move element from index 4 to 2 and copy it to the end.")
	print(f'List originally: {l1}')
	temp = l1.pop(4)
	print(f'removed {temp}: {l1}')
	l1 = l1[:2] + [temp] + l1[2:] + [temp]
	print(f'Adding {temp} at second and end positions: \n{l1}')
	print()
	return l1


def reversed_thirds(l1):
	#Slice list into 3 equal chunks and reverse each chunk
	print("Reverse each third of a list.")
	print(f'List originally: {l1}')
	result = l1[len(l1)//3-1::-1]
	result += l1[2 * len(l1)//3-1:len(l1)//3-1:-1]
	result += l1[:2 * len(l1)//3-1:-1]
	print(f'List transformed: {result}')
	print()
	return result


def count_distinct(l):
	# Count the occurrence of each element of a list
	print("Count of distinct elements of a list.")
	print(f'List: {l}')
	d = {}
	for element in l:
		if element in d:
			d[element] += 1
		else:
			d[element] = 1
	print(f'Count: {d}')
	print()
	return d


def couples(l1, l2):
	# Pair up the elements of 2 lists as tuples in a set.
	print("Pairing up these lists: ")
	print(l1, l2)
	if len(l1) != len(l2):
		print("Lists must be the same length.")
	s = set(zip(l1, l2))
	print(f"Pairings (squares): {s}")
	return s



def main():
	odds_n_evens_merge([3, 6, 9, 12, 15, 18, 21], [4, 8, 12, 16, 20, 24, 28])
	odds_n_evens_cat([3, 6, 9, 12, 15, 18, 21], [4, 8, 12, 16, 20, 24, 28])
	jumpin_around([34, 54, 67, 89, 11, 43, 94])
	reversed_thirds([11, 45, 8, 23, 14, 12, 78, 45, 89])
	reversed_thirds([11, 45, 8, 23, 14, 12])
	count_distinct([11, 45, 8, 11, 23, 45, 23, 45, 89])
	couples([2, 3, 4, 5, 6, 7, 8], [4, 9, 16, 25, 36, 49, 64])


if __name__ == '__main__':
	main()





