person = {}

person['first_name'] = 'elizabeth'
person['last_name'] = 'tchako'
person['age'] = '21'
person['city'] = 'schenectady'

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])


fav_num = {
    'rina' : 5,
    'elizabeth' : 72,
    'stevie' : 3,
    'joey' : 52,
}

print(fav_num)

data_str = {
    'lists' : 'uses []',
    'tupples' : 'uses ()',
    'dicts' : 'uses {:}',
    'sets' : 'uses {}',
    '.get()' : 'take 2 argument, second optional',
    '.values()' : 'take no arguments,\nand returns the sequence values',
    '.keys()' : 'takes no arguments,\nand returns the sequence keys\nand isnt neccesary in for loop since keys is the default for loops\nmethod exist because it can be used outside for loops',
    '.items()' : 'tales no argument,\nand returns the sequence key-value pairs'
}

for datastr, symbol in data_str.items():
    print(f"\nI have learned {datastr}")
    print(f"Which: {symbol}")




#print(f"I have learned about list, which use: {data_str['list']}\nI have learned about tupples, which use: {data_str['tupple']}\nI have learned about dictionaries, which use: {data_str['dict']}\n")