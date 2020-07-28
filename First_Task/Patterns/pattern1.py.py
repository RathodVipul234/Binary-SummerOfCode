n = int(input())

for i in range(1,n+1):
    A = 65
    Z = 90
    for j in range(0,(n-((n+i+1)//2)+1)):
        if i % 2 != 0:
            print(f"{chr(A)} ",end=' ')
            A += 1
        else:
            print(f" {chr(Z)}",end=' ')
            Z -= 1
    print('')

for i in range(1,n):
    A = 65
    Z = 90
    for j in range(0,(i//2)+1):
        if i % 2 != 0:
            print(f" {chr(Z)}",end=' ')
            Z -= 1
        else:
            print(f"{chr(A)} ",end=' ')
            A += 1
    print('')
