# 1. Assignmnent Operator.

print("Assignment Operator");

# The assignment operator is used to assign a value to a variable:
age = 20;

# To assign a variable value to another variable:
my_age = age;
print(age);
print(my_age);
age = 21;
print(age);
print(my_age);

# walrus operator
# Without walrus operator
numbers = [1, 2, 3, 4, 5]
squared_numbers = []

for num in numbers:
    squared = num ** 2
    squared_numbers.append(squared)

print(squared_numbers)

# With walrus operator
numbers = [1, 2, 3, 4, 5]
squared_numbers = [squared := num ** 2 for num in numbers]

print(squared_numbers)

# 2. Arithmetic Operator.

print("Arithmetic Operator");

# Addition
print(f"Addition: {5 + 2}");

# Subtraction
print(f"Subtraction: {5 - 2}");

# Multiplication
print(f"Multiplication: {5 * 2}");

# Division and Floor Division
print(f"Division: {5 / 2} , Floor Division: {5 // 2}");

# Exponentiation or Power
print(f"Exponentiation: {5 ** 2}");

# Remainder or modulus.
print(f"Modulus: {5 % 2}");

#  unary minus operator
print(f"Unrinary Minus Operator: {-5 + 4}");

# Arithemetic operator + can be used to concatenate string values.
print(f"Conactenate two strings: {'United States ' + 'America'}");

# We can combine the assignment operator with arithmetic operators:

print("We can combine the assignment operator with arithmetic operators.")
age = 1

age += 1; # age = age + 1
print(age) # 2

age -= 1; # age = age - 1
print(age) # 1

age *= 1; # age = age * 1
print(age) # 1

age /= 1; # age = age / 1
print(age) # 1.0 Result in division is always float.

age **= 1; # age = age ** 1
print(age) # 1.0 

age //= 1; # age = age // 1
print(age) # 1.0

age %= 1; age = age % 1
print(age); # 0.0
