array = [4,7,8,5,4,5]


for i in array:
    if array.count(i) == 2:
        continue
    else:
        print(i,end=" ")


