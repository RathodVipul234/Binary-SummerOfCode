no = int(input())

li = list(range(1,no+1))
ap_li = li[:-1]
ap_li.reverse()
for item in ap_li:
    li.append(item)

for i in range(0,no):
    a = li[i:(2*no-1)-i]
    for i in a:
        print(i,end='')  # gap is required because of 2 digit no
    print('')