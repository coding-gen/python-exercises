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
	print(f'Original lists: {l1} and {l2}')

	l3 = []
	for i in range(max(len(l1), len(l2))):
		if i % 2 == 0:
			l3.append(l2[i])
		else:
			l3.append(l1[i])
	return l3


def odds_n_evens_cat(l1, l2):
	"""
	Return a list of the concatenation of odd-index elements of l1
	and then even-index elements of l2.
	"""
	print(f'Original lists: {l1} and {l2}')

	l3 = l1[1::2]
	l3 += l2[0::2]
	return l3


def jumpin_around(l1):
	print(f'List originally: {l1}')
	# remove the item present at index 4 and add it to the 2nd position and at the end
	temp = l1.pop(4)
	print(f'removed {temp}: {l1}')
	l1 = l1[:2] + [temp] + l1[2:] + [temp]
	print(f'new list: {l1}')
	return l1


def reversed_thirds(l1):
	print(f'List originally: {l1}')
	#Slice list into 3 equal chunks and reverse each chunk
	result = l1[len(l1)//3-1::-1]
	result += l1[2 * len(l1)//3-1:len(l1)//3-1:-1]
	result += l1[:2 * len(l1)//3-1:-1]
	print(f'List transformed: {result}')
	"""
	result += l1[len(l1) // 3: 2 * len(l1) // 3].reverse()
	result += l1[2 * len(l1) // 3:].reverse()
	"""
	return result



def main():
	print(odds_n_evens_merge([3, 6, 9, 12, 15, 18, 21], [4, 8, 12, 16, 20, 24, 28]))
	print(odds_n_evens_cat([3, 6, 9, 12, 15, 18, 21], [4, 8, 12, 16, 20, 24, 28]))
	jumpin_around([34, 54, 67, 89, 11, 43, 94])
	reversed_thirds([11, 45, 8, 23, 14, 12, 78, 45, 89])
	reversed_thirds([11, 45, 8, 23, 14, 12])




if __name__ == '__main__':
	main()





