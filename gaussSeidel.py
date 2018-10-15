def gauss_seidel(matriz, vetor_b, dimensao, chute_inicial, iteracoes):
    x_anterior = [0.0 for i in range(dimensao)]
    for i in range(iteracoes):
        for j in range(dimensao):
            x_anterior[j] = chute_inicial[j]
        for j in range(dimensao):
            soma = 0.0
            for k in range(dimensao):
                if k != j:
                    soma += matriz[j][k] * chute_inicial[k]
            chute_inicial[j] = (vetor_b[j] - soma) / matriz[j][j]
        dif_norma = 0.0
        norma_anterior = 0.0
        for j in range(dimensao):
            dif_norma = dif_norma + abs(chute_inicial[j] - x_anterior[j])
            norma_anterior = norma_anterior + abs(x_anterior[j])
        if norma_anterior == 0.0:
            norma_anterior = 1.0
        norma = dif_norma / norma_anterior
        if (norma < iteracoes) and i != 0:
            print("A sequência converge para [", end="")
            for j in range(dimensao - 1):
                print(chute_inicial[j], ",", end="")
            print(f'{chute_inicial[dimensao - 1]}] e gastou {i+1} iterações')
            #print(norma)
            return

    print("A matriz não converge.")
