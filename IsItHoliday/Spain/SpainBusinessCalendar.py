import pandas as pd
from pandas.tseries.holiday import *
from pandas.tseries.offsets import CustomBusinessDay
from datetime import date

#General Holidays for Spain
class SpainBusinessCalendar(AbstractHolidayCalendar):
   rules = [
     #Spain - If one holiday is on a Sunday, each Autonomous Community can change it to a Monday.
     Holiday('Año Nuevo', month=1, day=1, observance=sunday_to_monday),
     Holiday('Epifanía del Señor', month=1, day=6, observance=sunday_to_monday),
     Holiday('Viernes Santo', month=1, day=1, offset=[Easter(), Day(-2)]),
     Holiday('Día del Trabajador', month=5, day=1, observance=sunday_to_monday),
     Holiday('Asunción de la Virgen', month=8, day=15, observance=sunday_to_monday),
     Holiday('Día de la Hispanidad', month=10, day=12, observance=sunday_to_monday),
     Holiday('Todos los Santos', month=11, day=1, observance=sunday_to_monday),
     Holiday('Día Constitución', month=12, day=6, observance=sunday_to_monday),
     Holiday('Inmaculada Concepción', month=12, day=8, observance=sunday_to_monday),	    
     Holiday('Navidad', month=12, day=25, observance=sunday_to_monday)
   ]


dr = pd.date_range(start='2008-01-01', end='2020-02-1')
df = pd.DataFrame()
df['Date'] = dr

cal = SpainBusinessCalendar()
holidays = cal.holidays(start=dr.min(), end=dr.max())

df['Holiday'] = df['Date'].isin(holidays).astype(int)
print(df)
