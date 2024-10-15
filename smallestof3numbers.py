num1=int(input("enter first number"))
num2=int(input("enter second number"))
num3=int(input("enter third numbr"))
if(num1<num2 and num1<num3):
    print("num1 smallest")
elif(num2<num1 and num2<num3):
    print("num2 smallest")
elif(num1==num2==num3):
    print("numbers are same")
else:
    print("num3 smallest")
