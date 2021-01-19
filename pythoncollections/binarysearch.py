lst=[10,9,5,6,34,8]
lst.sort()
flag=0
#step1 is sorting in binary search
#


low=0
upp=len(lst)-1
element=int(input("enter element for search"))
while(low<=upp):
    mid=(low+upp)//2
    if(element>lst[mid]):
        low=mid+1
    elif(element<lst[mid]):
        upp=mid-1
    elif(element==lst[mid]):
        flag+=1
        break
if(flag==0):
    print("element not found")
else:
    print("element found")
