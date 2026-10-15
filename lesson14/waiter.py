'''Let's create a function total_calc() that helps us calculate and print out the total amount paid at a restaurant. Given a bill amount and the percentage of the bill amount you decide to pay us a tip (tip_perc ), this function calculates the total amount you should pay.'''
def total_calc(amount,tip_percent):
    tipamount=(amount*tip_percent)//100
    totalbill=amount+tipamount
    return totalbill
print(total_calc(1000,10))