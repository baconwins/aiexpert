#Write a program to make a calculator : For making a calculator create four functions add, subtract, multiply, divide. Ask for a choice from users which operation they want to perform. Take user input whatever operation they want to perform And call that function accordingly.
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
choice=input("enter 1 for add, 2 for subtract, 3 for multiply, and 4 for divide.")
if choice=="1":
   sum= add(5,6)
   print(sum)
elif choice=="2":
    sum= subtract(12,4)
    print (sum)
elif choice=="3":
    sum= multiply(5,6)
    print(sum)
elif choice=="4":
    sum=divide(12,4)
    print(sum)
else:
    print("invalide choice")