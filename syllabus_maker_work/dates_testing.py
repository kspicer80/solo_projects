import datetime
import numpy as np
from dateutil.rrule import rrule, WEEKLY, MO, DAILY
from datetime import date, timedelta
from datetime import datetime
import pandas as pd

start = date(2022, 8, 22)
end = date(2022, 12, 16)
dates_list = []

#for date in rrule(WEEKLY, dtstart=start, byweekday=MO, count=3):


for date in rrule(DAILY, interval=2, byweekday=range(5), dtstart=start, until=end):
    dates_list.append(str(date))






#dates_df = pd.DataFrame(dates_list, columns=['date'])
days_of_the_week = ['Monday', 'Wednesday', 'Friday']

days_and_dates = list(zip(dates_list, days_of_the_week))
print(days_and_dates)

 