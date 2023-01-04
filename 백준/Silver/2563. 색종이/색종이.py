N = int(input())
array = [[0]*100 for _ in range(100)]

for i in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            array[i][j] = 1
            
area = 0
for i in array:
    area += i.count(1)
print(area)