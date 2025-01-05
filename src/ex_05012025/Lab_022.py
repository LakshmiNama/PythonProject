# Grade Calculator
# Write a program that calculates and displays the letter grade for a given numerical score
# based on the following grading scale

# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# E: 0-59

marks = int(input("Please enter your marks\n"))

if marks >= 100 and marks <= 100:
    print("Your grade is A")
elif marks >= 80 and marks <= 89:
    print("Your grade is B")
elif marks >= 70 and marks <= 79:
    print("Your grade is C")
elif 60 <= marks <= 69:
# elif marks >= 60 and marks <= 69:
    print("Your grade is D")
elif marks >= 0 and marks <= 59:
    print("Your grade is E")
else:
    print("Please enter marks between 0-100")
