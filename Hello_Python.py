name = input('What is your name? ')
birthday_month = input('What month were you born in ')
print(f'Hello, {name}!')

if birthday_month.lower() == 'january':
    print('Happy birthday month!')

print(f'There are {len(name)} letters in your name') # can put simple expressions in format strings

number_of_classes = input('How many classes are you taking this semester? ')