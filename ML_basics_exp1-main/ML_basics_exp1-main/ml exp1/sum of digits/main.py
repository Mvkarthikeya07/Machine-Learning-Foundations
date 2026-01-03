# Program to find the sum of digits of a number

# Input from user
num = int(input("Enter a number: "))

original = num
sum_of_digits = 0

while num > 0:
    digit = num % 10       # get last digit
    sum_of_digits += digit # add to sum
    num = num // 10        # remove last digit

print(f"The sum of digits of {original} is {sum_of_digits}")
