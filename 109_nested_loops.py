# looping over embedded lists

normal_list = [1, 2, 3, 4, 5]
embedded_list = [[1, 2, 3], [4, 5, 6]]

# for num in normal_list:
#   print(num * 3.5)

# for data in embedded_list:
#     print(data) # prints out list (in index 0), the second for loop runs
#     for num in data:
#         print(num)# prints out all of the list in index 0 of embedded_list

dict_data = {
    1: {'name': 'Standly Ho',
       'money': '£0.05'},
    2: {'name': 'Jeff Bezzo',
       'money': '£0.08'},
    3: {'name': 'Trump',
       'money': '£0.02'}
}

# Objective
# --> name
# --> money * 4,000,000

for key_1 in dict_data:
    # print(key_1)
    sub_dict = dict_data[key_1]
    print(sub_dict['name'])
    money_var =float(sub_dict['money'].replace('£',''))
    # for name in item:
    #     print(dict_data[item])