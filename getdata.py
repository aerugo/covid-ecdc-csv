# Thanks joshuagladwin for import code

import pandas as pd
from pprint import pprint 
from datetime import date, timedelta
import xlrd

today = date.today()
day = today.strftime("%d")
month = today.strftime("%m")

url  = "https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-2020-{}-{}.xls.xlsx".format(month, day)

df = pd.read_excel(url)

def read_date(date):
    return xlrd.xldate.xldate_as_datetime(date, 0)

df['DateRep'] = pd.to_datetime(df['DateRep'].apply(read_date), errors='coerce')
df.set_index('DateRep', inplace=True)
df = df.sort_index()

pprint(df.to_csv())