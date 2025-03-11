matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f"Digite o elemento da posição [{i+1},{j+1}]: ")))
    matriz.append(linha)

for linha in matriz:
    print(linha)
