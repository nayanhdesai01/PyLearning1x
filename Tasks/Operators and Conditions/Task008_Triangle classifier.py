"""Write a program that classifies a triangle based on its side lengths.


Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).


Use an if-else statement to classify the triangle.
"""
side1 = int(input("Enter a side 1: "))
side2 = int(input("Enter a side 2: "))
side3 = int(input("Enter a side 3: "))

if(side1==side2==side3):
    print("Triangle is Equilateral")
elif((side1==side2 or side1==side3 or side2==side3)):
    print("Triangle is Scalene")
else:
    print("Triangle is Isoceles")

