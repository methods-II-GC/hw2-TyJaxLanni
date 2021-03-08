#!/usr/bin/env python
"""One-line description of the program goes here."""
"""This is an edit for fun."""

import argparse

from typing import Iterator, List
import random


"""
Read all of the input data in using the above snippet.
Split the data into an 80% training set, 10% development set, and 10% test set.
Write the training set to the train path.
Write the develoment set to the dev path.
Write the testing set to the test path.
The resulting training, development, and testing set files should be in the same columnar format as the input format.
"""

#-----------------------------------------------------------

#-----------------------------------------------------------
def read_tags(path: str) -> Iterator[List[List[str]]]:
	with open(path, "r") as source:
		lines = []
		for line in source:
			line = line.rstrip()
			if line:  # Line is contentful.
				lines.append(line.split())
			else:  # Line is blank.
				yield lines.copy()
				lines.clear()
	# Just in case someone forgets to put a blank line at the end...
	if lines:
		yield lines




#---------------------------------------------------------

#-----------------------------------------------------------
def write_tags(data: List[List[List[str]]], write_path: str) -> None:
	with open(write_path, "w", encoding="utf-8") as file:
		for sentence in data:
			for tok in sentence:
				word_info = " ".join(tok)
				#word_info.join(tok)

				file.write(word_info)
				file.write("\n")
			file.write("\n")







#---------------------------------------------------------

#-----------------------------------------------------------
def split_data(data: Iterator[List[List[str]]], seed: int) -> List[List[List[List[str]]]]:

	#creating pseudorandom environment
	random.seed(seed)

	#shuffle data
	random.shuffle(data)

	#creating training data size
	data_size = len(data)
	train_size = int(data_size*.8)
	dev_test_size = int(data_size*.1)

	#train: 80% of the data, dev/test: 20% of data
	train = data[:train_size]	#data[0: .8 size of data]
	dev = data[train_size: (train_size+dev_test_size)]	#data[.8 size of data: .9 size of data]
	test = data[(train_size+dev_test_size):]		#data[.9 size of data: end of data]

	return (train, dev, test)






#---------------------------------------------------------

#-----------------------------------------------------------
def main(args: argparse.Namespace) -> None:

	#step 1) Read all of the input data in using the above snippet.
	corpus = list(read_tags(args.input))

	#step2) Split the data into an 80% training set, 10% development set, and 10% test set.
	train, dev, test = split_data(corpus, args.seed)

	#step 3) Write the training set to the train path.
	write_tags(train, args.train)

	#step 4) Write the development set to the dev path.
	write_tags(dev, args.dev)

	#step 5) Write the testing set to the test path.
	write_tags(test, args.test)



#----------------------------------------------------------

#-----------------------------------------------------------
if __name__ == "__main__":

	parser = argparse.ArgumentParser()

	parser.add_argument(
		"input", type=str, help= "File for our program to read/store"
		)
	parser.add_argument(
		"train", type= str, help= "File to write our train data into"
		)
	parser.add_argument(
		"dev", type=str, help= "File to write our dev data into"
		)
	parser.add_argument(
		"test", type=str, help="File to write our test data into"
		)
	parser.add_argument(
		"--seed", type=int, help="An integer to create a pseuodrandom seed", required= True)

	args = parser.parse_args()

	main(args)
