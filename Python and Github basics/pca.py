#Principal Component Analysis
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

np_array = np.loadtxt(sys.argv[1], delimiter = ',')

df = pd.DataFrame(np_array)
standard = (df-df.mean())/(df.std())
covariance = np.cov(standard.T, bias = 0)

eigenvalues, eigenvectors = np.linalg.eig(covariance)
dimensions = 2
top_eigenvectors = eigenvectors[:,:dimensions]
final_data = np.matmul(np.array(standard),top_eigenvectors)

plt.scatter(final_data[:,0]*10,final_data[:,1]*10)
plt.yticks(np.arange(-15,15.01,2))
plt.xticks(np.arange(-15,15.01,2))
plt.xlim(-15,15)
plt.savefig("out.png")
