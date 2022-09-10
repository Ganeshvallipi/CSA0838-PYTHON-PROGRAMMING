denomination1=int(input("enter the 1st denomination "))
denominationnotes1=int(input("enter the 1st denomination number of notes "))
denomination2=int(input("enter the 2nd denomination "))
denominationnotes2=int(input("enter the 2nd denomination number of notes :"))
denomination3=int(input("enter the 3rd denomination "))
denominationnotes3=int(input("enter the 3rd denomination number of notes :"))
denomination4=int(input("enter the 4th denomination "))
denominationnotes4=int(input("enter the 4th denomination number of notes "))
if(denomination1==2000 or 500 or 200 or 100 and denomination2==2000 or 500 or 200 or 100 and denomination3==2000 or 500 or 200 or 100 and denomination4==2000 or 500 or 200 or 100):
    print(denominationnotes1)
    print(denominationnotes2)
    print(denominationnotes3)
    print(denominationnotes4)
    print("the total amount present in the ATM is ",(denominationnotes1*denomination1)+(denominationnotes2*denomination2)+(denominationnotes3*denomination3)+(denominationnotes4*denomination4))
else:
    print("invalid entry")


