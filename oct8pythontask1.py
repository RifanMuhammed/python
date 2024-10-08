#Title: Simple desktop calculator using Python. Only the five basic arithmetic operators.

num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
num3=int(input("enter third number"))
ADDITION=num1+num2
print("The sum of num1 and num2 is:",ADDITION)
SUBTRACTION=num1-num2
print("The difference when num2 is subtracted from num1 is:",SUBTRACTION)
MULTIPLICATION=num1*num2
print("The product of num1 and num2 is:",MULTIPLICATION)
DIVISION=num1/num2
print("The quotient when num1 is divided by num2 is:",DIVISION)
MODULUS=num1//num2
print("The remainder when num1 is divided by num2 is:",MODULUS)
COMBINED_OPERATION=(num1+num2)*num3/2
print("The result of (num1 + num2) * num3 / 2 is:",COMBINED_OPERATION)
