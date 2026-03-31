# String Functions
# Python immutable in nature - They cant be changed! One created

name="ashish"
print(name)

# capitalize()
# Returns a copy of string with its first character capitalized
result1 = name.capitalize()
print(result1)

print(id(name))
print(id(result1))

#Upper case()
result2=name.upper()
print(result2)
print(id(result2))

#Lower case()
result3=name.lower()
print(result3)
print(id(result3))  #Identity -> Address reference

#Swapcase()
#Returns a copy of string with uppercase letters converted to lower case and vice versa

name = "aSHisH"
print(name.swapcase())

#Title
#Returns a title case version of the string(where word starts with
# uppercase character followed by lowercase

name="hello world"
print(name.title())

#Replace
text = "hello world"
result_rep= text.replace("world","python")
print(result_rep)

#find()
#Returns the lowest index of a substring in the string.
#Returns -1 if the substring is not found

text = "hello world"
index=text.find("world")
print(index)

#count()
count=text.count("l")
print(count)

