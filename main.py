import pandas as pd
from remove_ext import remove
import quality as q 
import noiser as n
from hunspell import Hunspell

#df=pd.DataFrame([['12/2','3', 12, 3.2],['21/3/2012','3',32,3.33]], columns=['date','obj','int','flt'])
df=pd.read_csv('disney_movies.csv')
print(df.head())
#df=q.norm_nan(df)
wrong, cols = q.cons_type(df)
print(q.acc_sem(df,cols))

# remove '.txt' from books archive name
# books = list(df['Work'])
# for i in range(len(books)):
#     books[i]=remove(books[i])
#     books[i]=n.typo(books[i], lvl=1)
#     print('\n-----------------------------------------------------------\n'+books[i])
#     words=books[i].split(' ')
#     for j in range(len(words)):
#         print(h.spell(words[j].lower()))   



# import nltk
# nltk.download('stopwords','plunkt')
# stopwords = nltk.corpus.stopwords.words("portuguese")
# print(len(stopwords))

# leitura do arquivo (csv)
# ########################################################
# path='penguins_size.csv'
# df=pd.read_csv(path)
#print(df.describe())

# verificação da qualidade dos dados
# ########################################################
# q.dtype_columns(df)
# q.duplicated(df)
# q.missing(df,df.columns)

# BOOKS # spellchexker
##########################################################################
#from spellchecker import SpellChecker
# df=pd.read_csv('guideToDocuments.csv')
# #print(df.head())
# # remove '.txt' from books archive name
# spell=SpellChecker(language='pt')
# books = list(df['Work'])
# for i in range(len(books)):
#     books[i]=remove(books[i])
#     books[i]=n.typo(books[i], lvl=1)
#     print('\n-----------------------------------------------------------\n'+books[i])
#     print(spell.correction(books[i]))
##########################################################################


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


# salvar no arquivo (csv)
########################################################
#df.to_csv('disney_movies_1pct.csv')