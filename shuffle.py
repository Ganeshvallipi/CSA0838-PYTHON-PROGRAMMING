li=[]
lj=[]
n11=int(input("enter 11 range:"))
if (n11<=0):
    print("Error")
else:
    for i in range (n11):
        i=int(input("enter:"))
        li.append(i)
n12=int(input("enter the 12 range:"))
if (n12<=0):
    print("Error")
else:
    for j in range (n12):
        j=int(input("enter:"))
        lj.append(j)
l=[]
l=li+lj
l.sort()
print("List:",l)
