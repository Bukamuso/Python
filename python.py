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

#Control Statements (they allow the flow of executions based on certain conditions)

num = 0

if num > 0:
    print("This number is positive")
elif num == 0:
    print("This number is zero")
else:
    print("This number is negative")
    
    #This is to ask the user to input variables and values
    
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    if num1 > num2:
        print(num1, "is greater than" , num2)
    elif num2 > num1:
        print(num2, "is greater than", num1)
    else:
        print("Both numbers are equal")    