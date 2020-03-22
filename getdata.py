# Thanks joshuagladwin for import code

import pandas as pd
from pprint import pprint 
from datetime import date, timedelta
import xlrd

today = date.today()
day = today.strftime("%d")
month = today.strftime("%m")

try:
  url  = "https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-2020-{}-{}.xls".format(month, day)
  try:
    df = pd.read_excel(url)
  except:
    url  = "https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-2020-{}-{}.xlsx".format(month, day)
    df = pd.read_excel(url)
  df = pd.read_excel(url)
except Exception as e:
  today = today - timedelta(days = 1)
  day = today.strftime("%d")
  month = today.strftime("%m")
  url  = "https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-2020-{}-{}.xls".format(month, day)
  try:
    df = pd.read_excel(url)
  except:
    url  = "https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-2020-{}-{}.xlsx".format(month, day)
    df = pd.read_excel(url)
  df = pd.read_excel(url)

print('DateRep,', 'Countries and territories,', 'NewConfCases,', 'NewDeaths,')
for index, row in df.iterrows():
    if row['GeoId'] != 'JPG11668':
      print(str(row['DateRep']) + ",", row['Countries and territories'] + ",", str(row['Cases']) + ",", str(row['Deaths']))