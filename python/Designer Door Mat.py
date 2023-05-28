l=input().split()

ln=int(l[1])
lm=int(l[0])
lw=int((ln-7)/2)
#UP
lnu=int((ln-1)/2)
lnd=lnu
lmu=int((lm-1)/2)
for j in range(0,lmu):
    #left
    for i in range(0,lnu-1):
        print('-',end='')
    print('.',end='')
    for t in range(j):
        print('|..',end='')
    #center
    print('|',end='')
    #right
    
    for t in range(j):
        print('..|',end='')
    print('.',end='')
    for i in range(0,lnu-1):
        print('-',end='')
    print()
    lnu-=3

#WELCOME
for i in range(0,lw):
    print('-',end='')

print('WELCOME',end='')
for i in range(0,(lw)):
    print('-',end='')
print()
#down
lnu+=3
for j in range(lmu,0,-1):
    #left
    for i in range(lnu-1):
        print('-',end='')
    print('.',end='')
    for t in range(j-1):
        print('|..',end='')
    #center
    print('|',end='')
    #right
    for t in range(j-1):
        print('..|',end='')
    print('.',end='')
    for i in range(0,lnu-1):
        print('-',end='')
    print()
    lnu+=3