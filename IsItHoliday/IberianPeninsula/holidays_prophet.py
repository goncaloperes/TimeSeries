import pandas as pd
from pandas.tseries.holiday import *
from datetime import date
from fbprophet import *
from fbprophet.make_holidays import make_holidays_df

year_list = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
PTBusinessCalendar = make_holidays_df(year_list=year_list, country='PT')
ESBusinessCalendar = make_holidays_df(year_list=year_list, country='ES')
iberian = [PTBusinessCalendar, ESBusinessCalendar]
iberian_2 = pd.concat(iberian).sort_values('ds').reset_index(drop=True)

def join(h):
    return ', '.join(h.holiday)
IberianBusinessCalendar = iberian_2.groupby('ds').apply(join).to_frame(name="holiday")

dr = pd.date_range(start='2008-01-01', end='2020-02-1')
df = pd.DataFrame()
df['Date'] = dr

cal = IberianBusinessCalendar.drop('holiday', 1)
cal['Holiday Date'] = cal.index
cal = cal.reset_index(drop=True)

df['Holiday'] = df['Date'].isin(cal['Holiday Date']).astype(int)
print(df)