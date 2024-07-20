name=input("Please enter your name : ")

print("Hello",name)
message="""
How may i help you sir/mam!

Please select any of them option
Type 1 >>>> CHECK BALANCE
Type 2 >>>> DEPOSIT
Type 3 >>>> WITHDRAWL """

print(message)

task=int(input("Please enter your option: "))
available_amount=5000

if(task>=1 and task<=3):
    print("Welcome to the vertual bank")
    #Check balance
    if task==1:
        print("Your available amount is :",available_amount)
        # deposit
    elif task==2:
        deposit_amount=int(input("Please enter deposit amount"))
        if deposit_amount>500:
            available_amount+=deposit_amount
            print("you have successfully deposit amount")
            print("Available amount is ",available_amount)
        else:
            print("Please enter more than 500 Rs.")
#withdrawal
    else:
        withdrawal_amount=int(input("Please enter amount to withdrawal : "))
        if withdrawal_amount>5000:
         print("Please enter less than 5000")
        else:
            available_amount-=withdrawal_amount
            print("your available_amount is :",available_amount)
else:
    print("please select valid option")
        