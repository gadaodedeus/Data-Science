import pandas as pd
import count as ct 
from init import init_df
import quality as q 

bd=init_df('base.xlsx')
q.missing(bd.plataforma)