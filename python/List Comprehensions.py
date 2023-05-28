if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    i=x
    j=y
    k=z
    matrix = [[x,y,z] for x in range(i+1) for y in range(j+1) for z in range(k+1) if x+y+z !=n ]
    print(matrix)
    