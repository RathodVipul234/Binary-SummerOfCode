li = []

def insert(s):
    li.append(s)

def update(d,s):
    res = input('Are you sure want to update the item ? (y/n): ')
    if res.lower() == 'y':
        li.__setitem__(d-1,s)
        print('Value updated Successfully...\n')
    
    else:
        print('Sorry you have declined the choice !!\nPlease try again...\n')

def print_item(li):
    print("\nYour ToDo item list as follows :")
    for i,j in enumerate(li):
        print(f"{i+1}. {j}\n")           

def delete_item(s):
    res = input('Are you sure want to delete the item ? (y/n): ')
    if res.lower() == 'y':
        li.remove(li[d-1])
        print('Item deleted Successfully...\n')
    
    else:
        print('Sorry you have declined the choice !!\nPlease try again...\n')

print("------------ToDo List---------")

while True:
    print('-'*30)
    print("""1.Insert\n2.Update\n3.Delete\n4.Print\n5.Exit""")
    try:
        choice = int(input('Enter your Choice: '))
        if choice > 5 or choice <=0:
            print('Enter Valid choice..\n')
        
        else:
            if choice == 1:
                s = input('Enter your Todo Item: ')
                insert(s)
            
            if choice == 2:
                if len(li) == 0 :
                    print(f"Your Todo item list is Empty ..\nYou can't update any value...\n")
                    continue
                
                else:
                    try: 
                        print_item(li)
                        d = int(input('Enter Index for update: '))

                    except ValueError:
                        print('Only interger no. is allowed...\nPlease try again with int no..\n')
                        continue
                    if d > len(li):
                        print("Todo item doesn't Exists\nPlease try again..")
                    else:
                        s = input('Enter new Todo Item: ')
                        update(d,s)
            
            if choice == 3:
                if len(li) == 0 :
                    print(f"Your Todo item list is Empty ..\nYou can't delete any value...\n")
                    continue
                
                else:
                    try:
                        print_item(li)
                        d = int(input('Enter Index for delete: '))
                    except ValueError:
                        print('Only interger no. is allowed...\nPlease try again with int no..\nPlease try again..\n')
                        continue
                    
                    if d > len(li):
                        print("Todo item doesn't Exists\nPlease try again..")
                    else:
                        delete_item(d)
            
            if choice == 4:
                if len(li) == 0:
                    print("\nEmpty Todo list\nCan't have any item to show..\n")
                print_item(li)              
            
            if choice == 5:
                break

    except ValueError:
        print('Only Numeric value is allowed...\nPlease Enter Number\n')
    
    except KeyboardInterrupt:
        print('Only Numeric value is allowed...\nPlease Enter Number\n')