matrix1, matrix2 = [], []

N, M = map(int, input().split())

for i in range(N):
    i = list(map(int, input().split()))
    matrix1.append(i)

for j in range(N):
    j = list(map(int, input().split()))
    matrix2.append(j)
    
for i in range(N):
    for j in range(M):
        print(matrix1[i][j] + matrix2[i][j], end=' ')
    print()