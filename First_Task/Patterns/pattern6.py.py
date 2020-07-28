no = int(input())

for i in range(no):
    for j in range(i):
        print("",end=' ')
    for j in range(no-i):
        a = j+1+i
        print(a,end=' ')
        a += 1
    print('')
    
for i in range(no):
    for j in range(no-i-1):
        print(end=' ')
    a = no-i
    for j in range(i+1):
        print(a,end=' ')
        a += 1
    print('')