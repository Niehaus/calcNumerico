import numpy as np
import triangular
import substituicao

arq = open('matriz.dat', 'r')
n = int(arq.readline().rstrip())

A = np.zeros((n,n), dtype='float')
b = np.zeros(n, dtype='float')

for i in range(n):
  linha = arq.readline().rstrip().split()
  for j in range(n):
    A[i][j] = linha[j]


linha = arq.readline().rstrip().split()
for j in range(n):
  b[j] = linha[j]

b, A = triangular.Superior(A, b)

x = substituicao.retrosub(b, A)

print ('\nO resultado eh')
print ('x1 =', x[0])
print ('x2 =', x[1])
print ('x3 =', x[2])
print(x)
