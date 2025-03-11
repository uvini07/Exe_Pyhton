A = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24]
]

B = [
    [24, 23, 22, 21, 20, 19],
    [18, 17, 16, 15, 14, 13],
    [12, 11, 10, 9, 8, 7],
    [6, 5, 4, 3, 2, 1]
]

S = [[A[i][j] + B[i][j] for j in range(6)] for i in range(4)]
D = [[A[i][j] - B[i][j] for j in range(6)] for i in range(4)]

for linha in S:
    print(*linha)

for linha in D:
    print(*linha)
