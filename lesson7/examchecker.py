'''Write a program to check whether the student can take an exam or not. Students will be allowed only in two conditions: If they have a medical cause (‘Y’ for yes and ‘N’ for no). If yes, then they will be allowed. If No, then check attendance If attendance is above 75, then allowed; otherwise, not allowed.'''
eligibility= input("enter Y for yes if you have medical cause, N for no if not.")
if eligibility=="Y":
    print("you can enter")
else:
     A= int(input("Enter your attendance"))
     if A>75:
          print("you can enter")
     else:
          print("you cannot enter")