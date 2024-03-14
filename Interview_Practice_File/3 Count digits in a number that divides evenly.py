#3. Count digits in a number
# (Solving above last digit prob wil make this easy for you)

#eg: 12
#count =2(1 divides 12 and gives 0 as remainder.  2 divides 12 and gives 0 as remainder)

# First try

#Using while loop

def count_digit(n):
    count=0
    temp=n
    while temp>0:
        last_digit=temp%10  # Extract the last digit.
        if last_digit!=0 and n%last_digit==0:  # Check if the last digit is not zer and divides the N input evenly, that is the remainder is zero.
            count+=1
        temp//=10  # Remove the last digit.
    return count

n=1234
print(f"The count of the number that divides the digit:{count_digit(n)}")


# Program to count digits in an integer (4 Different Methods)

# Method 1: Iteration

# Time Complexity : O(log10(n)) or O(num digits)
# Auxiliary Space: O(1) or constant

def count_digits(number):
    print("To count the number of digits in a number")
    count=0
    while number>0:
        number//=10
        count+=1
    return count

number=1234
print(count_digits(number))

number=33753567153671523765226765375
print(count_digits(number))

# Method 2: Using String.

# Time Complexity: O(1) or constant
# Auxiliary Space:  O(Number of digits in an integer)

def count_digits_Using_string(number):
    print("To count the number of digits in a number using string")
    return len(str(number))

number=123
print(count_digits_Using_string(number))

number=33753567153671523765226765375
print(count_digits_Using_string(number))

# Method 3: Using math formulae. (Log based)

import math

def count_digits_using_math_formulae(number):
    return math.ceil(math.log10(number)) # return int(math.log10(number)) + 1

number=123
print(count_digits_using_math_formulae(number))
    
number=33753567153671523765226765375
print(count_digits_using_math_formulae(number))


# Method 4: Recursion

def count_digits_Using_Recursion(number):
    if number <= 0:
        return 0
    # recursive case - greater than o.
    else:
        return 1 + count_digits_Using_Recursion(number // 10)
    
number=123
print(count_digits_Using_Recursion(number))
    
number=33753567153671523765226765375
print(count_digits_Using_Recursion(number))