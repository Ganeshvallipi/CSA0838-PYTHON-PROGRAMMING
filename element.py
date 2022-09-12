E=[]
L=[]
T = int(input("Range T : "))
for i in range (T):
    e=int(input("L : "))
    E.append(1)
sum=0
max=0
for i in range(T):
   sum+=E[i]-L[i]
   Max=max(Sum,Max)
print("output",Max)
    
