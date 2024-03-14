#file open in read - 'r', write - 'w'  and append - 'a' mode

#read mode

# with open('text.txt','r') as file:
    
#     #different types of read mode
    
#     # print(file.readable())  #True
    
#     # print(file.read())   #text.txt file's content as it is
    
#     # print(file.readline()) #Abinaya i.e. first line of the text.txt file
    
#     # print(file.readlines()) #List of the text.txt content
    
#     # Assigning the file.readlines() to data and used the for loop
    
    # data=file.readlines()
    # print(data)

    # for i in data:
    #     # print(i.rstrip('\n'))
        
    #     # print(f"{i.rstrip('\n')}")
        
    #     if i.strip('\n')=='Veeralakshmi':
    #         print(f"{i.strip('\n')} is 20 years old")
    #         #I'm able to use \n inside a format string why???
    #     # else:
    #     #     print(f"{i.strip('\n')} is 22 years old")

# Using function, the above is implemented here.

# def find_university_rank_holder(filename):
#     with open(filename,'r') as file:
        
#         #readlines() saves the data in a list
        
#         data=file.readlines()
#         for i in data:
#             if i.strip('\n')=='Veeralakshmi':
#                 print(i.strip('\n'), "is 20 years old.")
#             # else:
#             #     print(i.strip('\n'), "is a 22 years old.")
                
# # find_university_rank_holder('text.txt')

# with open('text.txt','r') as file:
#     print(file.readlines())
    
# with open('text.txt','a') as file:
#     file.write('Rajini\n')

#while attempting to write a file in read mode

# with open('text.txt') as file:
#     print(file.readlines())
    
# with open('text.txt','r') as file:
#     if file.writable():
#         file.write("Rajini")
#     else:
#         print("File is not writable")
 
# Trying to open a file in read mode which is not found, and at the same time 
# open a file in write mode which is not found, then it creates a new file 
# and write the data text_numbers.txt file
    
# with open('text_numbers.txt','r') as file:
#     print(file.readlines())  #Throws an error because no file found
    
# with open('text_numbers.txt','w') as file:
#     for i in range(0,100,5):
#         file.write(str(i) + '\n')   #Creates a new file, if it is not found

#to print the numbers from 5 to 100 with step value 5 

# with open('text_numbers.txt','r') as file:
#     print(file.readlines())
    
# with open('text_numbers.txt','w') as file:
#     # for i in range(0,101,5):
#     #     if i==0:
#     #         continue   # to avoid 0 to be printed
#     #     else:
#     #         file.write(str(i) + '\n')
    
#     for i in range(5,101,5):  #to start printing from 5
#         file.write(str(i) + '\n')

#read a text file 'text.txt' and write in a 'text.csv' file

# with open('text.txt','r') as file:
#     x=file.read()
#     names=x.split('\n')
# print(names)

# with open('text.csv','w') as file:
#     file.write('S.No.,Names,Phone_No.\n')
#     #file.write('1,Rajini,8888899999')
#     for i in range(1,len(names)):
#         file.write(f"{i+1},{names[i]},{8888899999+i}\n")

#to find the valentine for the given name, using the if 

# import csv

# def find_valentine(name):
#     with open('text.csv') as f:
#         a=csv.DictReader(f)
#         data=list(a)
#         for i in data:
#             if i.get('Names') == name:
#                 print(f"Your valentine's ({name}) phone no is: {i.get('Phone_No.')}")
        
# find_valentine(input('Enter your valentine\'s name:'))

#to find the valentine for the given name, using the return and assigning the function call to a variable answer

# import csv

# def find_valentine(name):
#     with open('text.csv') as f:
#         a=csv.DictReader(f)
#         data=list(a)
#         for i in data:
#             if i.get('Names') == name:
#                 return f"Your valentine's ({name}) phone no is: {i.get('Phone_No.')}"
            
    
# answer=find_valentine(input('Enter your valentine\'s name:')) #Assigning the function call to a variable answer

# if answer is not None:
#     print(answer)
# else:
    # print('Best of luck')

# to check the username and password, if it is correct then, Successfully logged in 
# to check the username and password, if the password is not correct and username is correct then, Invalid password
# to check the username and password, if both the username and password are not correct then, No such account found  

# import csv

# def check(name,password):
#     with open('output.csv') as f:
#         a=csv.DictReader(f)
#         data=list(a)
#         for i in data:
#             if (i.get('uname')==name) and (i.get('passwd')==password):
#                 return 'Successfully logged in'
#             elif(i.get('uname')==name) and (i.get('passwd')!=password):
#                 return 'Invalid password'
#         return 'No such account found'
# name=input('Enter your name:')
# password=input('Enter your password:')
# answer=check(name,password)
# print(answer)

# NOTE: try and except is used for analyzing the error.
# Here the output None is tried to catch in except block
# which will not work, since that is a output not an error.

