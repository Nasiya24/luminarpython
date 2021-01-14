num=int(input("enter the number"))
low=int(input("enter the low"))
upper=int(input("enter the upper"))
for i in range(1,(upper+1)):
    if i**num in range(low,upper): #i=1,so 1 in range(8,30)
        print(i**num)
    else:
        pass