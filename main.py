def print_title(title):
    raw_length = 100
    name = 'Vitaly Kichenko'
    theme = 'Homework GoIT'
    print(' ')
    print('*'*raw_length)
    print(f'**{name:^{raw_length-4}}**')
    print('**' + ' '*(raw_length-4) +'**')
    print(f'**{theme:^{raw_length-4}}**')
    print('**' + ' '*(raw_length-4) +'**')
    print(f'**{title:^{raw_length-4}}**')
    print('*'*raw_length)
    print(' ')

print_title('Theme 4')