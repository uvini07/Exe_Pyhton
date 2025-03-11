matriz1 = []
matriz2 = []

for i in range(2):
    linha1 = []
    linha2 = []
    for j in range(2):
        linha1.append(int(input(f"Digite o elemento da matriz 1 na posição [{i+1},{j+1}]: ")))
        linha2.append(int(input(f"Digite o elemento da matriz 2 na posição [{i+1},{j+1}]: ")))
    matriz1.append(linha1)
    matriz2.append(linha2)

matriz_resultante = [[matriz1[i][j] + matriz2[i][j] for j in range(2)] for i in range(2)]

print("\nMatriz resultante da soma:")
for linha in matriz_resultante:
    print(linha)
