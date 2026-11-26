print("=========POS SHOP=============")

correct_pin = "python1234"
Available_amount = 500

while True:
    user_pin = input('Enter pin: ')
    
    if user_pin != correct_pin:
        print('Incorrect pin\nEntry rejected')
    else:
        print("successful login")
        break     
    
while True:
    user_amount = int(input("Enter amount: "))
        
    if user_amount > Available_amount:
        print ("Insufficient funds\nTry again")
    else:
        Available_amount -= user_amount
        print("Payment Approved")
        print(f"You have ${Available_amount} left")
        break
exit("Thank you for your patronage")