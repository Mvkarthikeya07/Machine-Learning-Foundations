# Program to add two numbers safely

while True:
    try:
        num1 = float(input("Enter the first number: "))
        break
    except ValueError:
        print("Invalid input! Please enter a number.")

while True:
    try:
        num2 = float(input("Enter the second number: "))
        break
    except ValueError:
        print("Invalid input! Please enter a number.")

# Addition
sum_result = num1 + num2

# Display the result
print(f"The sum of {num1} and {num2} is: {sum_result}")
