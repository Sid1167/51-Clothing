import database as db

db.createtable()

menu =f'''
      Wellcome to 51 Clothing Management System
     {'-'*40}
     1. Add Clothing
     2. Update Clothing
     3. Delete Clothing
     4. Show All Clothing
     5. Show Clothing by Id
     6. Show Clothing by Name
     7. Sort Clothing List by Name
     8. Sort Clothing List by Price
     9. Chat Bot
    10. Exit
     {'-'*40}
     Select your Choice
'''

choice = 0

while choice!=11:
    choice = int(input(menu))

    if choice==1:
        name = input("Enter Name = ")
        price = eval(input("Enter Price = "))
        description = input("Enter Description")
        db.insert(name,price,description)
        print('Clothing Data has been Added')

    elif choice==2:
        id = int(input("Enter Id = "))
        name = input("Enter Name = ")
        price = eval(input("Enter Price = "))
        description = input("Enter Description")
        db.update(id,name,price,description)
        print('Clothing Data has been Updated')

    elif choice==3:
        id = int(input("Enter Id = "))
        db.delete(id)
        print('Clothing Data has been Deleted')

    elif choice==4:
        clothinglist = db.getall()
        if len(clothinglist)>0:
            print('-*-'*5,"51 Clothing List",'-*-'*5)
            for clothing in clothinglist:
                print('\t',clothing)
                print('-'*45)
        else:
            print('No Clothing Available')

    elif choice==5:
        id = int(input("Enter Clothing Id = "))
        clothing = db.searchbyId(id)
        if clothing!= None:
            print(clothing)
        else:
            print('No Clothing Found')

    elif choice==6:
        name = input("Enter Clothing Name = ")
        clothing1 = db.searchbyName(name)
        if clothing1!= None:
            print(clothing1)
        else:
            print('No Clothing Found')

    elif choice==7:
        sort = db.sortbyName()
        print(sort)

    elif choice==8:
        sort1 = db.sortbyPrice()
        print(sort1)

    elif choice==9:
        db.Chatbot()
        print('Chat Bot is running')

    elif choice==10:
        db.closeDB()

    else:
        print('Invalid Choice Entered')

