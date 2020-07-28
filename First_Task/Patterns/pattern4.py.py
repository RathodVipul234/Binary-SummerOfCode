no = int(input())

li = list(range(1,no+1))

for i in range(no-1,-1,-1):
    pat = li[i:]
    for i in pat:
        print(i,end=' ')
    print('')