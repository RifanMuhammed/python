'''Author:Rifan Muhammed
   dATE:1-10-2024
   Python program to print roll no and cgpa'''
name=input("enter the name of the student:")
roll_number=int(input("enter roll number"))
roll_number=roll_number+1
cgpa=float(input("enter cgpa"))
percentage=cgpa*10
print("cgpa percentage:",percentage,'%')
print(name,roll_number)
