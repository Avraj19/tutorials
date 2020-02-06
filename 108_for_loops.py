# for loops
# iterations

# syntax

# for <placeholder> in <iteratable>:
#   block of code
#   indented lines are part of the block

cars = ['skoda Felecia Fun', 'Mustang Boss 429', 'Falt 500', 'Jaguar 420g', 'Aston Martin Vanguish']

# for car in cars:
#   print(car)
#  time.sleep(1)


# Ilterating over an dictionary
student1 = {
    'name': 'Arya Stark',
    'stream': 'Many Faces',
    'grade': '10'
}

# for key in student1:
#   print(key)
#  print(student1[key])

for key in student1:
    print(key + ': ' + student1[key])
