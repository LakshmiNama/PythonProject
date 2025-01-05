# problem to find maximum between two

number1 = float(input("Enter first number\n"))
number2 = float(input("Enter second number\n"))

# print("The maximum of two number is", max(number1,number2))

if number1 > number2 :
    print(number1, "is greater")
else:
    print(number2, "is greater")
    print(f"max of two number is {number2:.2f}")