def right_triangle():
    side1=int(input("enter first side"))
    side2=int(input("enter second side"))
    side3=int(input("enter third side"))
    sides=[side1,side2,side3]
    sides.sort()
    if sides[2]**2==sides[0]**2+sides[1]**2:
        print("right triangle")
    else:
        print("not right triangle")
right_triangle()



