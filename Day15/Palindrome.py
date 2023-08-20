name = input("Enter name:")

reversed_name = name[::-1]

print(name)
print(reversed_name)


if name == reversed_name:
    print("Palimdrome")
else:
    print("not Palindrome")