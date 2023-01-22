import sys
from collections import deque
deque = deque()
N = int(input())

for i in range(N):
    line = sys.stdin.readline().rstrip().split()
    if(line[0] == "push_front"):
        deque.appendleft(int(line[1]))
    elif (line[0] == "push_back"):
        deque.append(int(line[1]))
    elif (line[0] == "pop_front"):
        if(len(deque) <= 0):
            print(-1)
        else:
            print(deque.popleft())
    elif (line[0] == "pop_back"):
        if (len(deque) <= 0):
            print(-1)
        else:
            print(deque.pop())
    elif (line[0] == "size"):
        print(len(deque))
    elif (line[0] == "empty"):
        if (len(deque) <= 0):
            print(1)
        else:
            print(0)
    elif (line[0] == "front"):
        if (len(deque) <= 0):
            print(-1)
        else:
            print(deque[0])
    elif (line[0] == "back"):
        if (len(deque) <= 0):
            print(-1)
        else:
            print(deque[len(deque) - 1])