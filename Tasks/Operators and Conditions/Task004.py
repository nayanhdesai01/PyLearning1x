#Find the max of 3 numbers using ternary operators

num1=int(input("Enter the first number: \n"))
num2=int(input("Enter the second number: \n"))
num3=int(input("Enter the third number: \n"))

max_num=num1 if(num1>num2 and num1>num3) else (num2 if(num2>num3) else num3)

print(f"{max_num} is maximum of {num1},{num2} and {num3}")