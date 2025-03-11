A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

soma_diagonal_principal = 0
soma_diagonal_secundaria = 0

for i in range(4):
    soma_diagonal_principal += A[i][i]
    soma_diagonal_secundaria += A[i][3 - i]

soma_total = soma_diagonal_principal + soma_diagonal_secundaria

print("Soma da Diagonal Principal:", soma_diagonal_principal)
print("Soma da Diagonal Secundária:", soma_diagonal_secundaria)
print("Soma total dos elementos marcados com X:", soma_total)
