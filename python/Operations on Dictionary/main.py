my_dict = {}

my_dict = { 1:'apple', 2:'banana'}

my_dict = { 'name':'John', 1:[2, 4, 3]}

my_dict = { 'name':'Jack', 'age': 26}

print(my_dict['name'])
print(my_dict.get('age'))

my_dict['age'] = 27
print(my_dict)

my_dict['address'] = 'Downtown'
print(my_dict)

my_dict.pop('age')
print(my_dict)

print("address : ", my_dict.pop('address'))

my_dict.clear()
print(my_dict)