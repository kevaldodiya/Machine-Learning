import csv
import matplotlib.pyplot as plt
import numpy as np
import math
from math import *

def normal_pdf(x, mu, sigma):
    return 1.0 / (sigma * (2.0 * pi)**(1/2)) * exp(-1.0 * (x - mu)**2 / (2.0 * (sigma**2)))

dataFile = "Dataset2.csv"

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
np.array([i for i in range(-7, 8)])
plt.hist(data, 60)
plt.xlabel("Data Values")
plt.ylabel("Frequency")
plt.title("Dataset")
plt.show()

def assignCluster(probs):
	maxProb = probs[0]
	ind = 0
	for i in range(probs.shape[0]):
		if(maxProb < probs[i]):
			maxProb = probs[i]
			ind = i
	return ind

def findMu(data):
	if(data.shape[0] == 0):
		return 0
	else:
		n = data.shape[0]
		Sum = 0
		for d in data:
			Sum += d
		if(Sum == 0):
			return 0.001
		return Sum/n

def findSigma(data, mu):
	if(data.shape[0] == 0):
		return 0.001
	else:
		n = data.shape[0]
		Sum = 0
		for d in data:
			Sum += ((d - mu)**2)
		if(Sum == 0):
			return 0.001
		#print(Sum)
		return sqrt(Sum/n)

def findClusters(data, k):
	means = np.random.rand(k, 1)*10 - 5
	sigmas = np.random.rand(k, 1)
	old_means = np.zeros((k, 1), dtype = float)
	old_sigmas = np.zeros((k, 1), dtype = float)
	cluster_fracs = np.ones((k, 1), dtype = float) * (1.0/k)
	mean_diff = 1.0
	sigma_diff = 1.0

	log_likelyhood = 0.0

	probs = np.zeros((data.shape[0], k), dtype=float)
	clusters = np.zeros((data.shape), dtype=int)
	
	#print("Initial Means: " + str(means))
	#print("Initial Variances: " + str(sigmas))

	while(abs(mean_diff) > 0.001 or abs(sigma_diff) > 0.001):
		for j in range(k):
			old_means[j] = means[j]
			old_sigmas[j] = sigmas[j]
		for i in range(data.shape[0]):
			for j in range(k):
				probs[i,j] = normal_pdf(data[i], means[j], sigmas[j])
		#print(probs)
		for i in range(data.shape[0]):
			for j in range(k):
				probs[i,j] = probs[i,j]/np.sum(probs[i])
		#print(probs)
		for i in range(k):
			cluster_fracs[i] = 0
		for i in range(data.shape[0]):
			clusters[i] = assignCluster(probs[i])
			cluster_fracs[clusters[i]] += (1/data.shape[0])
		#print(np.transpose(clusters))
		for j in range(k):
			c_wise_data = []
			for i in range(clusters.shape[0]):
				if(clusters[i] == j):
					c_wise_data.append(data[i])
			means[j] = findMu(np.array(c_wise_data))
			sigmas[j] = findSigma(np.array(c_wise_data), means[j])
		mean_diff = sum(abs(means - old_means))
		sigma_diff = sum(abs(sigmas - old_sigmas))
	print("Number of Clusters: " + str(k))
	print("Means: ")
	print(means)
	print("Standard Deviations: ")
	print(sigmas)
	print("Cluster Wise Fractions: ")
	print(cluster_fracs)

	for i in range(data.shape[0]):
		LLtmp = 0
		for j in range(k):
			normal = normal_pdf(data[i], means[j], sigmas[j])
			LLtmp += (normal * cluster_fracs[j])
		if(LLtmp == 0):
			LLtmp = 0.001
		log_likelyhood += (math.log(LLtmp))

	return log_likelyhood

LL = np.zeros((10, 1), dtype = float)
for i in range(10):
	LL[i] = findClusters(data, i + 1)

print("Log-Likelyhood Value for different number of Clusters: ")
for i in range(10):
	print(str(i + 1) + '\t' + str(LL[i]))
plt.plot([i for i in range(1, 11)], LL)
plt.title("Number of Clusters vs. Log-Likelyhood")
plt.xlabel("Number of Clusters")
plt.ylabel("Log-Likelyhood")
axs = plt.gca()
axs.set_xlim([0, 11])
plt.show()