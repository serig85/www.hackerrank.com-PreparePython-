if __name__ == '__main__':
    N = int(input())
    l=[]
    for i in range(N):
        oper=str(input())
        opers=oper.split()
        if opers[0]=="insert":
            opers[1]=int(opers[1])
            opers[2]=int(opers[2])
            l.insert(opers[1],opers[2])
        elif opers[0]=="print":
            print(l)
        elif opers[0]=="remove":
            opers[1]=int(opers[1])
            l.remove(opers[1])
        elif opers[0]=="append":
            opers[1]=int(opers[1])
            l.append(opers[1])
        elif opers[0]=="sort":
            l.sort()
            #print("otl",l)
        elif opers[0]=="pop":
            l.pop()
        elif opers[0]=="reverse":
            l.reverse()
