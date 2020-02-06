# Dictionaries
# we need to know where our crazy landlord lives, we need more information


# Dictionaries are organized using key value pairs
# like a real dictionary
# looking up 'omipresent'.

# Define a simple dictionary
# sytax
# my_dictionary = {
#                   'key': 'value'
#                    'other keys': 'values'}


# create one dictionary
my_carzy_x_landload = {'name': 'Filipe', 'phone': '07448929820', 'address': 'Hayes, London'}

# Create or add one key value pair

# Read one whole dictionary
print(my_carzy_x_landload)

# Read the value of one key in a dictionary
print(my_carzy_x_landload['phone'])

# Update the value in a key
my_carzy_x_landload['phone'] = '+44 07446879233'

# To remove or pop one key and value
my_carzy_x_landload.pop('address')

# Getting all the key out only
key = my_carzy_x_landload.keys()
print(key)

# Getting all the values out
values = my_carzy_x_landload.values()
print(values)
