

for number in range(2,21):
    isprime=True
    for i in range(2,number):
        if number%i==0:
            isprime=False
            break
    if isprime==True:
        print(number)