from os import name

val=None
Name=None
# None is not same as false
# None is not an empty string
# None is not 0
# val=None+2   unsupported operand type(s) for +: 'NoneType' and 'int'

print(val)
Name ="Arun"
print(Name)
print(type(val))  # <class 'NoneType'>

del Name
print(Name) #NameError: name 'Name' is not defined. Did you mean: 'name'?

