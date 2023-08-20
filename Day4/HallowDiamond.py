num = int(input("Enter The Num:"))

for i in range(1,num+1):
    if i == 1:
        print(" " * (num - i) + "*")
    else:
        left_spaces = " " * (num - i)
        hallow_spaces = "  " * (i - 1)
        print(left_spaces + "*" + hallow_spaces + "*")

for j in range(num-1):
    if j == 3:
        print(" " * (j + 1) + "*")
    else:
        left_spaces = " " * (j + 1)
        hallow_spaces = "  " * (num - j - 2)
        print((left_spaces + "*" + hallow_spaces + "*"))
