number=int(input("enter number for multiplication  table:"))
print("TABLE OF",number)
for i in range(1,13):
    print(i,'\t'"*",'\t',number,'\t',"=",number*i)