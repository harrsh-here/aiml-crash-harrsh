#Even Odd number program that handles invalid input.
try:
    num = int(input('Enter a Number : '))
    if num==0:
        ("Number is Zero!")
    elif num%2==0:
        print("EVEN")
    else:
        print("ODD")
except Exception as e: 
    print('Enter a valid number!!')
    
    