lst=[2,5,6,7]
#[18,15,14,13]

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


