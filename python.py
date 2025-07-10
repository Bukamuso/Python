#Numeric Data

num = 3

print(type(num))

num2 =3.14

print(type(num2))

# int num = 3
# float num = 3
# In Python, we don't declare the data type; it automatically asigns

#Variables (valid names)

my_variable = 10
total_count = 0
user = 'John'

#Invalid variable names
_second_variable = 10
user_name = 20
user_name = 20  #line 23 above fixed here

#Operators

# Addition (+)
# Subtraction (-)
# Multiplication (*)
# Division (/)
# Modulus (%) whatever is a remainder after you divide
# Exponent (**)

x = 10
y = 2

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(5%2)

print(x**y)

#Assignment operators (# There are argumented operators we can use)

x = 10
x -= 2

print(x)

#Operators with Strings

str1 = 'Hello'
str2 = 'World'

print(str1 + " " + str2 + " " + str2)

print(str1 * 3)

# Control Statements

num = 0

if num > 0:
    print("This number is positive")
elif num == 0:
    print("This number is zero")
else:
    print("This number is negative")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print(num1, "is greater than", num2)
elif num2 > num1:
    print(num2, "is greater than", num1)
else:
    print("Both numbers are equal")

#Loops

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
    
numbers = [1, 2, 3, 5, 7]

for number in numbers:
    print(number)    
    
#Using a while loop to count from 1 to 5

count = 1

while count <= 5:
    print(count)
    count += 1 #increments the count by 1  
    
#Loop control statements

fruits = ["mango", "avocado", "litch", "date"]

for fruit in fruits:
    if fruit == "litch":
      break  #exits the loop is litch is found
    print(fruit)
    
    print()
    
for fruit in fruits:
    if fruit == "litch":
        continue  #skips litch and moves to the next
    print(fruit)
    
    print()
    
for fruit in fruits:
    if fruit == "litch":
        pass  #placeholder; no action is needed for litch
    print(fruit)
    
    count = 0
    
    while count < 5:
        print(count)
        count += 1
        if count == 3:
            break #exists the loop when the count is 3, which is 3
        
#Operators

# Addition (+)
# Subtraction (-)
# Multiplication (*)
# Division (/)
# Modulus (%) whatever is a remainder after you divide
# Exponent (**)

x = 10
y = 2

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(5%2)

print(x**y)

x = 10
x -= 2

print(x)