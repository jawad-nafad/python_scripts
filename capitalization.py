first_value = ' FIRST challenge         '
second_value = '- second challenge -'
third_value = 'tH IR D-C HALLE NGE'
fourth_value = 'fourth'
fifth_value = 'fifth'
sixth_value = 'sixth'


#firt challenge
first_value = first_value.strip().title()
first_value = f'{first_value:^30}'
print(first_value)
#second challenge
second_value = second_value.replace('-','').strip().capitalize()
print(second_value)
#third challenge
third_value = third_value.lower()
third_value = third_value.replace(' ','').replace('-',' ').capitalize()
third_value = f'{third_value:^45}'
print(third_value)

# Fourth challenge - use only the print() function (no f-strings)
print(fourth_value,fifth_value,sixth_value,sep='#',end='!')

# Fifth challenge - use only a single print() function.  Create tabs and new lines using
print(f'\n\t{fourth_value}\n\t{fifth_value}\n\t{sixth_value}')
