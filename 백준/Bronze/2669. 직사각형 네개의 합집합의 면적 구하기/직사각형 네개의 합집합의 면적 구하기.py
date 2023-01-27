array = [[0]*100 for _ in range(100)] #좌표평면

for i in range(4):
    x1, y1, x2, y2 = list(map(int, input().split()))

    for i in range(x1, x2):
        for j in range(y1, y2):
            array[i][j] = 1

area = 0
for i in array:
    area += i.count(1)
print(area)