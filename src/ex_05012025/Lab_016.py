# Write a python program to calculate the
# area of a circle given it's radius using the formula
# '';' area = pi*r^2''' (take pie as 3.14
import math

radius = float(input("Enter the radius of a circle\n"))

# print("Area of a circle is", math.pi*pow(radius,2))
print("Pi value is", math.pi)
area = math.pi * math.pow(radius,2)
print("Area of a circle is ->", area)
print(f"Area of a circle is -> {area:.2f}")

# * -> Multiplication
# ** -> Power

# Convert above code in one line

print(math.pi*(float(input("Enter the radius\n"))**2))