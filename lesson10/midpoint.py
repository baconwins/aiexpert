number= 15735
n2=number
digit=0
while number!=0:
    number= number//10
    digit=digit+1
midpoint=digit//2+1
count=1
print(midpoint)
number=n2
while number!=0:
    if count==midpoint:
        print(number)
        break
    count=count+1
    number= number//10
    print(number)