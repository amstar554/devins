#ex1

men_retirement_age = 67
women_retirement_age = 62


year_born = int(input('what YEAR were you born? '))
month_born = int(input('what MONTH were you born? '))
day_born = int(input('what DAY were you born? '))

def get_age(y, m, d):
    current_month = 4
    current_year = 2020
    current_day = 22

    y = current_year - y
    m = current_month - m
    if m < 0:
        y -= 1
        m = 12 - abs(m)
    d = current_day - d
    if d < 0:
        d = 30 - abs(d)
    print(f' year: {y}, month: {m}, day: {d}')

get_age(year_born, month_born, day_born)

#ex3

# def describe_city(city="Reykjavik", country="Iceland"):
#     print(f'{city} is in {country}')
#
# describe_city("istanbul", "turkey")
# describe_city("tel aviv", 'Israel')
# describe_city()

#ex4

# def dislay_message():
#     sentence = "I'm learning about functions today"
#     print(sentence)
# dislay_message()