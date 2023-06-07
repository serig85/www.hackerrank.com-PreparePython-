import itertools
a=(input().split())
for i in range(len(a)):
    a[i]=int(a[i])
b=input().split()
for i in range(len(b)):
    b[i]=int(b[i])
ob=itertools.product(a,b)
ob=list(ob)
for i in range(len(ob)):
    print(ob[i],end=" ")