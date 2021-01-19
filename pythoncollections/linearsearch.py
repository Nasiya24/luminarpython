lst=[10,7,8,9,15]
number=int(input("enter number to search"))
flag=0
cnt=1
for num in lst:
    if(number==num):
        flag=1
        break
    else:
        pass

if(flag==0):
    print("element not found")
else:
    print("element found")

