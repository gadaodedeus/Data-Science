import pandas as pd
import count as ct 
from init import init_df

bd=init_df('base.xlsx')
print(ct.count_missing(bd.link_ifood))