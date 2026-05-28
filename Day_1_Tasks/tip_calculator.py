# Calculates total bill using current bill amount and tip given

def calculate_tip(bill, tip_percent):
    tip_amount = (bill*tip_percent)/100
    total_bill = bill + tip_amount
    return {'Tip Amount' : tip_amount, 'Total Bill' : total_bill}

print(calculate_tip(1400,2))

print(calculate_tip(100,10))
print(calculate_tip(4389,8))

#diff. between return and print
# return is used for sending the value out of the function while closing the function, 
#that can be stored, printed or used for further calculation, it can be of any type

# while print is used for printing the value or string in the user window
# It does not save the value for the program