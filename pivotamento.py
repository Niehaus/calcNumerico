import numpy as np

def pivo(k, b, A):

  print ('Entrou: pivotando a linha', k)
  print (A)
  n = len(b)
  jmax = k
  for j in range(k+1, n, 1):
    if ( np.abs(A[j][k]) > np.abs(A[jmax][k]) ):
      jmax = j

  TempA       = np.zeros_like(b)
  TempA[:]    = A[k][:]
  A[k][:]     = A[jmax][:]
  A[jmax][:]  = TempA[:]

  TempB  = b[k]
  b[k]   = b[jmax]
  b[jmax] = TempB

  print ('linha', k, 'trocou com', jmax)
  print (A, '\n')

  return A, b
