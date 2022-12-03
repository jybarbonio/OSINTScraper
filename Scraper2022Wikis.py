import pandas as pd
from pandas.io.html import read_html

url = 'https://en.wikipedia.org/wiki/Administrative_divisions_of_Armenia'
tbl_provs = pd.read_html(url, index_col=1, attrs={"class":"wikitable"})

type(tbl_provs)
print(tbl_provs[0])

tbl_provs[0].to_csv('ARM_provinces.csv')