num = int(input())

python_students = []

duplicate_remove = []

result = []

order = []

for i in range(1, num + 1):
    name = input()
    value = input()
    python_students.append([name] + [value])

for j in python_students:
    if j[1] not in duplicate_remove:
        duplicate_remove.append(j[1])
    else:
        result.append(j[1])

duplicate_remove.sort()

if len(result) == 1:
    for j in python_students:
        if result[0] == j[1]:
            order.append(j[0])
else:
    second_value = duplicate_remove[1]
    for m in python_students:
        if m[1] == second_value:
            order.append(m[0])

order.sort()
for student in order:
    print(student)