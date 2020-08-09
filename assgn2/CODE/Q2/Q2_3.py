import csv
import matplotlib.pyplot as plt
import numpy as np
import math
import random

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

W_ML = linear_regression(X, Y)

#W_t = np.random.rand(W_ML.shape[0], W_ML.shape[1])

def diff_in_w(W_M, W):
	return math.sqrt(np.sum((W_M - W) ** 2))

def calculate_cost(X, W, y, n):
	return (1.0/(2*n)) * np.sum((np.matmul(X, W) - y) ** 2)

def stochastic_gradient_desent(X, Y, alpha, iters, batch_size):
	n = X.shape[0]
	number_of_batches = n/batch_size
	X_batch = np.zeros([batch_size, X.shape[1]], dtype=float)
	Y_batch = np.zeros([batch_size, 1], dtype=float)
	W = np.random.rand(X.shape[1], 1)
	#print(W.T)
	W_tt = np.zeros((X.shape[1], iters))
	for it in range(iters):
		for i in range(batch_size):
			ind = random.randint(0, n - 1)
			X_batch[i,:] = X[ind,:]
			Y_batch[i] = Y[ind]
		pred = np.matmul(X_batch, W)
		#print(W.T)
		W = W - (1/n) * alpha * (np.matmul(X_batch.T, (pred - Y_batch)))
		#print(W.T)
		W_tt[:,[it]] = W

	return W, W_tt

#print("W: ")
#print(W.T)
print(W_ML.T)
W_t, W_tt = stochastic_gradient_desent(X, Y, 0.001, 10000, 100)
print(W_t.T)
Errors = np.zeros((W_tt.shape[1], 1))
for i in range(W_tt.shape[1]):
	Errors[i] = diff_in_w(W_ML.flatten(), W_tt[:,i].flatten())

print(calculate_cost(X, W_ML, Y, Y.shape[0]))
print(calculate_cost(X, W_t, Y, Y.shape[0]))

plt.plot([i for i in range(10000)], Errors)
plt.xlabel("Time t")
plt.ylabel("Norm of W_t - W_ML")
plt.title("Norm of W_t - W_ML vs. Time t")
plt.show()