def merge_the_tools(string, k):
    # your code goes here
    mn=set()
    ss=""
    sln=len(string)
    for i in range(0,sln):
        if (i//k)==(i/k) and i>0:
            print(ss)
            mn.clear()
            ss=""
        if string[i] not in mn:
            ss=ss+string[i]
            mn.add(string[i])
            #print(mn)
    print(ss)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)