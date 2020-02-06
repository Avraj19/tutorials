# strings
# These ara a list of characters put together in a list.

# my_string = "Amazing grillled Fish"
# print(my_string)
# print(type(my_string))

# joining of two strings
# first_name = "Avraj"
# last_name = "Singh"
# print(first_name +' '+ last_name)

# Interpolation
# you inject a string into another string
# name = "Lana"
# welcome_message = "Welcome to the DDDDAAAANGERSZZZONE"

# print(f"Welcome {name}, to the DDDAAAANNNNGGGGEEERRZZZONNE!!!!")

# special method for strings
my_sring = "Hello my name is ..."

# .count()
print(my_sring.count('i'))
print(my_sring.count(' '))

# .strip() removes trailing white spaces
print(my_sring)
print(my_sring.sprip())

# len() - function not a method
print(len(my_sring))
print(len(my_sring.split()))

# .capitalize()
print(my_sring.split().capitalize())

# separates the string in several strings,
# and returns it into a list.
print(my_sring.split())



# .upper()everything in caps
print(my_sring.upper())

# .lower everything in lower case
print(my_sring.lower())
