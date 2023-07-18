import pandas as pd
import count as ct 
from init import init_df

bd=init_df('base.xlsx')
print(bd.ifood.value_counts())