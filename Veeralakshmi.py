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

#Outline.py file

# from practice import find_university_rank_holder

# # find_university_rank_holder('text.txt')

# university_rank_holder=find_university_rank_holder('text.txt')
# print(university_rank_holder)  #prints None

# from practice import Items
# #from the practice.py file import the class Items

# # item1=Items('Phone',1000,'Samsung',5)
# # item2=Items('Phone',15000,'Redmi',5)
# # item3=Items(model='Oppo',price=25000,name='Phone',quantity=5)
# # item4=Items('Phone',12000,'Moto',5)
# # item5=Items('Phone',13000,'Nokia',5)
# # The above data is saved in items.csv and imported here

# Items.data_import('items.csv')
# # In the class "Items" using the dot notation call the,
# # function data_import and pass the file name -> 'items.csv'

# for i in Items.total_items:
#     print(i)



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

DJANGO

# create venv by selecting the interpreter in the status bar 
# .venv\Scripts\activate
# pip install django 
# django-admin 
# django-admin startproject website . 
# python manage.py runserver localhost=127.0.0.1
# python manage.py runserver 80 
# 
# 
# difference between TCP and UDP 
# Ans: connection oriented(getting proper response) (TCP), connection less (UDP). 
# TCP: Re-transmission of the packets:  3-way handshake syn syn-ack ack. connection oriented(getting proper response)
# UDP: No Re-transmission High chance of data loss. connection less. 
# TCP & UDP - 65535 + 65535
# HTTP -80; HTTPS-443 
# HTTPS is secured because of SSL certificate - Encrypted Cipher Text(Not in human readable form) 

#ftc - 21

# netstat -ant | findstr 80 


# to reduce traffic we use port. 


# http methods:
# get(receive the info) 
# post(pushing the info) 
# put
# delete


# client <----> server
# request ----> server
# client <---- response


# get /   
# / --->indicates index page 


# Response codes: 
# 1xx-> informational 
# 2xx-> ok(correct request and response) 
# 3xx-> redirection 
# 4xx-> Client-side error 
# 5xx-> server-side error 

 
# f12- network - we can see the get, post methods

In urls.py file

from django.shortcuts import HttpResponse

def home(request): 
    return HttpResponse("Hello World HOME PAGE")

def login(request): 
    return HttpResponse("Hello World LOGIN PAGE")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('login/',login),
]

create views.py (inside the website folder) -> where all the pages are called.

templates folder is created(Inside the website folder) and all the html pages are stored in it(dashboard.html,index.html,login_page.html,register_page.html)

inside the urls.py
from . import views

urlpatters=[path('login/',views.login_page)]
		    page - function

      
inside the settings.py(file inside the website folder)
installed_apps=['website']

templates=['dirs':['website/templates']]

mvt structure
modal(data from database or data) views(all logics)-> templates(static content,html,css)->jinja template

urls.py
from django.contrib import admin
from django.urls import path
from . import views # .->Current location


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('login/',views.login_page),
    path('dashboard/',views.dashboard),
    path('register/',views.registration_page),
]

index.html
{%include 'navbar.html'%}
{% block content%}
{{about}} #Calling the key here
{%endblock content%}

navbar.html
<a href="/">HOME</a>
<a href="/dashboard">DASHBOARD</a>
<a href="/login">LOGIN</a>
<a href="/register">REGISTER</a>
<hr>
{%block content%}
{%endblock content%}

login_page.html
{%include 'navbar.html'%}
{% block content%}
<h1>Welcome to login page</h1>
{%endblock content%}

register_page.html
{%include 'navbar.html'%}
{% block content%}
<h1>Welcome to registration page!</h1>
{%endblock content%}

views.py
from django.shortcuts import HttpResponse
from django.shortcuts import render

about="Welcome to my Blog site!"

def home(request):
    context={'about':about}#data
    return render(request,'index.html',context) 

def login_page(request):
    return render(request,'login_page.html')

def dashboard(request):
    return render(request,'dashboard.html')

def registration_page(request):
    return render(request,'register_page.html')


settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website' # code to be inserted @line 40
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'website/templates' # code to be inserted @ line 59
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

dashboard.html
{%include 'navbar.html'%}
{% block content%}
<h1>Welcome to the Dashboard</h1>
{%endblock content%}

Project Creation Flow:

1. Create a folder('django')

2. Open with vscode

3. Inside the django folder create a python file ('main.py')

