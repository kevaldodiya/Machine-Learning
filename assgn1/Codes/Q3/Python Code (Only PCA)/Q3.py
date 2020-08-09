import csv
import matplotlib.pyplot as plt
import numpy as np
import math

dataFile = "Dataset3.csv"

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
n = data.shape[0]
print("Data: ")
print(data)
plt.scatter(data[:,0], data[:,1])
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Original Data")
plt.show()

def sortInd(eigs, eigVs):
	for i in range(eigs.shape[0]):
		for j in range(i + 1, eigs.shape[0]):
			if(eigs[i] < eigs[j]):
				eigs[i],eigs[j] = eigs[j],eigs[i]
				eigVs[:,[i,j]] = eigVs[:,[j,i]]

def plotEigs(eigs):
	res = np.zeros(eigs.shape)
	res[0] = eigs[0]
	s = np.sum(eigs)
	ind = 0
	indf = 0
	for i in range(1, eigs.shape[0]):
		res[i] = res[i-1] + eigs[i]
		if(indf == 0 and (res[i]/s) >= 0.85):
			ind = i
			indf = 1
	plt.plot(100*eigs/s, label="individual contribution")
	plt.plot(100*res/s, label="commulative contribution")
	plt.xlabel("i-th Eigen Value after sorting")
	plt.ylabel("% Contribution")
	plt.legend("commulative contribution")
	plt.title("Contribution vs. i-th Eigen Value")
	plt.show()
	return ind


#print(np.matmul(data, np.transpose(data)))
#A = np.array([[1, 0], [0, 1]])
#a = np.mean(A, axis=0, dtype=np.float64)
#print(A)
#print(a)
#print(A-a)
#c = np.matmul(np.transpose(A-a), A-a)
#print(c)
#e, ev = np.linalg.eigh(c)
#ev[:,[0,1]] = ev[:,[1,0]]
#l = np.array([0, 1, 2, 3, 4, 5])
#ll = np.array([[0, 1, 2, 3, 4, 5], [5, 4, 3, 2, 1, 0], [0, 0, 0, 0, 0, 0]])
#sortInd(l, ll)
#print(l)
#print(ll)
#print(plotEigs(l))

d = np.mean(data, axis=0, dtype=np.float64)
cov = (np.matmul(np.transpose(data-d), data-d))/n
#print(cov)
eig, eigV = np.linalg.eigh(cov)
sortInd(eig, eigV)
print("Eigenvalues: ")
print(str(eig))
print("Eigenvectors: ")
print(str(eigV))
k = plotEigs(eig)
data_transformed = np.transpose(np.matmul(np.transpose(eigV[:,0:k+1]), np.transpose(data)))
print("Data After PCA:")
print(data_transformed)
plt.scatter(data_transformed[:,0], data_transformed[:,1])
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Data After applying PCA")
plt.show()