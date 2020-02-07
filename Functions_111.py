# functions

# function do one thing and do it well
# function should be small and easily testable.
# make code more readable, maintainable and testable
# runs a block of code when called
# functions are like machines, they take in input and do work on then output#
# do not use print inside a function
#

# DRY
# Don't Repeat Yourself

# syntax

# dif <name>(args)
#   block of code
#       can return out


def say_hello():
    return 'hello'


# print(say_hello()) #calling function

def full_name(f_name, l_name):
    return f_name + ' ' + l_name

# print(full_name('Avraj', 'Singh'))

def welcome_message(f_name, l_name):
    full_name_str = full_name(f_name, l_name)
    welcome_str = say_hello()
    return welcome_str + ' ' + full_name_str


