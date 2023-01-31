def math(A,B): 
    AB= (A+B)*(A-B)
    return AB
A,B = map(int, input().split())
print(math(A, B))