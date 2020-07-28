no = int(input())


spaces = no-1

for i in range(no):
    for j in range(spaces):
        print(end=' ')
    
    spaces -= 1
    li = list(range(1,no+1))
    for k in range(i+1):
        if i % 2 == 0:
            print('* ',end='')
        else:
            n = li[:i+1]
            for item in n:
                print(f"{item} ",end='')
            break
    print('\r')
