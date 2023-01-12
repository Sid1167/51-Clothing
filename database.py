import pymysql as pm

con = pm.connect(host='localhost',port=3306,user='root',password='',database='51Clothing')
                                                                            
cur = con.cursor()

def createtable():
    sqlQuery = "create table if not exists clothing(clothingId int primary key auto_increment,clothingName varchar (150) not Null,clothingPrice double(15,2) default 0,clothingDescription varchar (600))"
    i = cur.execute(sqlQuery)
    print(i,'row affected')
    print('Table has been Created')
    con.commit()

def insert(clothingName,clothingPrice,clothingDescription):
    sqlQuery = f"insert into clothing (clothingName,clothingPrice,clothingDescription)values ('{clothingName}',{clothingPrice},'{clothingDescription}')"
    i = cur.execute(sqlQuery)
    print('Clothing Data has been Added')
    con.commit()

def update(clothingId,clothingName,clothingPrice,clothingDescription):
    sqlQuery = f"update clothing set clothingName='{clothingName}',clothingPrice={clothingPrice},clothingDescription='{clothingDescription}' where clothingId={clothingId}"
    i = cur.execute(sqlQuery)
    print('Clothing Data has been Updated')
    con.commit()

def delete(clothingId):
    sqlQuery = f"delete from clothing where clothingId={clothingId}"
    i = cur.execute(sqlQuery)
    print('Clothing Data has baan Deleted')
    con.commit()

def getall():
    sqlQuery = "select* from clothing"
    i = cur.execute(sqlQuery)
    print(i,'row affected')
    rows = cur.fetchall()
    return rows

def searchbyId(clothingId):
    sqlQuery = f"select* from clothing where clothingId={clothingId}"
    i = cur.execute(sqlQuery)
    print(i,'row is affected')
    row = cur.fetchall()
    return row

def searchbyName(clothingName):
    sqlQuery = f"select* from clothing where clothingName like '{clothingName}%'"
    i = cur.execute(sqlQuery)
    print(i,'row is affected')
    row = cur.fetchall()
    print(row)
    return row   

def sortbyName():
    sqlQuery = f"select* from clothing order by clothingName"
    i = cur.execute(sqlQuery)
    print(i,'row is affected')
    rows = cur.fetchall()
    return rows

def sortbyPrice():
    sqlQuery = f"select* from clothing order by clothingPrice"
    i = cur.execute(sqlQuery)
    print(i,'row is affected')
    rows = cur.fetchall()
    return rows

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import time
time.clock = time.time

def Chatbot():
    # Give a name to the chatbot “Emo bot”
    bot = ChatBot('Emo') 
    
    # Create a new trainer for the chatbot
    bot = ListTrainer(bot)

    conversation = open('chats.txt','r').readlines()

    bot.train(conversation)
    
    name=input("Enter Your Name: ")
    reply=None     
    while True:
        request =  input(name+':')
        if request in ('Hello' , 'hello' , 'Hii' , 'hii','hi'):
            print(f'Emo: Hello {name} I am Emo Your Friendly Bot!,How can i Help you')
        elif request in ('Help' , 'help') :
            print("Contact us on our Email Id = 51clothing@gmail.com")
        elif  request in  ['bye' , 'Bye']:
            print('Emo: Bye')
            break
        else:
            reply = bot.conversation(request)      
    return reply

def closeDB():
    con.close()