4. Create the virtual enivronment

	-> Select the interpreter in the status bar(click the 3.12.0 64-bit--> next to Python)
	
	-> Select Create virtual environment in the command palette
	
	-> Select Venv creates a '.venv' virtual environment in the current workspace

	-> Select Python 3.12.0 64-bit ~\AppData\Local|Programs\Python\Python312\python.exe

5. Activate the virtual environment

	   (Code to be written in Terminal)

	-> .venv\Scripts\activate 

	   (Once the virtual environment is activated u could see the (.venv) before the path name)

6. In the terminal write the following commands:

	-> pip install django

	-> django-admin

	-> django-admin startproject projectname .

	                projectname -> sample

	-> python manage.py runserver 80

7. Open the link and check whether the project is running successfully.

	->Starting development server at http://127.0.0.1:80/

	                 (Click the http://127.0.0.1:80/ link)
			
			  A new window will open in the browser


Webpage Creation Flow:

1. Create the html files needed for the webpage in a single folder

	-> Inside the sample folder create 'templates' folder

	-> Create all the htmls file inside the 'templates' folder

	                 (index.html,login.html,dashboard.html,registration.html)

2. Create the views.py file and write the following commands:

	-> from django.shortcuts import HttpResponse
	-> from django.shortcuts import render

	-> Write the functions for the webpages
	-> def login(request): #login --> function name (following html file will be opened when the login function called)
		return render(request,'login.html') #login.html --> html page


3. In the urls.py file under the urlpatters=[], write the path for the pages in your website

	-> from . import views

	-> path('login/',views.login)

4. After creating the views.py and tempaltes folder in the 'settings.py'

	-> Add them (i.e. 

	    in the INSTALLED_APPS=['sample'] #add the sample folder

	    in the TEMPLATES=[{'DIRS':['sample/templates']}]) #add the templates path('sample/tempaltes') inside the dirs

[Practically the easy method urls.py(1), views.py(2), html files(3), settings.py(4)]

To create navbar:

1. create the links inside a html file(navbar.html) and at the end mention the {%block content%}{%endblock content%}

2. {%include 'navbar.html'%}
   {%block content%}
    inside the block, dump all the html code in every html files
   {%endblock content%}

To include a string in the web page:

In views.py

1. create a string
	
	-> about="Welcome to blog site"

	-> create a variable and assign a dictionary
	   content={'about_key':about}
	   return render(request,'index.html',content)

2. call the key inside the index.html, where ever u want.

	->{{about_key}}
	

Why are we using virtual environment?

	->Using a virtual environment avoids installing Django into a global Python environment 
	  and gives you exact control over the libraries used in an application.
	  A virtual environment also makes it easy to Create a requirements.txt file for the environment.

	->Creating a virtual environment for your Django application is a best practice 
	  that helps to manage dependencies and avoid conflicts with system-level Python installations.

Database

default database of django -> sqlite3
Only we can see tabels in admin panel

databases supported by django
PostgreSQL
MariaDB
MySQL
Oracle
SQLite


MYSQL
CRUD - Creaate, Read, Update, Delete

In the settings.py file

to connect the database

DATABASES ={
    'default':{
        'ENGINE':'django.db.backends.mysql', #change sqlite to mysql
        'NAME':'website', #project name
        'USER':'root',
        'PASSWORD':'admin123',
        'DEFAULT-CHARACTER-SET':'utf8', 
    }
}

Install the following to connect the database
pip install mysql-connector-python
pip install mysqlclient

Bootstrap

Install the bootstrap
pip install django-bootstrap-v5

In the settings.py

INSTALLED_APPS=['bootstrap5'] #add


After installing bootstrap
In the navbar.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}{% endblock %}</title>
    {% load bootstrap5 %}
    {% bootstrap_css %}
    {% bootstrap_javascript %}
</head>
<body>
    <div class="container">
        <ul class="nav bg-dark">
          <li class="nav-item">
            <a class="nav-link link-light" href="/">HOME</a>
          </li>
          <li class="nav-item">
            <a class="nav-link link-light" href="/dashboard">DASHBOARD</a>
          </li>
          <li class="nav-item">
            <a class="nav-link link-light" href="/login">LOGIN</a>
          </li>
          <li class="nav-item">
            <a class="nav-link link-light" href="/register">REGISTER</a>
          </li>
        </ul>
    </div>
<hr>
{%block content%}
{%endblock content%}
</body>
</html>


