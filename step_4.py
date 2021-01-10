import time
import pandas as pd
import numpy as np
def read_split():
	"""Do  opening,reading and spliting of file contents at new line

	Function Parameters:None

	Function Returns:Two lists
	"""
	with open('subset_elemets.txt') as f:
		subset_elements = f.read().split('\n')
	with open('all_elements.txt') as f:
		all_elements = f.read().split('\n')
	return subset_elements,all_elements
def unique_elements1(subset_elements,all_elements):
	"""Print number of unique elements in both the lists and the time taken to do this

	Function Parameters:2
	Parameter1:The sub list
	Parameter2:A main list
	"""
	start = time.time()
	verified_elements=[]
	for element in subset_elements:
		if element in all_elements:
			verified_elements.append(element)
			print(len(verified_elements))
			print('Duration: {} seconds'.format(time.time() - start))
def unique_elements2(subset_elements,all_elements):
	"""Print number of unique elements in both the lists and the time taken to do this

	Function Parameters:2
	Parameter1:The sub list
	Parameter2:The main list
	"""
	start = time.time()
	verified_elements = np.intersect1d(all_elements,subset_elements)
	print(len(verified_elements))
	print('Duration: {} seconds'.format(time.time() - start))
def unique_elements3(subset_elements,all_elements):
	"""Print number of unique elements in both the lists and the time taken to do this

	Function Parameters:2
	Parameter1:The sub list
	Parameter2:The main list
	"""
	start = time.time()
	verified_elements = list(set(subset_elements) & set(all_elements))
	print(len(verified_elements))
	print('Duration: {} seconds'.format(time.time() - start))
def main():
	"""This is the main function that calls all the above function to perform the task"""

	unique_elements1(read_split())
	unique_elements2(read_split())
	unique_elements3(read_split())
main()
