TEMP=float(input("enter temperature:"))
CF=input("Is this in (C)elsius or (F)ahrenheit?")
if CF=="C":
    f=(9/5*TEMP)+32
    print(TEMP,"Celsius is",f,"Fahrenheit")
elif CF=="F":
    c=5/9*(TEMP-32)
    print(TEMP,"Fahrenheit is",c,"celsius")
else:
    print("invalid command")

