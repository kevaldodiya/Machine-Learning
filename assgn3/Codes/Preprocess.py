import csv
import os
import re


def preprocessEachWord(word):

	tempWord = ""
	for letter in word:
		if (letter >= 'a' and letter <= 'z') or (letter >= 'A' and letter <= 'Z'):
			tempWord += letter

	tempWord = tempWord.lower()
	return tempWord

def preprocessFile(filename):
	words = []
	with open(filename, "r", errors="ignore") as file:
		filedata = file.readlines()

		for line in filedata:
			for word in re.split('[^a-zA-Z]', line):
				if(word == ""):
					continue
				if(word[0] == '\\' or word[0] == '<' or word[0] == '{' or word[0] == '['):
					continue
				word = preprocessEachWord(word)
				if(word == ""):
					continue
				words.append(word)

	return words

def preprocessFiles(filenames):
	words = []
	for filename in filenames:
		words += preprocessFile(filename)

	return words

def createDictionaryFromWords(words):
	frequencies = [words.count(word) for word in words]
	return dict(list(zip(words, frequencies)))

def saveDictionaryToCSV(dic, filename):
	with open(filename, "w+") as file:
		for word in dic.keys():
			file.write("%s %d\n" % (word, dic[word]))

def readDictionaryFromCSV(filename, datatype="float"):
	dic = {}
	if not os.path.exists(filename):
		return dic
	with open(filename, "r") as file:
		filedata = file.readlines()
		for line in filedata:
			word, frequency = line.split(" ")
			if(datatype == "float"):
				dic[str(word)] = float(frequency)
			elif(datatype == "int"):
				dic[str(word)] = int(frequency)
			else:
				dic[str(word)] = frequency

	return dic



