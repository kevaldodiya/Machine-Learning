import os
import Preprocess as preproc
from collections import Counter

spamTrainPath = ".\\train\\spam\\"
hamTrainPath = ".\\train\\ham\\"
spamFilesList = [(spamTrainPath + fname) for fname in os.listdir(spamTrainPath)]
hamFilesList = [(hamTrainPath + fname) for fname in os.listdir(hamTrainPath)]

vocab = {}
spamDict = {}
hamDict = {}

totalWordsCountSpam = 0
totalWordsCountHam = 0
totalWordsCount = 0

#spamProb = len(spamFilesList)/len(spamFilesList + hamFilesList)
#hamProb = len(hamFilesList)/len(spamFilesList + hamFilesList)

def createVocab(filesList):
	#spamDict = preproc.createDictionaryFromWords(preproc.preprocessFiles(spamFilesList))
	#hamDict = preproc.createDictionaryFromWords(preproc.preprocessFiles(hamFilesList))
	vocab = preproc.createDictionaryFromWords(preproc.preprocessFiles(filesList))
	preproc.saveDictionaryToCSV(vocab, ".\\dictionary\\vocab.csv")
	return vocab

def createDictionary(spamFilesList, isSpam):
	Dict = preproc.createDictionaryFromWords(preproc.preprocessFiles(spamFilesList))
	if isSpam == True:
		preproc.saveDictionaryToCSV(Dict, ".\\dictionary\\spam.csv")
	else:
		preproc.saveDictionaryToCSV(Dict, ".\\dictionary\\ham.csv")
	return Dict

def updateDictionary(spamFilesList, isSpam):
	Dict1 = preproc.createDictionaryFromWords(preproc.preprocessFiles(spamFilesList))
	Dict2 = {}
	if isSpam == True:
		Dict2 = preproc.readDictionaryFromCSV(".\\dictionary\\spam.csv", "int")
		Dict = Counter(Dict1) + Counter(Dict2)
		Dict = dict(Dict.most_common(5000))
		preproc.saveDictionaryToCSV(Dict, ".\\dictionary\\spam.csv")
	else:
		Dict2 = preproc.readDictionaryFromCSV(".\\dictionary\\ham.csv", "int")
		Dict = Counter(Dict1) + Counter(Dict2)
		Dict = dict(Dict.most_common(5000))
		preproc.saveDictionaryToCSV(Dict, ".\\dictionary\\ham.csv")

def updateVocab():
	Dict1 = preproc.readDictionaryFromCSV(".\\dictionary\\spam.csv", "int")
	Dict2 = preproc.readDictionaryFromCSV(".\\dictionary\\ham.csv", "int")
	Dict = dict(Counter(Dict1) + Counter(Dict2))
	preproc.saveDictionaryToCSV(Dict, ".\\dictionary\\vocab.csv")

"""
def trimDictionaries():
	spamDict = preproc.readDictionaryFromCSV(".\\dictionary\\spam.csv", "int")
	hamDict = preproc.readDictionaryFromCSV(".\\dictionary\\ham.csv", "int")
	spamDict = Counter(spamDict)
	hamDict = Counter(hamDict)
	spamDict = dict(spamDict.most_common(5000))
	hamDict = dict(hamDict.most_common(5000))
	preproc.saveDictionaryToCSV(spamDict, ".\\dictionary\\spam.csv")
	preproc.saveDictionaryToCSV(hamDict, ".\\dictionary\\ham.csv")
"""


# Basic Learning
"""
print("Training...")

vocab = createVocab(spamFilesList + hamFilesList)
print("50% Done!")
print("Training...")
spamDict = createDictionary(spamFilesList, True)
print("Training...")
hamDict = createDictionary(hamFilesList, False)

print("Training Complete!")
"""
# Progressive Learning
updateDictionary(spamFilesList, True)
updateDictionary(hamFilesList, False)
#trimDictionaries()
updateVocab()
"""
preproc.saveDictionaryToCSV(preproc.createDictionaryFromWords(preproc.preprocessFile(spamFilesList[0])), "test.csv")
preproc.readDictionaryFromCSV("test.csv", "int")

preproc.saveDictionaryToCSV(preproc.createDictionaryFromWords(preproc.preprocessFiles(spamFilesList + hamFilesList)), "test_combined.csv")
preproc.readDictionaryFromCSV("test_combined.csv", "int")
"""

