import numpy as np

def decorate_matrix(n):
	out = np.zeros(n*n).reshape(n,n)
	out[0,:] = out[n-1,:] = out[:,0] = out[:,n-1] = 1
	return out

print(decorate_matrix(5))