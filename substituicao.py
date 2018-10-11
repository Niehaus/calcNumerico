import numpy as np

def retrosub(b, A):
  n = len(b)
  x = np.zeros_like(b)
  x[n-1] = b[n-1] / A[n-1][n-1]

  for i in range(n-2, -1, -1):
    soma = b[i]
    for j in range(i+1, n, 1):
      soma = soma - A[i][j]*x[j]
    x[i] = soma / A[i][i]

  return x
