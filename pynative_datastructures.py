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
	l3 = l1[1::2]
	l3 += l2[0::2]
	return l3


def jumpin_around(l1):
	temp = l1.pop(4)
	print(f'removed {temp} from {l1}')
	l1 = l1[:2] + [temp] + l1[2:] + [temp]
	print(f'new list: {l1}')




def main():
	print(odds_n_evens_merge([3, 6, 9, 12, 15, 18, 21], [4, 8, 12, 16, 20, 24, 28]))
	print(odds_n_evens_cat([3, 6, 9, 12, 15, 18, 21], [4, 8, 12, 16, 20, 24, 28]))
	jumpin_around([34, 54, 67, 89, 11, 43, 94])



if __name__ == '__main__':
	main()





