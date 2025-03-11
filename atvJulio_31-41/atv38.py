
G = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]


print("Gabarito:")
for num in G:
    if num == 1:
        print("Coluna 1")
    elif num == 2:
        print("Coluna do Meio")
    elif num == 3:
        print("Coluna 2")


apostas = [
    [1, 0, 0], 
    [0, 1, 0], 
    [0, 0, 1],
    [1, 0, 0],
    [0, 1, 0], 
    [0, 0, 1],
    [1, 0, 0],
    [0, 1, 0], 
    [0, 0, 1],
    [1, 0, 0],
    [0, 1, 0], 
    [0, 0, 1], 
    [1, 0, 0]  
]


total_apostas_coluna_1 = 0
total_apostas_coluna_meio = 0
total_apostas_coluna_2 = 0

for i in range(13):
    if apostas[i][0] == 1:
        total_apostas_coluna_1 += 1
    if apostas[i][1] == 1:  
        total_apostas_coluna_meio += 1
    if apostas[i][2] == 1:
        total_apostas_coluna_2 += 1

# Exibir o resultado
print("\nTotal de apostas por coluna:")
print(f"Coluna 1: {total_apostas_coluna_1}")
print(f"Coluna do Meio: {total_apostas_coluna_meio}")
print(f"Coluna 2: {total_apostas_coluna_2}")
