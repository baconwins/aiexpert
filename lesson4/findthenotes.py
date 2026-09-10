# Write a program to calculate the number of notes in the given amount?
amount= int (input("Enter your amount here!"))
notesof100= amount//100
notesof50= (amount%100)//50
notesof10= ((amount%100)%50)//10
print ("notesof100=", notesof100)
print ("notesof50=", notesof50)
print ("notesof10=", notesof10)
