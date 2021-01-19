lst=[10,11,12,13,14,15,16,17]
evenlist=list()
oddlist=list()
for num in lst:
    if(num%2==0):
        evenlist.append(num)
    else:
        oddlist.append(num)

print(oddlist)
print(evenlist)
teven=sum(evenlist)
print(teven)
evenlist.append(teven)
print("oddsum",sum(oddlist))
print("evensum",sum(evenlist))

