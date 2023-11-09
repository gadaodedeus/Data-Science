import pandas as pd 
import matplotlib.pyplot as plt
import re

def pie_plot(labels, dict_col, title):
    l=0
    fig, axs = plt.subplots(len(dict_col.keys()))
    fig.suptitle(title)

    if(len(dict_col.keys()) > 1):   # more than one item on dict
        for i in dict_col.keys():
            axs[l].pie([dict_col[i], 1-dict_col[i]], labels=labels, autopct='%1.1f%%')
            axs[l].set_title(i)
            l+=1

    else:   # one item on dict
        axs.pie([dict_col['0'], 1-dict_col['0']], labels=labels, autopct='%1.1f%%')

    plt.show()

def duplicated(df): # rows duplicated
    percent_dupli = df.duplicated().sum()/len(df)
    labels=['Duplicados','Únicos']
    pie_plot(labels, {'0': percent_dupli}, 'Registros Duplicados')

def missing(df, col): # missing values on columns
    dict_col={}
    for i in col:
        percent_mis = df[i].isna().sum()/len(df)
        dict_col[i]=percent_mis
    labels = ['Faltando', 'Completo']
    pie_plot(labels, dict_col, 'Registros Faltantes')

def dtype_columns(df):  # data type on each row
    print(df.dtypes)
