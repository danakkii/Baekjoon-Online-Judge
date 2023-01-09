import sys

n = int(input())
arr = [int(sys.stdin.readline()) for i in range(n)]
arr.sort()
print(*arr, sep='\n') 