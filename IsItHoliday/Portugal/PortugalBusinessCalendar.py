import pandas as pd
from pandas.tseries.holiday import *
from pandas.tseries.offsets import CustomBusinessDay
from datetime import date

#General Holidays for Portugal
class PortugalBusinessCalendar(AbstractHolidayCalendar):
   rules = [
     Holiday('Ano Novo', month=1, day=1),
     #Holiday('Entrudo', month=1, day=1, observance=sunday_to_monday) - it is always on a Tuesday between 3 of February and 9 of March,
     Holiday('Sexta-Feira Santa', month=1, day=1, offset=[Easter(), Day(-2)]),
     Holiday('Páscoa', month=1, day=1, offset=[Easter()]),
     Holiday('Dia da Liberdade', month=4, day=25),
     Holiday('Dia do Trabalhador', month=5, day=1),
     # Holiday('Corpo de Deus', month=1, day=1, observance=sunday_to_monday) - it is always on a Thursday between 21 of May and 24 of June,
     Holiday('Dia de Portugal', month=6, day=1),
     Holiday('Assunção de Nossa Senhora', month=8, day=15),
     Holiday('Implantação da República', month=10, day=5),
     Holiday('Todos os Santos', month=11, day=1),
     Holiday('Restauração da Independência', month=12, day=1),
     Holiday('Imaculada Conceição', month=12, day=8),
     Holiday('Natal', month=12, day=25)
   ]


dr = pd.date_range(start='2008-01-01', end='2020-02-1')
df = pd.DataFrame()
df['Date'] = dr

cal = PortugalBusinessCalendar()
holidays = cal.holidays(start=dr.min(), end=dr.max())

df['Holiday'] = df['Date'].isin(holidays).astype(int)
print(df)
