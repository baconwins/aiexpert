#Define a function to find a cube and define another function which let execute the cube function if the number is divisible by 3
def cube(number):
    return number*number*number
def divisible(number):
    c= cube(number)
    if c%3==0:
        print(f"{number} is divisible by 3.")
    else:
        print(f"{number} is not divisible by 3.")
print(divisible(5))