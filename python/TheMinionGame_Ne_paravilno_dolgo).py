def minion_game(string):
    # your code goes here
    ss=set()
    sk=set()
    ck=0
    Vowels="AEIOU"
    st=""
    lns=len(string)
    for i in range(0,lns):
        #print(i)
        for j in range(i,lns):
            st=st+string[j]
            #print(st,end=" ")
            if string[i]in Vowels:
                sk.add(st)
                
            else:
                ss.add(st)
        st=""
    
    ssc=cou(string,ss)
    skc=cou(string,sk)
    if ssc==skc:
        print("Draw")
    else:
        if ssc>skc:
            print("Stuart",ssc)
        else:
            print("Kevin",skc)

def cou(string,ps):
    ck=0
    for ang in ps:
        for c in range(len(string)):
            if string[c:c+len(ang)]==ang:
                ck=ck+1
    return(ck)    

if __name__ == '__main__':
    s = input()
    minion_game(s)