def merge_sorted_list(num1,num2):
    num=[]
    i=j=0
    while((i<len(num1))and(j<len(num2))):
        if(num1[i]<num2[j]):
            num+=[num1[i]]
            i+=1
        else:
            num+=[num2[j]]
            j+=1
    num+=num1[i:]
    num+=num2[j:]
    return num
print(f"Merged Sorted list:{merge_sorted_list([1,3,5,7],[2,4,6,8])}")
    
def remove_duplicates(list):
    emp_list=[]
    i=0
    while(i<len(list)):
        if(list[i] not in emp_list):
            emp_list+=[list[i]]
        i+=1
    return emp_list
print(f"Remove duplicates in the given list:{remove_duplicates([1,1,2,3,3,4])}")
            
def move_zeros(nums):
    non_zero_count=0
    for num in nums:
        if(num!=0):
            nums[non_zero_count]=num
            non_zero_count+=1
    for i in range(non_zero_count,len(nums)):
        nums[i]=0
    return nums
print(f"Move zeros:{move_zeros([0,1,2,0,3])}")

def check_palindrome(name):
    left=0
    right=len(name)-1
    while(left<right):
       if(name[left]==name[right]):
            left+=1
            right-=1
       else:
           return False
    return True

test_cases=["zoho","mom","veera","dad","jimin"]

for test_case in test_cases:
    result=check_palindrome(test_cases)

if result:
    print(f"{test_case} is palindrome")
else:
    print(f"{test_case} is not a palindrome")
    

def palindrome(name):
    left=0
    right=len(name)-1
    while(left<right):
        if(name[left]==name[right]):
            left+=1
            right-=1
        else:
            return False
    return True

test_case="mom"
if palindrome(test_case):
    print(f"{test_case} is a palindrome")
else:
    print(f"{test_case} is not a palindrome")
    
def find_last_digit(num):
    return (f"The last digit:{num%10}")

def find_first_digit(num):
    while num>=10:
        num=num//10
    return num

print(f"The first digit is{find_first_digit(123)}\n The last digit is{find_last_digit(123)}")
    
    
def print_word_odd_letters(word):
    n=len(word)
    for i in range(n):
        for j in range(n):
            if(i==j or i+j==n-1):
                print(word[j],end=" ")
            else:
                print(" ",end=" ")
        print()
word="PROGRAM"
print_word_odd_letters(word)

def is_perfect_square(num):
    # Edge case: 0 is a perfect square
    if num == 0:
        return True

    # Start from 1 and check if the square of i equals the number
    i = 1
    while i * i <= num:
        if i * i == num:
            return ("perfect square")
        i += 1

    return ("not a perfect square")

numbers=[20,5,12,16]
for num in numbers:
    print(f"{num} is {is_perfect_square(num)}")
                

#Find sum of weights problem
                
def find_sum_of_weights(number):
    weight=0
    if number%4==0 and num%6==0:
        weight+=4
    if number%2==0:
        weight+=3
    
    def is_perfect_square(number):
        nonlocal weight
        if num==0:
            weight+=5
        i=1
        while i*i <=num:
            if i*i==num:
                weight+=5
            i+=1
    is_perfect_square(number)
    return weight
    
nums=[10,36,54,89,12]
result=[]
for num in nums:
    result+=[num,find_sum_of_weights(num)]
result = [(result[i], result[i + 1]) for i in range(0, len(result), 2)]
print(result)


def is_perfect_square(num):
    i = 1
    while i * i <= num:
        if i * i == num:
            return True
        i += 1
    return False

def find_sum_of_weights(number):
    weight = 0
    if is_perfect_square(number):
        weight += 5
    if number % 4 == 0 and number % 6 == 0:
        weight += 4
    if number % 2 == 0:
        weight += 3
    return weight

def sorting(number):
    n=len(number)
    for i in range(n):
        for j in range(0,n-i-1):
            weight1=find_sum_of_weights(number[j])
            weight2=find_sum_of_weights(number[j+1])
            if weight1>weight2 or (weight1==weight2 and number[j]>number[j+1]):
                number[j],number[j+1]=number[j+1],number[j]
                
nums=[10,36,54,89,12]
sorting(nums)
for i in range(len(nums)):
    num=nums[i]
    weight=find_sum_of_weights(num)
    print(f"<{num},{weight}>", end='')
    if i < len(nums) - 1:
        print(', ', end='')
            


class Railway_reservation_system():
    def __init__(self):
        self.bookings={}
    
    def ticket_booking(self,passenger_name,seat_number):
        if seat_number not in self.bookings:
            self.bookings[seat_number]=passenger_name
            print(f"{passenger_name} Successfully booked the ticked on seat number{seat_number}")
        else:
            print(f"Seat is already booked")
    
    def availability_checking(self,seat_number):
        if seat_number not in self.bookings:
            print(f"{seat_number} is available")
        else:
            print(f"{seat_number} is not booked")
            
    def cancellation(self,seat_number):
        if seat_number in self.bookings:
            passenger_name=self.bookings.pop(seat_number)
            print(f"{passenger_name} is successfully cancelled the seat{seat_number}")
        else:
            print(f"No such seat is booked.")

    def prepare_chart(self):
        print("Passenger seat chart")
        for seat,name in self.bookings.items():
            print(f"seat:{seat},{name}")

reservation_system=Railway_reservation_system()

reservation_system.ticket_booking("Alice",1)
reservation_system.ticket_booking("Bob",2)
reservation_system.ticket_booking("Jimin",3)
reservation_system.ticket_booking("Veera",3)

reservation_system.availability_checking(4)
reservation_system.availability_checking(5)
reservation_system.availability_checking(6)
reservation_system.availability_checking(3)

reservation_system.cancellation(3)
reservation_system.cancellation(4)

reservation_system.prepare_chart()


def is_rectangle(a,b,c,d):
    if (a==b and c==d) or (a==c and b==d) or (a==d and b==c):
        print("It forms an rectangle")
    else:
        print("It doesn't form an rectangle")
        
a,b,c,d=1,1,2,2
is_rectangle(a,b,c,d)

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
num=5
print(f"Factorial of {num} is {factorial(num)}")

def factorial1(n):
    if(n==0):
        return 1
    i=n
    fact=1
    while(n/i!=n):
        fact=fact*i
        i-=1
    return fact

num=5
print(f"The factorial of {num} is:{factorial1(num)}")
