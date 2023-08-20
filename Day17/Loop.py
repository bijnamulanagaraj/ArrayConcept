word = input("Enter the word:")
index = int(input("Enter index:"))

char = word[index]

for j in word:
    if j == char:
        continue
    print(j,end="")