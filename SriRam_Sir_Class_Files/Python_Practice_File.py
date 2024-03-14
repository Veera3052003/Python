print("Day 1 - 18/Nov/2023");
print("Topics: Variable, Indentation, Comments, Data Types, Assignment Operator, Arithmetic Operator and Unary Operator");

name="veeralakshmi";#Variable name and String eg
print(f"My name is: {name}");#printing name using format
print(f"Data type of name {name} is {type(name)}");#Printing data type of name

age=20;#Integer eg
print(f"My age is: {age}"); #printing age using format
print(type(age));#Printing the data type of age

percentage=94.57;#Floating point number eg
print(f"This is Floating point number : {percentage}"); #printing percentage using format
print(type(percentage));#Printing the data type of percentage

#Hash mark is used for inline comment

'''Triples quotes 
is used for 
multiline comment'''

print("Data types")#Data types:Integer, String, Boolean
first_name="Jimin ";
last_name="Park";
print(f"First name and Last name: {first_name + last_name}");#String Concantenation

bias_name=first_name+last_name;#storing values of variables into another variable
print(f"Bias_name:{bias_name}");

print(f"String Slicing:{bias_name[0:5:1]}");#String slicing

yoongi_oppa="AGUST D";
print(f"Reverse the string:{yoongi_oppa[-1:-8:-1]}");#Reverse the string

yoongi_oppa=yoongi_oppa[-1:-8:-1];
print(f"String slicing:{yoongi_oppa[3:7:1]}");#String slicing

print("Arithmetic Operator");
print(f"Addition:{1+2}");
print(f"Subtraction:{2-1}");
print(f"Multiplication:{2*1}");
print(f"Division:{2/1}");
print(f"Modulus:{2%1}");
print(f"Exponent:{2**1}");