# import csv

# def find_valentine(name):
#     try:
#         with open('text.csv') as f:
#             a=csv.DictReader(f)
#             data=list(a)
#             for i in data:
#                 if i.get('Names')==name:
#                     return f"Your valentine's {name} phone no is: {i.get('Phone_No.')}"
#     except None:
#         print('Best of luck')
            
# print(find_valentine(input('Enter your valentine\'s name:')))

# try and except block

#NOTE: try and except only works when, we except a error in an output
# If the code itself contain any error, then it won't work
# try:
#     print('Hello World\')
# except SyntaxError:
#     print("Error 0x001: Error! Try Again.")

#try and except block

# try:
#     a=int(input("Enter first no:"))
#     b=int(input("Enter second no:"))
#     # print(a+b)  
#     print(a/b)
# except SyntaxError:
#     print('Error 0x001: Error! Try Again.') # arises when syntax error
# except ValueError:
#     print("Error 0x002: Error! Try Again.") # arises when both operation cannot be done on the input value(string and integer cannot be added)
# except ZeroDivisionError:
#     print("Error 0x003: Error! Try Again.") # arises when divide by zero

# This program counts 60 to 0 and after printing one value it clear screens and print the next value

# import time,os

# count=60
# while count>=0:
#     print(count)
#     time.sleep(1)
#     count=count-1
#     os.system('cls')

# This is a fraud program which counts 60 to 0 and after printing one value it prints 5 lines-> \n*5 and prints the next value

# import time
# count=60
# while count>=0:
#     print(count,'\n'*5)
#     time.sleep(1)
#     count=count-1

#timer while seconds is given as input

# import time,os
# my_time=int(input("Enter the time in seconds:"))

# for x in range(my_time,0,-1):
#     seconds=x%60
#     minutes=(x//60)%60
#     hours=x//3600
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)
#     os.system('cls')

# Timer

# import time
# import os

# def timer(hr, min, sec):
#     if sec>60:
#         print("Enter seconds below 60")
#         sec=int(input("Enter the seconds:"))
        
#     total_seconds = hr * 3600 + min * 60 + sec  # Convert hours and minutes to seconds
#     while total_seconds > 0:
#         hours, remainder = divmod(total_seconds, 3600) # total_seconds/3600, to obtain the total no. of hours, where as the 
#                                                        # quotient represents total hours and the remainder represents the remaining seconds 
#         minutes, seconds = divmod(remainder, 60)  #the remaining seconds from the step 1 is divided by 60, where as the 
#                                                        # quotient represents total minutes and the remainder represents the seconds
#         print(f"{hours:02}:{minutes:02}:{seconds:02}", end='\r')
#         time.sleep(1)
#         total_seconds -= 1
#         os.system('cls')  # Clear console screen os.system('cls' if os.name == 'nt' else 'clear')
    

# seconds = int(input("Enter the seconds: "))
# minutes = int(input("Enter the minutes: "))
# hours = int(input("Enter the hour: "))
# timer(hours, minutes, seconds)

# Use csv file and check whether the login_status is success, if not then,
# Get the username, if it is not found in the csv file then, ask the user username again
# Get the username, get the password, if it is wrong, then 3 attempts allowed, if it is wrong again then
# again ask the user to enter the username...
# Terminate the program when the login_status is successful.

# import csv
 
# def read_csv(filename):
#     with open(filename, 'r') as f:
#         x = csv.DictReader(f)
#         creds = list(x)
#         return creds


# def authenticate():
#     output = read_csv('output.csv')
#     login_status = False
#     while not login_status:
#         uname = input('Enter your username: ')
#         for i in output:
#             if i.get('uname') == uname:
#                 count = 1
#                 while count <= 3:
#                     passwd = input(f'Attempt {count}: Enter your password: ')
#                     count = count + 1
#                     if i.get('passwd') == passwd:
#                         print('Login Success.')
#                         login_status = True
#                         break
#                     else:
#                         print('Incorrect password. Try Again.')
#                 else:
#                     break
#                 if i.get('uname') == uname and i.get('passwd') == passwd:
#                     break
#         else:
#             print('Username not found.')


# authenticate()

#py -m venv .venv                       these both commands are of no use
#.venv\Scripts\activate

#pip install mysql-connector            both the packages installed in the terminal
#pip install mysql-connector-python 

#To get mysql-connector-python package, click python from the sidebar and then 
# In workspace environments, under packages, click the search icon and search for
# mysql-connector-python , then click on it, package will be installed.

# import mysql.connector

# db=mysql.connector.connect(
#     host="localhost",
#     user='root',
#     password='admin123'
# )

# #print(db)  # prints the database as object

# cursor=db.cursor()
# cursor.execute("select * from students.crendentials where uname='rajini' and")  # with the "" -> double quotes we can give query to be executed

