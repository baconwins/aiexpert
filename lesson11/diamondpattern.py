
norows=6
half= norows//2
space= half-1
for row in range(1,half+1,1):
    for s in range(1,space+1):
        print(" ",end="")
    space= space-1
    for col in range(2*row-1):
        print("*", end="")
    print("")
space=1
for row in range(1,half,1):
    for s in range(1,space+1):
        print(" ",end="")
    space= space+1
    for col in range(1,2*(half-row)):     
        print("*", end="")
    print("")