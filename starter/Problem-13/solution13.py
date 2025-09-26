
dict1 = {'age': 13, 'id': 12, 'address': 'Banani', 'course': 'Python'}

dict2 = {'address': 'Rupnagar', 'id': 25, 'course': 'MERN'}

common_items ={}


for key in dict1:
    if key in dict2:
        common_items[key] = [dict1[key], dict2[key]]
print("Common items : ", common_items) # {'id': [12, 25], 'address': ['Banani', 'Rupnagar'], 'course': ['Python', 'MERN']}