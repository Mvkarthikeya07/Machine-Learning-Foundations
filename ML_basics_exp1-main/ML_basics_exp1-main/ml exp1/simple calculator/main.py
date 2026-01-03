# Simple Calculator in Python

print("Select operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Take input from user
choice = input("Enter choice (1/2/3/4): ")

# Input numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform calculation
if choice == '1':
    result = num1 + num2
    operator = '+'
elif choice == '2':
    result = num1 - num2
    operator = '-'
elif choice == '3':
    result = num1 * num2
    operator = '*'
elif choice == '4':
    if num2 == 0:
        print("Error! Division by zero.")
        exit()
    result = num1 / num2
    operator = '/'
else:
    print("Invalid input!")
    exit()

# Display result
print(f"{num1} {operator} {num2} = {result}")
