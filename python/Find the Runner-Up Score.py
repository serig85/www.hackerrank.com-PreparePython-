if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sp=list(arr)
    sp.sort()
    l=len(sp)
    n=sp[l-1]
    x=2
    while n==sp[l-x]:
        x+=1
    print(sp[l-x])