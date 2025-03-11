M = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

soma_linha_3 = sum(M[2])
soma_coluna_2 = sum(M[i][1] for i in range(5))
soma_diagonal_principal = sum(M[i][i] for i in range(5))
soma_diagonal_secundaria = sum(M[i][4-i] for i in range(5))
soma_total = sum(sum(linha) for linha in M)

print(soma_linha_3)
print(soma_coluna_2)
print(soma_diagonal_principal)
print(soma_diagonal_secundaria)
print(soma_total)
