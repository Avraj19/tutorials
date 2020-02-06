student1 ={
    'Name': 'Morty',
    'Stream': 'Universal Quest',
    'Grades': 12
}

student2 ={
    'Name': 'Summer',
    'Stream': 'Terrestial Quest',
    'Grades': 20
}

student_list = [student1, student2]

#print(student_list[1])

student_dict ={
    'Student1': student1,
    'Student2': student2
}

# Use the list to print the individual student name
# student_list[index][key]
print(student_list[0]['Name'])
print(student_list[1]['Name'])

# use the dictionary to print individual student name
# student_dict[dict name][key]
print(student_dict['Student1']['Name'])
print(student_dict['Student2']['Name'])

