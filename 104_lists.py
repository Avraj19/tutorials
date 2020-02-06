# List

# Defining and creating a list
# lable = []
carzy_landlord = []

# We can dynamically define a list
# or re-define a list
carzy_landlord = ['Mr Richards', 'Raj', 'Mr shirik', 'Zmem', 'Zemmunm' ]

# List are organised using index
# To access lable[index number]
print(carzy_landlord[1])

# We can also redfine at a specific index
carzy_landlord[4] = 'Alice'
print(carzy_landlord)

# Print the last arg
print(carzy_landlord[-1])

# Another way is to get the length and make it into an index
length_list = len(carzy_landlord)
last_index = length_list -1
print(carzy_landlord[last_index])

# Adding an arg into list
# .append(obj)
carzy_landlord.append('Lana')

# insterting arg in a specific index
carzy_landlord.insert(0, 'Mr, Catlady')

# Removing items form list
# .remove(arg)
carzy_landlord.remove('Alice')

# Removing using index
# .pop()
carzy_landlord.pop() # when there is nothing in the brackets, it remove the last arg
carzy_landlord.pop(0)# can also be used to remove from specifice index

# We can have mixed data list
hybrid_list = ['JSON', 'Jason', 13, 53, [1,2] ]
print(hybrid_list)

# Tuple
# Imutable List
my_tuple = (2, 'hello', 22, 'more valuse')
print(my_tuple)

# Accessing the characters within a tuple
print(my_tuple[1][0]) # will print from index 1, the index

# range slicing
print(carzy_landlord[0:1]) # select the range 0 ot 1 but 1 is not included

example_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# jumping/slicing
# syntax [N:M:O]
# N - starting index
# M - where to end, if not add it will run till the end
# O - number of indexes to jump

print(example_list[1:9:3])


carzy_landlord = ['Raj', 7448927379, 'Mr shirik', 2892493803,  'Zmem', 2892472997]
