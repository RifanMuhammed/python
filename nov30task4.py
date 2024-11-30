def checkupperlower():
    str=input("enter string:")
    upper=0
    lower=0
    for i in str:
        if i.isupper():
            upper+=1

        elif i.islower():
            lower+=1
        

    print("No. of upper case letters=",upper)
    print("No. of lower case letters=",lower)
checkupperlower()