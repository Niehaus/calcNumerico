import numpy as np

arq = open('matriz.dat', 'r')
n = int(arq.readline().rstrip())
m = int(arq.readline().rstrip())

## b = vetor y do teste (da base de dados)
## A = matriz G
## y = vetor y-chapeu do treino
A = np.zeros((n,m), dtype='float')
b = np.zeros(n, dtype='float')

for i in range(n):
  linha = arq.readline().rstrip().split()
  for j in range(m):
    A[i][j] = linha[j]

linha = arq.readline().rstrip().split()
for j in range(n):
  b[j] = linha[j]

print("G = \n",A)
print("y = \n", b)

print("\nGTG x = GTy\n")
#Gera matriz transposta
GT = A.transpose()
GTG = np.dot(GT,A)
GTy = np.dot(GT,b)
print("GT =\n",GT)
print("\n")
print("GTG = \n", GTG)
print("\n")
print("GTy =\n",GTy)

#Solução sistema linear
alpha = np.linalg.solve(GTG,GTy)
#print ('\nAlpha por eliiminação de Gauss', alpha)
#Polinomio gerado
print(f'\nPolinomio: P(x) = {round(alpha[0],2)} + {round(alpha[1],2)}x1 + {round(alpha[2],2)}x2\n')
for i in range(n):
    resultado = round(alpha[0],2) + round(alpha[1],2)*A[i][1] + round(alpha[2],2)*A[i][2]
    print(f'P(x) = {round(alpha[0],2)} + {round(alpha[1],2)}x{A[i][1]} + {round(alpha[2],2)}x{A[i][2]}')
    print(f'P(x) =  {round(alpha[0],2)} + {round(alpha[1],2)*A[i][1]} + {round(alpha[2],2)*(A[i][2])} = {resultado}')
    print(f'Diferença = {np.sqrt(((resultado - b[i]) ** 2).mean())}\n')
