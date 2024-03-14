#Interview practice - coding practice file

#1. Find even or odd

#First Try: Using if else

#Time Complexity: O(1)
#Auxiliary Space: O(1)

def find_even_or_odd():
    print("To Find whether the given number is even or odd")
    number=int(input("Enter a number:"))
    if number%2==0:
        print(f"The given number {number} is Even\n")
    else:
        print(f"The given number {number} is Odd\n")
find_even_or_odd()

#Note: While calling a function, 
# if the input will be given by the user, then no need of mention the argument, while calling a function
# eg: def find_even_or_odd():


#Method 1: Using if else, single line code

#Time Complexity: O(1)
#Auxiliary Space: O(1)

def isEven():
    return (n%2==0)
print("To Find whether the given number is even or odd")
n=int(input("Enter a number:"))
print(f"The given number {n} is Even\n" if isEven() else f"The given number {n} is Odd\n")


#Method 2: Using bitwise &(and) operator

#Time Complexity: O(1)
#Auxiliary Space: O(1)

def Even_or_Odd(n):
    # n&1 is 1, then odd, else even 
    return (not(n&1))
n=2
print(f"{n} is even\n" if Even_or_Odd(n) else f"{n} is odd\n")

n=5
print(f"{n} is even\n" if Even_or_Odd(n) else f"{n} is odd\n")

# if the input is already defined in the program, then mention the argument, while calling a function
# eg: def find_even_or_odd(n):


#Method 3: Using right shift and right shift operators

#Time Complexity: O(1)
#Auxiliary Space: O(1)

def isEven(n):
    # Original number == ((original number >> 1)<< 1)
    return (n==((n>>1)<<1))

n=2
print(f"{n} is Even.\n" if isEven(n) else f"{n} is Odd.\n")

n=5
print(f"{n} is Even.\n" if isEven(n) else f"{n} is Odd.\n")