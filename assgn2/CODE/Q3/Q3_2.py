import csv
import matplotlib.pyplot as plt
import numpy as np
import math

def loadData(file_name):
	dataFile = file_name

	data = []

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
	return X, Y

X, Y = loadData("Dataset_train.csv")

train_valid_ratio = 0.8
X_train = X[:int(round(train_valid_ratio * X.shape[0])),:]
X_valid = X[int(round(train_valid_ratio * X.shape[0])):,:]
Y_train = Y[:int(round(train_valid_ratio * Y.shape[0])),:]
Y_valid = Y[int(round(train_valid_ratio * Y.shape[0])):,:]

X_test, Y_test = loadData("Dataset_test.csv")

print("X: ")
print(X)
print("Y: ")
print(Y)
print(X_train.shape)
print(X_valid.shape)
print(Y_train.shape)
print(Y_valid.shape)

def linear_regression(X, Y):
	return np.matmul(np.linalg.inv(np.matmul(np.transpose(X), X)),np.matmul(np.transpose(X), Y))

W_ML = linear_regression(X_train, Y_train)

#W_t = np.random.rand(W_ML.shape[0], W_ML.shape[1])

def diff_in_w(W_M, W):
	return math.sqrt(np.sum((W_M - W) ** 2))

def calculate_cost(X, W, y, n):
	return (1.0/(2*n)) * np.sum((np.matmul(X, W) - y) ** 2)

def ridge_gradient_desent(X, Y, alpha, iters, lam=0.5):
	n = X.shape[0]
	W = np.random.rand(X.shape[1], 1)
	#print(W.T)
	for it in range(iters):
		pred = np.matmul(X, W)
		#print(W.T)
		W = W - alpha * (((1/n) * np.matmul(X.T, (pred - Y))) + 2 * lam * W)
		#print(W.T)

	return W


W_t = ridge_gradient_desent(X_train, Y_train, 0.0001, 10000, 1/10)
print(W_t.T)
print(calculate_cost(X_train, W_t, Y_train, Y_train.shape[0]))

print(W_ML.T)

lambda_max = 2

Errors = np.zeros([int(lambda_max * 10), 1])
for i in range(1, int(lambda_max * 10) + 1):
	W_t = ridge_gradient_desent(X_train, Y_train, 0.0001, 10000, i/10)
	if(i == 1):
		W_min = W_t
		min_cost = calculate_cost(X_valid, W_t, Y_valid, Y_valid.shape[0])
		Errors[i - 1] = min_cost
	else:
		tmp_cost = calculate_cost(X_valid, W_t, Y_valid, Y_valid.shape[0])
		Errors[i - 1] = tmp_cost
		if(tmp_cost < min_cost):
			min_cost = tmp_cost
			W_min = W_t

print("Errors: ")
print(Errors)

print("Cost with Maximum Likelyhood Estimator: ")
print(calculate_cost(X_test, W_ML, Y_test, Y_test.shape[0]))
print("Cost with Ridge Regression: ")
print(calculate_cost(X_test, W_min, Y_test, Y_test.shape[0]))
print("Difference in W_ML and best W_ridge: ")
print(diff_in_w(W_ML.flatten(), W_min.flatten()))

plt.plot([i/10 for i in range(1, int(lambda_max * 10) + 1)], Errors)
plt.xlabel("lambda (W_ridge)")
plt.ylabel("Error")
plt.title("lambda (W_ridge) vs. Error")
plt.show()