# Write a Python program to calculate the area of a circle
# given its radius using the formula area=π×r^2 ( Take pie as 3.14)
import math

radius=float(input("Enter the radius of the circle: \n"))
area1=3.14*(radius**2)
area2=math.pi*(radius**2)
print("The area of the circle is:",area1)
print("The area of the circle is:",area2)
