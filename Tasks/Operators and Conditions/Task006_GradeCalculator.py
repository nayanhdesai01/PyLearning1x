"""Write a program that calculates and displays the letter grade for a given numerical score (e.g., A, B, C, D, or F) based on the following grading scale:
input- score - 89
output- B
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: 0-59"""

input_score = int(input("Enter your score: "))

if(input_score >90 and input_score <=100):
    print("A")
elif(input_score >80 and input_score <=89):
    print("B")
elif(input_score >70 and input_score <=79):
    print("C")
elif(input_score >60 and input_score <=69):
    print("D")
else:
    print("F")