# for i in cursor:
#     print(i)
    

# lambda function is mainly created for future purposes
# Eg: Changing the year 2024 to 2025, Changing one person's phone no.

# x=lambda a: a+10
# print(x(5))

# y=lambda a,b,c: a* b* c
# print(y(5,6,7))

# def myfunc(n):
#     print(f"{n} is n value")
#     return lambda a: a*n
    
# mydoubler=myfunc(3) # n value is 3

# print(mydoubler(4)) # a value is 4

# class is created for creating our data type. 
# Class -> blueprint  
# Instance -> copy of class, 
# self -> instance's value.
# A function inside a class is called method. 
# Magic method/Constructor. __init__ initialization,
# assert is used to verify

# class Items:
    
# #     #Magic Method, Constructors
     
#     def __init__(self,name:str,price:float,model:str,quantity:int):
        
#         assert quantity>=0, f"{quantity} is less than Zero."
#         assert price>=0, f"{price} is less than Zero."
#         assert len(name)>=3, f"{name} should be more than 3 Characters "
        
#         self.name=name
#         self.price=price
#         self.model=model
#         self.quantity=quantity
        
#     def name(self):
#         return self.name
    
#     def price(self):
#         return self.price
    
#     def quantity(self):
#         return self.quantity
    
#     def total_price(self):
#         return self.price * self.quantity
    
# item1=Items(name='phone',price=15000,model='Samsung',quantity=15)  #objects
# item2=Items(model='Iphone',name='phone',price=70000,quantity=5)
# item3=Items(price=100000,quantity=1,model="Samsung_S23_Flip",name="phone")
        
# print(item1.total_price())
# print(item3.total_price())

# # print(item3.name())  # 'str' object is not callable only functions are callable

# print(item3.name) # while you want to just print the value of a particular variable
#                   # then just give the parameter name


# import csv

# class Items:
#     # class-level variable
#     total_items = []

#     # Magic Method, Constructors
#     def __init__(self, name: str, price: float, model: str, quantity: int):
#         assert quantity >= 0, f"{quantity} is less than Zero."
#         assert price >= 0, f"{price} should not be less than Zero."
#         assert len(name) >= 3, f"{name} be 3 or more characters."

#         self.name = name
#         self.price = price
#         self.model = model
#         self.quantity = quantity

#         Items.total_items.append(self)

#     @classmethod  # Decorators
#     def data_import(filename):
#         with open(filename, 'r') as file:
#             x = csv.DictReader(file)
#             data = list(x)

#             for i in data:
#                 Items(
#                     name=i.get("name"),
#                     price=float(i.get("price")),
#                     model=i.get("model"),
#                     quantity=int(i.get("quantity")),
#                 )

#     def name(self):
#         return self.name

#     def price(self):
#         return self.price

#     def quantity(self):
#         return self.quantity

#     def total_price(self):
#         return self.price * self.quantity

#     def __repr__(self): # __repr__ how it displays
#         return f"Items('{self.name}', {self.price}, '{self.model}', {self.quantity})"



# the code inside the constructor gets executed automatically when the class is called 
# Decorators-> 
# classmethod-> data that changes Dynamically, for every instance the data will change, -> cls is the first parameter. 
# staticmethod-> will not change for every instances, it is common for all the instances that have created -> Converting every value into dollar, float like that


# codechef, interviewbit, leetcode, hackerearth 
# 1. w3schools-exercises 
# 2. codingbat(logic 1, logic 2) 
# 3. hackerearth.com 


# Four pillars of python(OOPs)  
# 5 types of inheritance : 
# Single inheritance -> class derived from one parent class. 
# Multiple inheritance -> class derived from two parent classes. 
# Multilevel inheritance ->  Class derived from base class, intermediate class,(grandfather(base class) -> father(intermediate class) -> son(derived class)). 
# Hierarchical inheritance -> class derived from single base class have multiple child classes(parent -> siblings).
# Mixture of all the types of inheritance.

# polymorphism -> poly means many, morph means forms 
# single method multiple output 
# eg: len (len function can count a array's length as well as count the length for string, list etc..), date, time Inheritance works top to bottom (we can call the methods from parent to child but we cannot call the methods from child to parent)
                                                                                            
#  abstraction -> showing the essential details and hiding the unnecessary details from the user 

#  encapsulation -> binding the values. private and protected. 
#  private members-> double underscore(__) the data cannot be accessible from outside the class
#  protect members->  single underscore(_) We use encapsulation to restrict accessability of data. 
#  We can modify the data of the protected member(from parent class) in the child class. 
#  Private member -> we cannot modify or access the data of a private member(from parent class) in the child class.
#  to hide the sensitive info -> we use encapsulation, to hide the unnecessary info -> we use abstraction

#  destructor -> works at end, to delete the  variable i.e. reset to the initial state