croatia = ['c=', 'c-','dz=','d-','lj','nj','s=','z=']
alpha = input()
for i in croatia:
    alpha = alpha.replace(i, '*')
print(len(alpha))