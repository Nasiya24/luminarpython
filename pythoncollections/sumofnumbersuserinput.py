#to input the list and find sum of numbers in list except one number and print them

limit=int(input("enter limit"))
lst=list()
for i in range(0,limit):
    number=int(input("enter number"))
    lst.append(number)
#finding total of list
#total=20
#20-2=18
#20-5=15
#20-6=14
#20-7=13

out=list() #empty list
total=sum(lst)
for num in lst:
     out.append(total-num)
print(out)