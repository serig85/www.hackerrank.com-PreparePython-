def print_formatted(number):
    # your code goes here
    n=int(number)
    l=[oct,hex,bin]
    w=len(str((bin(n))[2:]))
    for i in range(n):
        print(str(i+1).rjust(w,' '),end="")
        for j in l:
            print (str((j(i+1))[2:]).upper().rjust(w+1,' '),end="")
        print()

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)