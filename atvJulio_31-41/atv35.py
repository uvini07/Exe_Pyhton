G = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

SL = [sum(linha) for linha in G]
SC = [sum(G[i][j] for i in range(5)) for j in range(5)]

print("SL:", SL)
print("SC:", SC)
