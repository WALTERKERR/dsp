# Hint:  use Google to find python function
from datetime import datetime
####a)
a_date_start = '01-02-2013'
a_date_stop = '07-28-2015'

def a_subtract_dates(a, b):
    datetime_start = datetime.strptime(a, "%m-%d-%Y").date()
    datetime_end = datetime.strptime(b, "%m-%d-%Y").date()
    print ((datetime_end - datetime_start).days)
## --> 937

####b)
b_date_start = '12312013'
b_date_stop = '05282015'

def b_subtract_dates(a, b):
    datetime_start = datetime.strptime(a, "%m%d%Y").date()
    datetime_end = datetime.strptime(b, "%m%d%Y").date()
    print ((datetime_end - datetime_start).days)
## --> 513


####c)
c_date_start = '15-Jan-1994'
c_date_stop = '14-Jul-2015'
def c_subtract_dates(a, b):
    datetime_start = datetime.strptime(a, "%d-%b-%Y").date()
    datetime_end = datetime.strptime(b, "%d-%b-%Y").date()
    print ((datetime_end - datetime_start).days)
## --> 7850