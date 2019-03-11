import datetime


def print_header():
    print('--------------------')
    print('    Birthday App    ')
    print('--------------------')


def get_user_birthday():
    print('When were you born?')
    year = int(input('Year [YYYY]'))
    month = int(input('Month [MM]'))
    day = int(input('Day [DD]'))

    birthday = datetime.date(year, month, day)
    return birthday


def compute_days_between(original_birthdate_date, today_date):
    birthday_this_year = datetime.date(today_date.year, original_birthdate_date.month, original_birthdate_date.day)

    delta = birthday_this_year - today_date
    return delta.days


def print_birthday_info(days):
    if days < 0:
        print('Your birthday was {} days ago! happy belated'.format(days))
    elif days > 0:
        print('Your birthday is in {} days! Plan something fun'.format(days))
    else:
        print('HAPPY BIRTHDAY!')


def main():
    print_header()
    bday = get_user_birthday()
    today = datetime.date.today()
    number_of_days = compute_days_between(bday, today)
    print_birthday_info(number_of_days)


main()