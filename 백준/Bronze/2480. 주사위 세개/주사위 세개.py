import sys

a, b, c = map(int, sys.stdin.readline().split())


if a == b == c:
    print(10000+(a*1000))
elif a == b:
    print(1000+(a*100))
elif a == c:
    print(1000+(a*100))
elif c == b:
    print(1000+(c*100))
else:
    print(max(a, b, c)*100)
    