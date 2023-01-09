import sys

n = int(input())
arr = []
for _ in range(n) : 
    input = int(sys.stdin.readline())
    arr.append(input)
arr.sort()

print(*arr, sep='\n')