# Numerical Data Types
# ints, long, float, complex
# These are numerical types which can use numerical operators

# complex and long we don't uses these these much
# complex are built in with imaginary numbers
# longs are just integers of unlimited size

# int and float
# int a whole number
# float a number with decimals

# int
my_int = 10
print(my_int)
print(type(my_int))

# float
my_float = 10.2
print(my_float)
print(type(my_float))

# operators - add, subtract, divide, multiply, and modulus
num1 = 12
num2 = 21

print(num1 + num2)
print(num1 - num2)
print(num1 / num2)
print(num1 * num2)

# modulus returns the remainder
print(10 % 3)
# --> 3*3 = 9, 1 remainder

# removes decimals
print(20 // 3)

# comparision operator --> boolean values
# ==  - equating things on both sides
# < / > - bigger and smaller than
# <= - smaller than or equal to
# >= - bigger than or equal to
# != - not equal to
# is - equates if something is something
# is not - equates if something is not

my_variables = 10
my_variables2 = 13

print(my_variables == my_variables2)
print(my_variables == 10)

print(my_variables < my_variables2)
print(my_variables > my_variables2)
print(my_variables <= my_variables2)
print(my_variables >= my_variables2)

# Booleans
# Only comes in True or False
# is - equates if something is something
# is not - equates if something is not
print(my_variables is 13)
print(my_variables is not 13)

# None is an appsence of values
print(None)
print(type(None))

print(0 == None)

# operators, logical & and logical Or

a_var = True
b_var = False

# for &, both sides should be True for return to be True
print(a_var & True)
print(a_var & False)

# for or, only one side need to be True for return to be True
print(' this will be true>>>')
print(True or False)
james = 'sitting'
print(james == 'sitting' or 10 > 2000)



