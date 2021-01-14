num=int(input("enter the number"))
while(num>0):
    rev=num%10
    print(rev,end="") #to print on same line
    num=num//10