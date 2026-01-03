# Program to find the largest of four numbers

# Input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
num4 = float(input("Enter fourth number: "))

# Find the largest
largest = num1  # assume num1 is largest

if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3
if num4 > largest:
    largest = num4

# Display the result
print("The largest number is:", largest)
