for row in range(1,6,1):
    for space in range(1,6-row,1):
        print(" ", end="")
    for star in range(1,row+1,1):
        print("*", end="")
    print("")



