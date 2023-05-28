if __name__ == '__main__':
    tabl=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        tabl.append([score,name])
    tabl.sort()
    x=tabl[0][0]
    rez=[tabl[0][0]]
    rc=0
    for i in range(_+1):
       if tabl[i][0] !=x:
        x=tabl[i][0]
        rez.append(tabl[i][0])
        rc+=1
        #print(rc)
       if rc==1:
        print(tabl[i][1])
    #print(rez)

   
