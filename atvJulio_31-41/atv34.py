D = [list(map(int, input(f"Digite os elementos da linha {i+1}: ").split())) for i in range(5)]

X = int(input("Digite o número X para verificar se existe na matriz: "))


existe = False
for i in range(5):
    if X in D[i]:
        existe = True
        break

if existe:
    print(f"O valor {X} existe na matriz.")
else:
    print(f"O valor {X} NÃO existe na matriz.")
