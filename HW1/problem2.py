import datetime
import time
import calendar

b = datetime.date(1999, 3, 24)
print(b)

b_y = my_birthdate.year
print(b_y)


b_m = b.month
print( b_m)


b_d = b.day
print( b_d)

b_w = b.isoweekday()
print(b_w)


n_b = b + datetime.timedelta(days = 365*24, hours = 24*6)
t = datetime.date.today()
t_b = n_b - t
print( t_b)


cal = calendar.month(2017, 5)
print(cal)


d = datetime.timedelta(days = 1)
y = datetime.datetime.today() - d
print(y)


d2 = datetime.timedelta(days = 2)
t = yesterday + d2
print(t)


d3 = datetime.timedelta(days = 3)
td = yesterday - d3
print(td)