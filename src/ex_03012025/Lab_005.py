# Take a user input a,b and calculate sum, mul, div, sub
# Calculator program


#num1 = input("Enter the number 1")
#num2 = input("Enter the number 2")

#num1 and num2 is of type str
#convert it to integer

num1 = int(input("Enter the number 1"))
num2 = int(input("Enter the number 2"))

print(type(num1))
print(type(num2))

print("Sum of two numbers is", num1+num2)
print("Subtraction of two numbers is", num1-num2)
print("Multiplication of two numbers is", num1*num2)
print("Division of two numbers is", num1/num2)
print("Maximum of two numbers is", max(num1,num2))
print("Power of num1 to num2", pow(num1,num2))