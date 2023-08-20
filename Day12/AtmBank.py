user_pin_number = input("enter pin number:")
saving_balance = 5000

error = ""

try:
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
                error = "not sufficient balance"

        elif user_input == "credit":
            amount = int(input("Enter Amount:"))
            total_amount = saving_balance + amount
            print(total_amount)
except:
    error