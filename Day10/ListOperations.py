# Creating  List
my_list = []
print("Empty List:",my_list)

my_list = [1, 2, 3, 4, 5]
print("List With Initial Values:", my_list)

# Accessing List Elements
first_element = my_list[0]
print("First Element:",first_element)

Last_element = my_list[-1]
print("Last Element", Last_element)

#Modifying List Elements
my_list[2] = 10
print("List after updating element:",my_list)

my_list.insert(3,7)
print("List after inserting element at index 3:",my_list)

another_list = [8, 9, 10]
my_list.extend(another_list)
print("List after extending with another list",my_list)

# Removing Elements from the list
my_list.remove(4)
print("List after removing element 4:", my_list)

removed_element = my_list.pop(2)
print("List after removing element at index 2", my_list)
print("Removed element:", removed_element)

removed_last_element = my_list.pop()
print("List after removing last element:", my_list)
print("Removed last element:", removed_last_element)

#clear list
my_list.clear()
print("List after clearing all elements:", my_list)

another_list = [8, 9, 10, 5, 7, 3, 9]
my_list.extend(another_list)
print("List after extending with another list:", my_list)

# Slicing List
sliced_list = my_list[1:3]
print("sliced list from index 1 to 3 (exclusive):", sliced_list)

#sub_list
sub_list = my_list[2:]
print("Sublist from index 2 till the end:", sub_list)
