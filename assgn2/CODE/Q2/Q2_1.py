import csv
import matplotlib.pyplot as plt
import numpy as np
import math

dataFile = "Dataset_train.csv"

data = []

x = []
y = []

with open(dataFile, 'r') as csvFile:
	csvreader = csv.reader(csvFile)

	for rows in csvreader:
		row = []
		for field in rows:
			row.append(float(field))
		data.append(row)

data = np.array(data)
#print(data)
X = np.ones(data.shape, dtype=float)
X[:,1:101] = data[:,0:100]
Y = data[:,100:101]
print("X: ")
print(X)
print("Y: ")
print(Y)

def linear_regression(X, Y):
	return np.matmul(np.linalg.inv(np.matmul(np.transpose(X), X)),np.matmul(np.transpose(X), Y))

W = linear_regression(X, Y)
print("W: ")
print(W.T)