Why are we using virtual environment?

	->Using a virtual environment avoids installing Django into a global Python environment 
	  and gives you exact control over the libraries used in an application.
	  A virtual environment also makes it easy to Create a requirements.txt file for the environment.

	->Creating a virtual environment for your Django application is a best practice 
	  that helps to manage dependencies and avoid conflicts with system-level Python installations.

Database

default database of django -> sqlite3
Only we can see tabels in admin panel

databases supported by django
PostgreSQL
MariaDB
MySQL
Oracle
SQLite


MYSQL
CRUD - Creaate, Read, Update, Delete

In the settings.py file

to connect the database

DATABASES ={
    'default':{
        'ENGINE':'django.db.backends.mysql', #change sqlite to mysql
        'NAME':'website', #project name
        'USER':'root',
        'PASSWORD':'admin123',
        'DEFAULT-CHARACTER-SET':'utf8', 
    }
}

Install the following to connect the database

Use any one:
pip install mysql-connector-python
pip install mysqlclient

Bootstap

Install the bootstrap
pip install djano-bootstrap-v5

In the settings.py

INSTALLED_APPS=['bootstrap5'] #add


After installing bootstrap
In the navbar.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}{% endblock %}</title>
    {% load bootstrap5 %}
    {% bootstrap_css %}
    {% bootstrap_javascript %}
</head>
<body>
    <div class="container">
        <ul class="nav bg-dark">
          <li class="nav-item">
            <a class="nav-link link-light" href="/">HOME</a>
          </li>
          <li class="nav-item">
            <a class="nav-link link-light" href="/dashboard">DASHBOARD</a>
          </li>
          <li class="nav-item">
            <a class="nav-link link-light" href="/login">LOGIN</a>
          </li>
          <li class="nav-item">
            <a class="nav-link link-light" href="/register">REGISTER</a>
          </li>
        </ul>
    </div>
<hr>
{%block content%}
{%endblock content%}
</body>
</html>

After running these two commands the tables created automatically in the sql

python .\manage.py makemigrations

python .\manage.py migrate

If operation error occurs, then database is not connected properly

operation error- database error

To create a user

