str=input("enter string to be checked:")
vowals="AEIOUaeiou"
count=0
for i in str:
    if i in vowals:
        count+=1
print("NUMBER OF VOWELS=",count)