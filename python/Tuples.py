if __name__ == '__main__':
    n = int(input())
    #integer_list = map(int, input().split())
    integer_list=[]
    str_list=input().split()
    
    for i in range(len(str_list)):
        integer_list.append(int(str_list[i]))
    
    #print(integer_list)  
    t=tuple(integer_list)
    print(hash(t)) 