python .\manage.py createsuperuser

	-> Username(leave blank to use 'asus'): admin (User name whatever you prefer)

	-> Email address: (if u need u can give otherwise leave it as blank and then press enter)

	-> Password: (write the password)

	-> Password (again): (re-enter the password and this time it won't visible to the user)

	-> Bypass password validation and create user anyway?[y/N]: y  (Occurs when the password is weak..)

(The data u have entered above, will reflect in the database)

(The password u have entered above will be encrypted(hashed) and saved in the database,
 NOTE: if you use the terminal, to enter the password it will be a hash value.
       if you directly give the password in the database i.e. direct entry in the databse,
            the password will not stored as an hashed value.)

Decoraters, it act as a condition

First import the decorators, then use it in the program.

	-> from django.contrib.auth.decorators import login_required

	   @login_required(login_url='/login')
	   # Indicates, When the user tries to access the dashboard, when the user doesn't logged in, it moves to the login page
	   def dashboard(request):

		return render(request,'dashboard.html')

csrf    -> cross site request forjery
	-> To avoid hacking

To create a login page

In login_page.html (inside the templates folder)

{%include 'navbar.html'%}
{% block content%}
<br>
<style>
    .card{
        max-width: 375px;
        height: 282px;
        margin: 10px auto;
        padding: 31px;
        border-radius: 8px;
        box-shadow: -1px 0px 16px 2px rgb(230, 169, 224);
        margin-top:57px;
    }
</style>
<div class="card">
    <h1 style="text-align:center">Login</h1><br>
    {%endblock content%}
    <form style="text-align:center" action="" method="POST">
        {% csrf_token %}

        USERNAME: <input type="text" name="uname"><br><br>
        PASSWORD: <input type="password" name="passwd"><br><br>
        <input type="submit" value="LOGIN">
        
    </form>
</div>

Add the path inside the urls.py file

In urls.py

urlpatters=[
    path('login/',views.login_page),
    path('logout/',views.logout_page),  # here we are accessing the function logout_page
]

If the user logged in before then, logout should be displayed
If the user doesn't logged in before then, login should be displayed

from django.shortcuts import login, logout, authenticate

# these are inbuilt login, logout and authenticate methods
#In the views.py file

def login_page(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        passwd=request.POST.get('passwd')
        user=authenticate(username=uname,password=passwd)
        if user is not None:
            login(request,user)
            return redirect('/dashboard')
    return render(request,'login_page.html')

def logout_page(request):
    logout(request)
    return redirect('/)  # here we are redirecting page to the home page

In navbar.html

# if the user is authenticated logout will be displayed,
otherwise login will be displayed

{%if user.is_authenticated%}
<li class="nav-item">
    <a class="nav-link link-light" href="/logout">LOGOUT</a>
</li>
{%else%}
<li class="nav-item">
    <a class="nav-link link-light" href="/login">LOGIN</a>
</li>
{%endif%}


HTML - Static, 
CSS - Style, 
JS - Dynamic Content 

Empty elements - do not have an end tag

Inline(within a line) CSS , 
Internal(within the particular html file) CSS, 
External(Creating a separate html file and linking it to the html file wherever it is need using the link tag) CSS

paragraph always start with a new line -> <p>

<del> -> strike through effect, 
<ins> -> text with underline effect.

text formatting elements -> b, em, i, small, srong, sub, sup, ins, del

address -> italic


Tables are called as models

To create a table in the db:

step 1: Create the model

In models.py

from django.contrib.auth.models import models

# import model, then create the class

class Students(models.Model):
    s_name=models.CharField(max_length=100)
    s_email=models.EmailField(max_length=100)
    s_phone=models.BigIntegerField()
    s_entry_date=models.DateTimeField(auto_now_add=True)
    manager=models.Manager()

step 2: Execute the makemigrations and migrate command

	-> python .\manage.py makemigrations website #your schema name

	-> python .\manage.py migrate

step 3: check the db, whether the table is created

	-> you can view the entire table using the following command:

	select * from website.website_students;

NOTE:

	->id is created automatically in the mysql db(so no need to create a separate column for id)

 	-> manage=models.Manager() -> to call the every field inside the class.

	-> phone number will always comes in biginteger

	-> auto_now_add -> Entry creation time

	-> auto_time -> update time

To create a form(Custom form)

Step 1: create the form

Inside the models.py

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import models, User

class RegisterForm(UserCreationForm):
    email=models.EmailField()
    
    class Meta:
        model = User
        # to connect the user in the model
        fields=['username','email','password1','password2'] #only the selected fields will be displayed in the output
        # fields='__all__'


fields='__all__' -> select all the fields available in the UserCreationForm


step 2:
call the RegistrationForm in the model, and save it in a variable(here 'form' is used)
save the variable(form) in another variable(context) 
while rendering the registration page,also return the context.
 
set if the user entered valid details, 
save the form and redirect to the login page
Otherwise, show the error message


In views.py

from . import models

def registration_page(request):
    form=models.RegisterForm()
    context={'form':form} # this displays the HTML page
    if request.method=="POST":
        form=models.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
        else:
            messages.error(request,"User Creation Failed. Try again!")
    return render(request,'register_page.html',context)

In register_page.html

<form method="POST" action="">
    {%csrf_token%}
    <div><div>{{form.username.label}}:</div><div>{{form.username}}</div></div><br>
    <div><div>{{form.email.label}}:</div><div>{{form.email}}</div></div><br>
    <div><div>{{form.password1.label}}:</div><div>{{form.password1}}</div></div><br>
    <div><div>{{form.password2.label}}:</div><div>{{form.password2}}</div></div><br>
{%if messages%}
<ul class="messages">
    {%for message in messages%}
    {{message}}
    {%endfor%}
</ul>
{%endif%}
<div class="button_center"><input class="button_style" type="submit" value="REGISTER"></div>
</form>
{% comment %} {{form.username.label}} {{form.as_p}} {% endcomment %}
{% comment %} to have a default perfect alignment {% endcomment %}



django flash messages, to throw errors

To install crispy forms

step 1: pip install django-crispy-forms

step 2: In settings.py add,

	'crispy_forms', -> inside the INSTALLED APPS=[]

	after that add,

	CRISPY_TEMPLATE_PACK = 'bootstrap4'

To use django-crispy-forms in Django templates:

{%load crispy_forms_tags %}  -> in the top of the django template

the replace {{form}} with {{form|crispy}}

To Add IMAGE

1. Create a static folder inside the project(website)

2. Store all the images inside the static folder

3. Add the path of the static folder inside the settings.py

	-> settings.py

	   STATICFILES_DIR=[BASE_DIR/"static"]

4. Add the image inside the desired folder(index.html -> image)

{%load static%}

<img src="{%static 'bg.jpeg'%}" width=85.5%% height="800" style="margin:0 149px 0px 47px;">

To create a dashboard, 
where details like name, email, phone can be added to the database using a button(add button)
Display the details in a table format and 
Add update and delete buttons to each entry

NOTE: Before adding the value into the table,
open the file models.py and
run the below commands in the terminal,

	-> python manage.py makemigrations website

	-> python manage.py migrate


In dashboard.html

<div style="text-align:center; background-color:LightGrey; margin:45px auto; border:5px solid black; max-width:500px; padding:20px;">

//Form created to retrive the details from the user.

    <form method="POST" action="" atuocomplete="off">
        {%csrf_token%}
        <b><label>Name:</label><b>
        <input type="text" name="name" placeholder="Enter your Name"><br><br>
        <b><label>Email:</label><b>
        <input type="text" name="email" placeholder="Enter your E-mail"><br><br>
        <b><label>Phone:</label><b>
        <input type="text" name="phone" placeholder="Enter your Phone"><br><br>
        <input type="submit" value="ADD">

Once the values are entered perfectly,
the below message will be displayed
(In views.py, the message to be displayed function is written)

        {%if messages%}
        <ul class="messages">
            {%for message in messages%}
            {{message}}
            {%endfor%}
        </ul>
        {%endif%}
    </form>
</div>

In the below table, 
the above details collected will be displayed

<table>
    <tr>
      <th>S.No</th>
      <th>Name</th>
      <th>E-mail</th>
      <th>Phone</th>
      <th style="text-align:center" colspan="2">Options</th>
    </tr>

for the r_data called here, the function is written in views.py

        {%for i in r_data%}

    <tr>
      <td>{{forloop.counter}}</td>

for the s_name, s_email, s_phone data, the function is written in views.py

      <td>{{i.s_name}}</td>
      <td>{{i.s_email}}</td>
      <td>{{i.s_phone}}</td>

pk -> primary key

      <td><button onclick="location.href='{%url 'up_student' pk=i.id %}'">Update</button></td>
      <td><button onclick="location.href='{%url 'del_student' pk=i.id %}'">Delete</button></td>
      {%endfor%}
    </tr>
</table>
{%endblock content%}
</html>

In views.py

@login_required(login_url='/login')
def dashboard(request):
    if request.method=="POST":

All the class Students details(i.e. database values(table is created inside the models.py under the class Students)) 
are saved in the data variable

        data=models.Students()

the data received(get)from the form in the dashboard.html
saved in the data's s_name variable(the s_name here should match the s_name variable in the class Students)

	data.s_name=request.POST.get('name')
 
		the name here and dashboard's input name should match('name')
				same for the email and phone
        data.s_email=request.POST.get('email')
        data.s_phone=request.POST.get('phone')
        
	try:
            if data!="":
                data.save()
                messages.success(request,'Entry Created successfully.')
        except (ValueError,TypeError):
            messages.error(request,'Incomplete Detail')
    
All the details, name, email, phone no, entry date are stored in the r_data
(these are table column names which is created in the models.py inside the class Students)

    r_data=models.Students.manager.all()


    context={'r_data':r_data}
    return render(request,'dashboard.html',context)


To update and delete the data saved in the database

Create file update.html, 
For delete we are just redirecting the page to the dashboard,
so no need of separate delete.html

In views.py

def update_student(request, pk):
    data = models.Students.manager.get(pk=pk)
    context = {'data': data}
    if request.method == "POST":
        data.s_name = request.POST.get("name")
        data.s_email = request.POST.get("email")
        data.s_phone = request.POST.get("phone")
        data.save()
        messages.success(request, "Student details updated successfully.")
    return render(request, 'update.html', context)


def delete_student(request, pk):
    data = models.Students.manager.filter(pk=pk)
    data.delete()
    return redirect('dashboard')

In urls.py

add the below paths

path('dashboard/',views.dashboard, name="dashboard"),

add name to the dashboard

path('update_student/<int:pk>',views.update_student,name='up_student'),
path('delete_student/<int:pk>',views.delete_student,name='del_student'),


In update.html

create a form which will accept the name, e-mail, phone no.
mention the name and value for the input field as same as in the views.py file

<div style="background-color:powderblue; text-align:center; border:2px solid black; padding:20px; max-width:350px; margin:auto;">
    {% comment %} {{data}} {% endcomment %}
    <form method="POST" action="">
        {%csrf_token%}
        <label>Name:</label>
        <input type="text" value="{{data.s_name}}" name="name"><br><br>
        <label>E-mail:</label>
        <input type="text" value="{{data.s_email}}" name="email"><br><br>
        <label>Phone:</label>
        <input type="text" value="{{data.s_phone}}" name="phone"><br><br>
        <input type="submit" value="Update">
        {%if messages%}
        <ul class="messages">
            {%for message in messages%}
                {{message}}
            {%endfor%}
        </ul>
        {%endif%}
</div>


SCRAPY

Refer the documentation of scrapy

1.Creating a new Scrapy project

2.Writing a spider to crawl a site and extract data

3.Exporting the scraped data using the command line

4.Changing spider to recursively follow links

5.Using spider arguments


SCRAPY PROJECT

1. Create a new project(python_scrapy)

2. Create a virtual environment

3. Install scrapy

pip install scrapy

4. To create a project 

NOTE: Don't forget to put fullstop in the end

scrapy startproject tutorial .

5. Inside the spiders folder,
create a python file (first_spider.py)

write the below code

from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            "https://quotes.toscrape.com/page/1/",
            "https://quotes.toscrape.com/page/2/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")

6. Run the spider file
 
Run the below code in the terminal

scrapy crawl quotes (here the quotes is the name inside the class)

->Two html files quotes-1 and quotes-2 will be created automatically inside the python_scrapy project

-> i.e. the above 2 mentioned pages in the url will be saved locally.

-> if we right click the quotes-1.html and 
	select the Reveal in File explorer option,
	saved local html page will be displayed.


what are the different types of selector in scrapy
xpath, css

difference between xpath and css

xpath -> function
//span/text()

css -> calling the variable directly
span::text 

SCRAPY - AMAZON

To scrap the amazon website to get all the names of the headphones
And save all the names in a txt file

In the first_spider.py

from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "amazon"

    def start_requests(self):
        urls = [
            "https://www.amazon.in/s?k=headphones",
            "https://www.amazon.in/s?k=headphones&page=2",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            
    def parse(self,response):
        names=response.css(".a-color-base.a-text-normal::text").getall()
        for i in names:
            with open("amazon_names.txt","a") as f:
                f.write(i+"\n")

To view the data in the shell

scrapy shell https://www.amazon.in/s?k=headphones

In the shell,

view(response)

inspect -> span -> copy -> full xpath

/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[4]/div/div/span/div/div/div/div[2]/div/div/div[1]/h2/a/span

response.xpath("/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[4]/div/div/span/div/div/div/div[2]/div/div/div[1]/h2/a/span/text()").get()

if u need list -> getall()
if u need only string -> get()

To make the work easier, 
We are using selector gadget

Reason 1: instead copying the xpath or full xpath or selector path

Reason 2: the xpath or full path or selector path have some variations for some reasons(if they have discount, if they have today's sale)

So, instead of using try, except block 

WE USE SELECTOR GADGET 

NOTE: SELECTOR GADGET only works for LIVE PAGES

selector gadget chrome-> add to chrome -> pin it

Once selector gadget is pinned, when we click the name of the product,

we can easily get the class name in the below search bar

.a-color-base.a-text-normal

Now, write the class name inside the parse function

response.css(".a-color-base.a-text-normal::text").get()

response.css(".a-color-base.a-text-normal::text").getall()


Here the all the names of the headphones are stored in a variable names,
A new file amazon_names.txt was opened in append mode(if we open in the write mode it does not entering the data into new line, so we are using append mode) and 
all the names are written in the txt file

def parse(self,response):
        names=response.css(".a-color-base.a-text-normal::text").getall()
        for i in names:
            with open("amazon_names.txt","a") as f:
                f.write(i+"\n")


urls = []
        for i in range(1, 21):
            urls.append(f"https://www.amazon.in/s?k=headphones&page={i}")

To create a connection to a database in django..

1. create a database in mysql...(students_entry) -> Manually.

In Django Project
2. Then, make the changes related to database in the settings.py

3. Then, write -> python manage.py makemigrations and python manage.py migrate

4. Then, Create superuser -> python .\manage.py createsuperuser

Username (leave blank to use 'asus'): admin_veera
Email address: veeralakshmimariyappan2003@gmail.com
Password: Veera@2003
Password (again): Veera@2003
Superuser created successfully.

if ctrl+c is not working vscode, 
then Files > Preferences > Keyboard Shortcuts > copy > Add keybindings > ctrl+c

pip install pillow -> for image field

