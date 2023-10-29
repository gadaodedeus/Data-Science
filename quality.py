import pandas as pd 
import matplotlib.pyplot as plt
import re

def pie_plot(labels, percent, title):
    plot=plt.pie([percent,1-percent],labels=labels,autopct='%1.1f%%')
    plt.title(title)
    plt.show()

def duplicated(df):
    percent_dupli = df.duplicated().sum()/len(df)
    labels=['Duplicados','Únicos']
    print(df.duplicated().sum()/len(df))
    pie_plot(labels, percent_dupli, 'Registros Duplicados')

def missing(df): #quantidade de registros nao vazios
    percent_mis = df.isna().sum()/len(df)
    labels = ['Faltando', 'Completo']
    title='Dados faltantes em '+str(df.name)
    pie_plot(labels, percent_mis, title)
