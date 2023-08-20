# Armstrong Number
# For eg: 153, is an Armstrong number because it has 3 digits, and 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

num = int(input("Enter number:"))

num_str = str(num)

num_len = len(num_str)

sum = 0
for i in num_str:
    power = int(i) ** num_len
    sum += power

if num == sum:
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")