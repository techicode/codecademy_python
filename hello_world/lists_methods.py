# insert()
# first parm is the index, second is the value
store_line = ["Karla", "Maxium", "Martim", "Isabella"]
store_line.insert(2, "Vikor")

# pop()
# removes the last item in the list / optional parameter is the index /  returns the value of the deleted item
deleted = store_line.pop(0)     # remove the first item and store it in deleted

# range()
# returns a list of numbers from 0 to the number specified
numbers = range(10)
print(list(numbers))    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# range with 2 parameters
another_numbers = range(5, 10)
print(list(another_numbers))    # [5, 6, 7, 8, 9]

# range with 3 parameters
yet_another_numbers = range(5, 10, 2)
print(list(yet_another_numbers))    # [5, 7, 9]

# length of a list
print(len(store_line))    # 4
