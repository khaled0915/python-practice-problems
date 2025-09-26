data_list = [13, 24, 'Karim', {'name': 'guru'}, 45, 17]

only_ages=[]

for item in data_list:
    if type(item) == int:
        only_ages.append(item)


print(only_ages) # [13, 24, 45, 17]