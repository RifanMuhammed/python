def checknum():
    num=input("enter mobile number ")
    length=len(num)
    print(length)
    if length==10:
        if num[0]==('7') or num[0]==("8") or  num[0]==("9"):
            print("number is valid")
        else:
            print("not valid")
checknum()