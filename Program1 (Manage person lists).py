l=[]
while True:
    print('**Program to handle usernames**','\n')
    print('Option 1: You can add new persons')
    print('Option 2: You can add new persons in specific locations')
    print('Option 3: You can delete any person from the menu')
    
    a=int(input('Enter option: '))
    if a==1:
        while True:
            print('Current list status: ',l)
            b=input('Add username: ')
            l.append(b)
            c=input('Add more users? Y/N: ')
            if c=='Y':
                continue
            else:
                break
    if a==2:
        while True:
            print('Current list status: ',l)
            d=input('Add username: ')
            e=int(input('Specify location: '))
            l.insert(e,d)
            f=input('Add more users? Y/N: ')
            if f=='Y':
                continue
            else:
                break
    if a==3:
        while True:
            print('Current list status: ',l)
            print('Select the record to be deleted')
            g=input('Enter the username: ')
            l.remove(g)
            h=input('Delete more users? Y/N: ')
            if h=='Y':
                continue
            else:
                break


            
            
            
            
