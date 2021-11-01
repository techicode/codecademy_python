# declare a list
list_number = [1, 2, 3, 4, 5]

# list methods

# append
garden = []
garden.append('tomato')

# another way is just using plus concatenation
garden += ['carrot', 'potato']
print(garden)  # ['tomato', 'carrot', 'potato']

# modify a element of a list
garden[0] = 'apple'
print(garden)  # ['apple', 'carrot', 'potato']

# remove a element of a list
garden.remove('carrot')
print(garden)  # ['apple', 'potato']

# multidimensional list
garden = [['tomato', 'carrot'], ['potato', 'cucumber']]
print(garden)  # [['tomato', 'carrot'], ['potato', 'cucumber']]

# replace element from multi-dimensional list
garden[0][0] = 'apple'
print(garden)  # [['apple', 'carrot'], ['potato', 'cucumber']]

# append element to multi-dimensional list
garden[0].append('pear')
print(garden)  # [['apple', 'carrot', 'pear'], ['potato', 'cucumber']]
