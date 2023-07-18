import pandas as pd
import count as ct 

bd=pd.read_excel('base.xlsx')
bd=bd.values.tolist()
bd=pd.DataFrame(bd, columns=['nome','ifood','rating','cnpj'] )
print(ct.count_reg(bd.nome))