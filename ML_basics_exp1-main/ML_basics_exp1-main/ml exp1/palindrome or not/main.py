# Program to check if a number is a palindrome

# Input from user
num = input("Enter a number: ")

# Check palindrome
if num == num[::-1]:
    print(num, "is a palindrome.")
else:
    print(num, "is not a palindrome.")
