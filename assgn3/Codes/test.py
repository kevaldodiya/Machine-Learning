import os
import Preprocess as preproc
import math

vocab = {}
spamDict = {}
hamDict = {}

totalWordsCountSpam = 0
totalWordsCountHam = 0
totalWordsCount = 0

spamProb = math.log(0.5)
hamProb = math.log(0.5)
print(spamProb)
print(hamProb)

vocab = preproc.readDictionaryFromCSV(".\\dictionary\\vocab.csv")
spamDict = preproc.readDictionaryFromCSV(".\\dictionary\\spam.csv")
hamDict = preproc.readDictionaryFromCSV(".\\dictionary\\ham.csv")

totalWordsCount = len(vocab)
totalWordsCountSpam = len(spamDict)
totalWordsCountHam = len(hamDict)

print(totalWordsCount)
print(totalWordsCountSpam)
print(totalWordsCountHam)

def predict(filename):
	testDict = preproc.createDictionaryFromWords(preproc.preprocessFile(filename))

	testSpamProb = spamProb
	testHamProb = hamProb

	for word in testDict.keys():
		if word in spamDict.keys():
			wordSpamProb = (spamDict[word] + 1.0) / (totalWordsCountSpam + totalWordsCount)
		else:
			wordSpamProb = (0.0 + 1.0) / (totalWordsCountSpam + totalWordsCount)
		testSpamProb += math.log(wordSpamProb)
	
		if word in hamDict.keys():
			wordHamProb = (hamDict[word] + 1.0) / (totalWordsCountHam + totalWordsCount)
		else:
			wordHamProb = (0.0 + 1.0) / (totalWordsCountHam + totalWordsCount)
		testHamProb += math.log(wordHamProb)

	#print(testSpamProb)
	#print(testHamProb)

	#print(testSpamProb / (testSpamProb + testHamProb))
	#print(testHamProb / (testSpamProb + testHamProb))
	if(testSpamProb > testHamProb):
		print("Spam!")
		return 1
	else:
		print("Ham!")
		return 0


spamTestPath = ".\\test\\spam\\"
hamTestPath = ".\\test\\ham\\"
spamFilesList = [(spamTestPath + fname) for fname in os.listdir(spamTestPath)]
hamFilesList = [(hamTestPath + fname) for fname in os.listdir(hamTestPath)]
spamAccu = 0
hamAccu = 0
print("Spam Test Predictions")
for file in spamFilesList:
	if(predict(file) == 1):
		spamAccu += (1/len(spamFilesList))
print("Ham Test Predictions")
for file in hamFilesList:
	if(predict(file) == 0):
		hamAccu += (1/len(hamFilesList))

spamAccu *= 100
hamAccu *= 100
print("Spam Test Accuracy:")
print(spamAccu)
print("Ham Test Accuracy:")
print(hamAccu)

print("Prediction on example Email 1: ")
predict(".\\test\\email1.txt")

print("Prediction on example Email 2: ")
predict(".\\test\\email2.txt")