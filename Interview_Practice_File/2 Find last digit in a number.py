#2.Find last digit in a number

#First Try: Converting the given number to string and using index slicing, we can retrieve the last digit

def find_first_digit_And_last_digit(n):
    print("To find the first and last digit in a number")
    print(f"Last digit: {str(n)[-1]}\n")
    print(f"First digit: {str(n)[0]}\n")
    
n=123
print(find_first_digit_And_last_digit(n))


#Using % operator to find the last digit in a number - without using loop

def find_last_digit():
    print("To find the last digit in a number - without using loop")
    return (f"The last digit in {n} is {(n%10)}\n")

import math

def find_first_digit():
    print("To find the first digit in a number - without using loop")
    digit=int(math.log10(n))
    number=int(n/pow(10,digit))
    return (f"The first digit in {n} is {number}\n")

n=123
print(find_last_digit())
print(find_first_digit())


# if you are using a return statement, then print should be used in the function call
# eg: print(find_even_or_odd(n))


#Using while loop

def find_last_digit():
    print("To find the last digit in a number using loop")
    return (f"The last digit in {n} is {(n%10)}\n")

def find_first_digit(n):
    print(f"To find the first digit in a number using loop")
    while n>=10:
        n=n/10
    return int(n)
 
# while using a while loop declare and assign the parameter in both function call and function name, 
# if the value of the parameter is not a local variable
 
 
n=123   
print(find_last_digit())
print(find_first_digit(n))

