items1 = dict({'Key1': 1, 'Key2': 2, 'Key3': 3, 'Key4': 4})
print(items1)

items2 = {}
items2['key1'] = 1
items2['key2'] = 2
items2['key3'] = 3

print(items2)

items2['key2'] = 'two'

print(items2)

# print(items1['key7'])

# iteration

for key, value in items1.items():
    print(f'Key: {key} value: {value} pair')