import numpy as np
import triangular
import substituicao
import gaussSeidel
import time

arq = open('matriz.dat', 'r')
n = int(arq.readline().rstrip())

A = np.zeros((n,n), dtype='float')
b = np.zeros(n, dtype='float')
#print("dimensao = ",n)
for i in range(n):
  linha = arq.readline().rstrip().split()
  for j in range(n):
    A[i][j] = linha[j]


linha = arq.readline().rstrip().split()
for j in range(n):
  b[j] = linha[j]

# ELEMINAÇÃO DE GAUSS
gauss_tempo_inicio = time.time()
b, A = triangular.Superior(A, b)
x = substituicao.retrosub(b, A)
gauss_tempo_final = time.time()

print ('\nResultado para Eliminação de Gauss:', x)


chute_inicial = [0,0,0,0]
iteracoes = 4
# GAUSS SEIDEL
print ('\nResultado para Gauss-Seidel:')
gauss_seidel_tempo_inicio = time.time()
gaussSeidel.gauss_seidel(A,b,n,chute_inicial,iteracoes)
gauss_seidel_tempo_final = time.time()
print("\n")
print("Tempo gasto para Gauss = ", gauss_tempo_final - gauss_tempo_inicio)
print("Tempo gasto para Gauss Seidel = ", gauss_seidel_tempo_final - gauss_seidel_tempo_inicio)
