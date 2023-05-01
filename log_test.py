#! /usr/bin/python3

"""
Author: Genevieve LaLonde

Python Dataset coding exercise from: 
https://pynative.com/python-functions-exercise-with-solutions/
"""

import argparse
import logging



parser = argparse.ArgumentParser(description='A set of simple data structure exercises in python.')
parser.add_argument('-v',
	'--verbose',
	default = False,
	dest='verbose',
	action='store_true',
	help='Output details of exercises.')
parser.add_argument('-o',
	'--outfile',
	default = False,
	dest='outfile',
	action='store_true',
	help='Output to file instead of stdout.')
parser.add_argument('-f',
	'--filename',
	type=str,
	default = 'py_function.log',
	dest='log_filename',
	help='Name of file where to save.')
args = parser.parse_args()


def main():
	if args.verbose:
		log_level=logging.INFO
	if args.outfile:
		logging.basicConfig(
			level=log_level, 
			filename=args.log_filename,
			filemode='w', 
			format='%(asctime)s:%(levelname)s : %(message)s'
		)
	else:
		logging.basicConfig(
			level=log_level, 
			format='%(asctime)s:%(levelname)s : %(message)s'
		)


	logger = logging.getLogger('test_logger')
	logger.info('This is an info message.')
	logger.warning('This is a warning.')



if __name__ == '__main__':
	main()





