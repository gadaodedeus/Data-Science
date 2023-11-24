import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import re
from hunspell import Hunspell 
import string
import math
import operator


# PLOT
###############################################################################
def pie_plot(labels, dict_col, title):
    # axis reference
    x = 0
    y = 0
    
    if(len(dict_col.keys()) > 1):   # one plot required (item on dict)
        fig, axs = plt.subplots(ncols=4,nrows=int(len(dict_col.keys())/4)+1)
    else:   # more than one plot (item on dict)
        fig, axs = plt.subplots()

    fig.suptitle(title) # title
    fig.set_size_inches(18.5, 10.5, forward=True)   # fig format
   
    if(len(dict_col.keys()) > 1):   # more than one item on dict
        for i in dict_col.keys():
            axs[y,x].pie([dict_col[i], 1-dict_col[i]], autopct='%1.1f%%')   # autopct = shows data on pie graph
            axs[y,x].set_title(i)
            axs[y,x].legend(loc='upper right', labels=labels)         
            
            # index update
            if(x==3):
                x=0
                y+=1
            x+=1

    else:   # one item on dict
        axs.pie([dict_col['0'], 1-dict_col['0']], autopct='%1.4f%%')
        axs.legend(loc='upper right', labels=labels)   

    plt.show()

def bar_plot(data, title):
    X = data.keys()
    Y = [] 
    Z = [] 
    for i in data.keys():
        Y.append(data[i][0])
        Z.append(data[i][1])

    X_axis = np.arange(len(X)) 
    
    plt.bar(X_axis - 0.2, Y, 0.4, label = 'Total') 
    plt.bar(X_axis + 0.2, Z, 0.4, label = 'Wrong') 
    
    plt.xticks(X_axis, X) 
    plt.xlabel("Properties") 
    plt.ylabel("Data quantity") 
    plt.title(title) 
    plt.legend() 
    plt.show() 
###############################################################################

# PANDAS AND HUNSPELL FUNCS
###############################################################################
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

def typo_detect(df, col):
    dict_col={}
    
    h = Hunspell('Portuguese (Brazilian)', hunspell_data_dir='dict')
    for i in col:
        typo_count=0    # qtn rows detected with typo
        for j in range(len(df[i])):
            words=df[i][j]  # get words from df
            words=re.sub(r'\W+', ' ', words)    # remove non-alphanumeric stuff -> whitespace
            words=words.split(' ')  # split to list
            print(words)

            for k in range(len(words)): # check each word of sentence
                if(not h.spell(words[k].lower())):  # misspelled
                    typo_count+=1
                    break

        if(len(col) == 1):  # single plot
            dict_col['0']=typo_count/len(df[i])
        else:               # multiples plots
            dict_col[i]=typo_count/len(df[i])

    labels = ['Errado', 'Correto']
    pie_plot(labels, dict_col, 'Typo Errors')
###############################################################################


# ACCURACY FUNCS
###############################################################################
    # 1.1 SYNTAX
def acc_syntex(df, col):
    for i in col:
        pass
###############################################################################


# CONSISTENCY FUNCS
###############################################################################
# CONSISTENCY MAIN FUNC
def consistency(df):    # get all the subcaracteristcs in one func
    data={'format':[]}
    # 3.3 format
    data['format'].append(len(df.columns))
    data['format'].append(cons_type(df))
    # print('Total columns: '+str(len(df.columns)))
    # print('Wrong type columns: '+str(wrong_cols))


    bar_plot(data, 'CONSISTENCY')
#

def cons_type(df):  # 3.3 FORMAT   # data type on each row
    # var def
    ######################################################
    
    #############
    #returned var   # count wrong type columns
    wrong_cols=0
    #############

    #types in df via pandas
    real_type=df.dtypes
    # fraction of df
    aux=df#.sample(frac=0.01)
    #series of prevision
    detected={}
    # df.columns (will be used to try except)
    col=0
    # count of possible types
    types_incol={'int': 0 , 'float': 0, 'datetime': 0, 'object': 0}
    # inconsistency cols
    inc_cols=[]
    #######################################################

    # re patterns
    #######################################################
    integer = re.compile("[0-9]+")
    flt = re.compile('[0-9]+[.;,]{1}[0-9]+')
    date=re.compile('((0?[1-9]|1[0-9]|2[0-9]|3[0-1])[/-]((0?)[1-9]|11|12)[/-]?([1-9][0-9]{1}|[1-9][0-9]{3})?)|(([1-9][0-9]{1}|[1-9][0-9]{3})[/-]((0?)[1-9]|11|12)[/-]?(0?[1-9]|1[0-9]|2[0-9]|3[0-1])?)|(((0?)[1-9]|11|12)[/-]((0)?[1-9]|1[0-9]|2[0-9]|3[0-1])[/-]?([1-9][0-9]{1}|[1-9][0-9]{3})?)')
    ########################################################

    # verification
    #########################################################
    # dataframe
    ################### 
    try:    
        col=df.columns

        # each column
        for i in col:
            types_incol={'int': 0 , 'float': 0, 'datetime': 0, 'object': 0} # reset dict

            # each row
            for j in range(len(aux)):
                
                # verify nan
                if(pd.isna(aux[i][j])):
                    pass
                
                # match pattern
                else:
                    #print(str(df[i][j]))

                    if(date.fullmatch(str(df[i][j]))):
                        types_incol['datetime']+=1

                    elif(flt.fullmatch(str(df[i][j]))):
                        types_incol['float']+=1
                    
                    elif(integer.fullmatch(str(df[i][j]))):
                        types_incol['int']+=1
        
                    else:
                        types_incol['object']+=1
            
            detected[i]=max(types_incol.items(), key=operator.itemgetter(1))[0]
            if(str(detected[i]) not in str(real_type[i])):
                print('Which type is the real one for '+i)
                print('\t1- '+detected[i])
                print('\t2- '+str(real_type[i]))
                real=int(input())
                if(real == 2):
                    inc_cols.append(i)
                    wrong_cols+=1
        if(wrong_cols > 0):
            print('As colunas '+str(inc_cols)+' sao inconsistentes!')

    # series
    ###################    
    except: 

        # each row
        for j in range(len(aux)):

            # verify nan
            if(pd.isna(aux[j])):
                pass

            # match pattern
            else:
                if(date.fullmatch(str(df[j]))):
                    types_incol['datetime']+=1

                elif(flt.fullmatch(str(df[j]))):
                    types_incol['float']+=1
                
                elif(integer.fullmatch(str(df[j]))):
                    types_incol['int']+=1
    
                else:
                    types_incol['object']+=1
                    
        type_serie=max(types_incol.items(), key=operator.itemgetter(1))[0]

        if(str(type_serie) not in str(real_typ)):
                print('Which type is the real one?')
                print('\t1- '+type_serie)
                print('\t2- '+real_type)
                real=int(input())
                if(real == 1):
                    wrong_cols+=1
        if(wrong_cols > 0):
            print('O tipo da Serie é inconsistente!')

    return wrong_cols
    ###################################################
###############################################################################