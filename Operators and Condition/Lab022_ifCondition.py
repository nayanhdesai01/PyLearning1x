#Condition
#Set of rules ->age >18 then can watch movie

age=int(input("Enter your age: "))
print(f"My age is: {age}")

if age>=18:
    print("You are old enough to watch movie")
else:
    print("You are not old enough to watch movie")