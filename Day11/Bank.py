user_pin_number = input("enter pin number:")
saving_balance = 5000


if user_pin_number == '1191':
    user_input = input("Enter Something:")
    if user_input == 'bal_enquiry':
        print(saving_balance)

    elif user_input == "withdraw":
        amount = int(input("Enter Amount:"))
        if amount < saving_balance or amount == saving_balance:
            remaining_balance = saving_balance - amount
            print(remaining_balance)
        else:
            print("not sufficient balance")

    elif user_input == "credit":
        amount = int(input("Enter Amount:"))
        saving_balance = saving_balance + amount
        print(saving_balance)



user_pin_number = input("Enter pin number:")

if user_pin_number == '1191':
    user_input = input("Enter Something:")
    if user_input == "withdraw":
        amount = int(input("Enter Amount:"))
        if amount < saving_balance or amount == saving_balance:
            remaining_balance = saving_balance - amount
            print(remaining_balance)
        else:
            print("not sufficient balance")

