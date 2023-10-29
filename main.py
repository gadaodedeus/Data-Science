import pandas as pd
from init import init_df
import quality as q 
import noiser as n

df=pd.read_excel('base.xlsx')

n.typo(df, 0.2, ['Segmento '], 1)