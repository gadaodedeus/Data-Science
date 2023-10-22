import pandas as pd
from init import init_df
import quality as q 

bd=init_df('base.xlsx')
q.validity(bd.nome, 'nome')