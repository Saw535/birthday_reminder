from datetime import datetime, timedelta

users = [
    {'name': 'John', 'birthday': datetime(1990, 5, 1)},
    {'name': 'Jane', 'birthday': datetime(1995, 4, 29)},
    {'name': 'Bob', 'birthday': datetime(1985, 5, 1)},
    {'name': 'Alice', 'birthday': datetime(1992, 5, 2)},
    {'name': 'Charlie', 'birthday': datetime(1988, 5, 3)},
    {'name': 'David', 'birthday': datetime(1997, 5, 4)},
    {'name': 'Eve', 'birthday': datetime(1983, 5, 5)}
]

def get_next_weekday_date(date, weekday):
    days_to_add = (weekday - date.weekday()) % 7
    if days_to_add == 0:
        days_to_add = 7
    return date + timedelta(days=days_to_add)

def get_birthdays_per_week(users):
    today = datetime.today()
    next_monday = get_next_weekday_date(today, 0)

    date_list = [next_monday + timedelta(days=i) for i in range(7)]
    birthday_dict = {date: [] for date in date_list}

    for user in users:
        birthday = user['birthday'].replace(year=today.year)

        # якщо день народження припадає на вихідний, він переноситься на наступний робочий день
        if birthday.weekday() > 4:
            birthday = get_next_weekday_date(birthday, 0)

        for date in date_list:
            if date.day == birthday.day and date.month == birthday.month:
                birthday_dict[date].append(user['name'])

    for date in date_list:
        print(f"{date.strftime('%A')}: {', '.join(birthday_dict[date])}")

get_birthdays_per_week(users)