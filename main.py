import pandas as pd
import quality as q 
import noiser as n

# leitura do arquivo (csv)
########################################################
df=pd.read_csv('disney_movies_1pct.csv')

# remoção de registros com dados faltando
########################################################
# print(len(df))
# df=df.dropna(axis='rows')
# print(len(df))

# adição de ruido
########################################################
# frac=0.05
# q.dtype_columns(df)

# df=n.insert_nan(df, frac, df.columns)
# df=n.typo(df, frac, ['movie_title', 'genre', 'mpaa_rating'])
# df=n.to_str(df, frac ,['total_gross'])
# df=n.duplicate_rows(df, frac)

# verificação da qualidade dos dados
########################################################
q.dtype_columns(df)
q.duplicated(df)
q.missing(df,df.columns)

# salvar no arquivo (csv)
########################################################
#df.to_csv('disney_movies_1pct.csv')