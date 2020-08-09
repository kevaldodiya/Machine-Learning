import csv
import matplotlib.pyplot as plt
import numpy as np
import math

dataFile = "Dataset1.csv"

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

plt.scatter([data[i][0] for i in range(len(data))], [data[i][1] for i in range(len(data))])
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Dataset")
plt.show()

tmp_data = np.array(data)
plt.hist(tmp_data[:,0], 60)
plt.xlabel("X-coordinate")
plt.ylabel("Frequnecy")
plt.title("Frequency vs X-coordinate")
plt.show()
plt.hist(tmp_data[:,1], 60)
plt.xlabel("Y-coordinate")
plt.ylabel("Frequency")
plt.title("Frequency vs Y-coordinate")
plt.show()

def calculateMu(data):
	return sum(data)/len(data)

def calculateSigma(data, mu):
	n = len(data)
	res = 0.0;
	for i in data:
		res = res + (1.0/n)*(i - mu)*(i - mu)
	res = math.sqrt(res)
	return res

x_mu = calculateMu([data[i][0] for i in range(len(data))])
y_mu = calculateMu([data[i][1] for i in range(len(data))])
x_sigma = calculateSigma([data[i][0] for i in range(len(data))], x_mu)
y_sigma = calculateSigma([data[i][1] for i in range(len(data))], y_mu)

#print(str(x_mu) + " " + str(x_sigma))
#print(str(y_mu) + " " + str(y_sigma))

def calculateLL(data, mu, sigma):
	n = len(data)
	res = -((n/2.0)*math.log(2*math.pi)) - (n*math.log(sigma))
	for i in data:
		res = res - ((1.0/(2*sigma*sigma))*((i - mu)*(i - mu)))
	#print("res: " + str(res))
	return res

def plotLLvsmu(data, mu, sigma, coor):
	LL = np.array([calculateLL(data, m, sigma) for m in mu])
	plt.plot(mu, LL)
	plt.xlabel("Mu values")
	plt.ylabel("Log-Likelyhood")
	if(coor == 0):
		plt.title("Log-Likelyhood vs. Mu values (For x-coordinate)")
	else:
		plt.title("Log-Likelyhood vs. Mu values (For y-coordinate)")
	plt.show()

print("Log Likelyhood for maximum estimator for \'x\' with Mu : " + str(x_mu) + ", and Sigma : " + str(x_sigma) + " is :" + str(calculateLL([data[i][0] for i in range(len(data))], x_mu, x_sigma)))
print("Log Likelyhood for maximum estimator for \'y\' with Mu : " + str(y_mu) + ", and Sigma : " + str(y_sigma) + " is :" + str(calculateLL([data[i][1] for i in range(len(data))], y_mu, y_sigma)))

mu_range = np.array([i for i in range(-10, 11)])
plotLLvsmu([data[i][0] for i in range(len(data))], mu_range, 1, 0)
plotLLvsmu([data[i][1] for i in range(len(data))], mu_range, 1, 1)