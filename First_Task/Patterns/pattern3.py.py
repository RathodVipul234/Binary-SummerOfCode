n = int(input())

for i in range(n):
    for j in range(n-i):
        print("",end=' ')
    
    if i < 3:
        for j in range(i+1):
            print('*',end=' ')
    else:
        print('*',end='')
        
        for k in range(i-1):
            print(end=' ')
        print('*',end='')
       
        for k in range(i-1):
            print(end=' ')
        print('*',end='')
   
    print(' ')    