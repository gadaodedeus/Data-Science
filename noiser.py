import pandas as pd 
import numpy as np
import random as rand
import string


df=pd.read_excel('base.xlsx')

# FUNCTIONS
#########################################
#
# DUPLICATE ROWS BY PERCENTAGE
def duplicate_rows(df, fraction):
    samp = df.sample(frac=fraction, axis=0) # by index
    df=pd.concat([df,samp], axis=0)
    return df
#
# TRANSFORM INTO NAN BY COLUMNS PERCENTAGE
def insert_nan(df, fraction, cols):
    for i in cols:
        samp = df.sample(frac=fraction, axis=0) # by index
        df=pd.concat([df,samp], axis=0)
        df=df.drop_duplicates(keep=False)
        samp[i]=np.NAN
        df=pd.concat([df,samp], axis=0)
    return(df)
#
# SIMULATE TYPO ERRORS
def typo(df, fraction, cols, lvl):
    for i in cols:
        samp = df.sample(frac=fraction, axis=0) # by index
        df=pd.concat([df,samp], axis=0)
        df=df.drop_duplicates(keep=False)
        for j in range(len(samp)):
            word=samp[i].iloc[j]
            for k in range(lvl):
                letter_swap = rand.choice(range(len(word)))
                new_word = ''.join([word[w] if w != letter_swap else rand.choice(string.ascii_letters) for w in range(len(word))])
                word=new_word
            samp[i].iloc[j]=new_word
        df=pd.concat([df,samp], axis=0)
    return df
#
# TIPE ERROR num -> str
def to_str(df, fraction, cols):
    for i in cols:
        samp = df.sample(frac=fraction, axis=0) # by index
        df=pd.concat([df,samp], axis=0)
        df=df.drop_duplicates(keep=False)
        samp[i]=samp[i].astype(str)
        df=pd.concat([df,samp],axis=0)
    return df
#

# 
## EXAMPLES
#########################################

## INSERT NAN
print(df.isnull().sum())
col=['Outra Plataforma de Delivery', 'Link da Plataforma ', 'Avaliação Google', 'Avaliação Ifood']
df=insert_nan(df,0.2,col)
print(df.isnull().sum())
#
## TYPOS SIMULATING
print(df['Segmento '].value_counts())
df=typo(df, 0.2, ['Segmento '], 3)
print(df['Segmento '].value_counts())
#
## CONVERT NUMERICAL VALUES TO OBJECT VALUES (num -> str)
#
#       convert to numerical to test function
df['Número de Seguidores']=pd.to_numeric(df['Número de Seguidores'], errors='coerce').convert_dtypes() 
print(df.dtypes)
#
df=to_str(df, 0.2, ['Número de Seguidores'])
print(df.dtypes)
#
#
## DUPLICATE ROWS BY %
df=duplicate_rows(df,0.2)
print(df.duplicated().sum())
#
## SAVE IN FILE
##################################################
df.to_excel('test.xlsx')