# Program to find Maximum between 3 numbers

number1 = int(input("Enter first number\n"))
number2 = int(input("Enter Second number\n"))
number3 = int(input("Enter third number\n"))

if number1 > number2 and number1 > number3:
    print(number1,"is greater")
elif number2 > number1 and number2 > number3:
    print(number2, "is greater")
elif number3 > number1 and number3 > number2:
    print(number3, "is greater")

if number1 < number2 and number1 < number3:
    print(number1,"is smaller")
elif number2 < number1 and number2 < number3:
    print(number2, "is smaller")
elif number3 < number1 and number3 < number2:
    print(number3, "is smaller")

result = max(number1, number2, number3)
result1 = min(number1, number2, number3)

print("Greater number among given is", result)
print("Greater number among given is", max(number1, number2, number3))
print("Smaller number among given is", result1)