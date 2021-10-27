import datetime

month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def is_leap(year):
    if year % 400 == 0 or year % 40 == 0 or year % 4 == 0:
        return True
    else:
        return False


def minus_result(first_year, second_year):
    y = first_year.year - second_year.year
    m = first_year.month - second_year.month
    d = first_year.day - second_year.day
    if d < 0:
        if second_year.month == 2:
            if is_leap(second_year.year):
                month_days[2] = 29
        d += month_days[second_year.month]
        m -= 1
    if m < 0:
        m += 12
        y -= 1
    if y == 0:
        if m == 0:
            return ('{}天'.format(d))
        else:
            return ('{}月{}天'.format(m, d))
    else:
        return ('{}岁{}月{}天'.format(y, m, d))



if __name__ == '__main__':
    dotdot = datetime.date(1951, 4, 22)
    t = datetime.date.today()
    print(minus_result(t, dotdot))
