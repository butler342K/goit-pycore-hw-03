# Common decoration
def print_title(title):
    raw_length = 150
    name = 'Vitaly Kichenko'
    theme = 'Homework GoIT'
    print(' ')
    print('*'*raw_length)
    print(f'**{theme:^{raw_length-4}}**')
    print('**' + ' '*(raw_length-4) +'**')
    print(f'**{name:^{raw_length-4}}**')
    print('**' + ' '*(raw_length-4) +'**')
    print(f'**{title:^{raw_length-4}}**')
    print('*'*raw_length)
    print(' ')

def print_footer(message):
    raw_length = 150
    print('='*raw_length)
    print(f'{message:>{raw_length}}')
    print(' ')

# Task 1: Days from today to the date
def get_days_from_today(date):
    from datetime import datetime

    today = datetime.now()
   # today = datetime(2021,5,5) # check for correct result from the task. Must be -157
    target_date = datetime.strptime(date, '%Y-%m-%d')
    delta = today - target_date
    return delta.days

# Task 2: Generate a list of unique lottery numbers
def get_numbers_ticket(min, max, quantity):
    import random
    random_set = set()

    if min <1 or max > 1000:
        raise ValueError('Min value must be >= 1 and Max value must be <= 1000') 
    elif min>= max:
        raise ValueError('Min value must be less than Max value')

    if quantity < 1 or quantity > (max - min + 1):
        raise ValueError('Quantity must be between Min and Max values')

    while len(random_set) < quantity:   # add unique numbers to the set until it reaches the required quantity
        random_set.add(random.randint(min, max))

    tickets_numbers = list(random_set)
    tickets_numbers.sort()
    return tickets_numbers


# Task 3: Normalize phone number
def normalize_phone(phone_number):
    import re
    phone_number = re.sub(r'\D', '', phone_number)  # remove all non-digit characters
    if len(phone_number) < 10:
        raise ValueError('Wrong number. Phone number must contain at least 10 digits')
    if phone_number[0] == '0': # if first digit is '0'
        phone_number = '+38' + phone_number 
    elif phone_number.find('38', 0, 2) > -1:  # if phone number starts with '38. Redundant conditiion, but it's can be useful for other international numbers'
        phone_number = '+' + phone_number  
    else:
        phone_number = '+' + phone_number 
    return phone_number

# Task4: Upcoming birthdays
def get_upcoming_birthdays(users):
    from datetime import datetime, date, timedelta
    period_days = 7  # period for upcoming birthdays
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
        birthday_this_year = birthday.replace(year=today.year)  
        # if birthday was before today, set it to next year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_until_birthday = (birthday_this_year - today).days
        if days_until_birthday <= period_days:
            if datetime.weekday(birthday_this_year) == 5:  # if birthday is on Saturday, move it to Monday
                birthday_this_year += timedelta(days=2)
            elif datetime.weekday(birthday_this_year) == 6:  # if birthday is on Sunday, move it to Monday
                birthday_this_year += timedelta(days=1)
            congratulation_date = datetime.strftime(birthday_this_year, '%Y.%m.%d')
            upcoming_birthdays.append({'user':user['name'], 'congratulation_date':congratulation_date})

    return upcoming_birthdays

# Main execution. Output results

print_title('Theme 4')

print('Task 1: Days from today to the date')
days = get_days_from_today('2021-10-09')
print(f'Days from the date 2021-10-09 to today: {days} days')
print(' ')

print('Task 2: Generate a list of unique lottery numbers')
lottery_numbers = get_numbers_ticket(10, 12, 1)
print(f'Ваші лотерейні числа: {lottery_numbers}')
print(' ')

print('Task 3: Normalize phone number')
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
print(' ')

print('Task 4: Upcoming birthdays')
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Alex Reva", "birthday": "1992.06.15"},
    {"name": "Forest Gump", "birthday": "1988.06.21"},
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
print(' ')

print_footer('End of Homework')