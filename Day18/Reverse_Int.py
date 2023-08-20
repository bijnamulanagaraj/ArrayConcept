# Write a program to reverse an integer in Python.
#Enter a number: 12345
#Reverse of the number: 54321

number = int(input("Enter a number:"))

str_cov = str(number)

reverse_num = str_cov[::-1]

int_cov = int(reverse_num)

print(int_cov)

