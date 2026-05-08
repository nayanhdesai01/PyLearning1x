# Create a program that takes two numbers as input and prints whether
# the first number is greater than, less than, or equal to the second number.

a=int(input("Enter a number1:"))
b=int(input("Enter a number2:"))

result="greater than" if(a>b) else "less than" if(a<b) else "equal to"
print(f"{a} is {result} {b}")