prime=int(input("enter number to be checked:"))
for i in range(2,prime):
    if prime%i==0:
        print("NOT PRIME NUMBER")
        break
    else:
        print("PRIME NUMBER")
        break

