# Program to print multiplication table

# Input from user
num = int(input("Enter a number to print its multiplication table: "))

print(f"Multiplication table of {num}:")

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
