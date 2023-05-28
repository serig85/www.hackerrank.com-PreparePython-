if __name__ == '__main__':
    s = input()
    ls=len(s)
    
    c=False
    for i in range(0,ls):
        if (s[i].isalnum())==True:
              c=True
    print(c)
    
    c=False
    for i in range(0,ls):
        if (s[i].isalpha())==True:
            c=True
    print(c)
    
    c=False
    for i in range(0,ls):
        if (s[i].isdigit())==True:
            c=True
    print(c)
           
    
    c=False
    for i in range(0,ls):
        if (s[i].islower())==True:
            c=True
    print(c)
    
    c=False
    for i in range(0,ls):
        if (s[i].isupper())==True:
            c=True
    print(c)