def print_rangoli(size):
    # your code goes here
    l=""
    ch=97+size-1
    for i in range(size-1,-1,-1):
        for j in range(size-i-1):    
            l=l+chr(ch-j)
        
        for j in range(size-i-1,-1,-1):    
            l=l+chr(ch-j)
            
        l="-".join(list(l))
        print(l.center((size*2-1)+(size*2-2),'-'))
        l=""
    for i in range(1,size,1):
        for j in range(size-i-1):    
            l=l+chr(ch-j)
            
        for j in range(size-i-1,-1,-1):    
                l=l+chr(ch-j)
                
        l="-".join(list(l))
        print(l.center((size*2-1)+(size*2-2),'-'))
        l=""
    
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)