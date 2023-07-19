import pandas as pd 

def dict_sum(table):
    count=0
    for i in table.keys():
        count+=table[i]
    return count

def report(metric, aux_dict, total):
    if(metric == 'duplicated'):
        duplicated_data=dict_sum(aux_dict)
        percentage=float(duplicated_data/total)
        print('--------------DUPLICATED')
        print('\tTOTAL DATA: '+str(total))
        print('\tDUPLICATED DATA: '+str(duplicated_data))
        print('\tPERCENTAGE: '+str(percentage*100)+'%')

    if(metric == 'uniquiness'):
        unique_data=dict_sum(aux_dict)
        percentage=float(unique_data/total)
        print('--------------UNIQUINESS')
        print('\tTOTAL DATA: '+str(total))
        print('\tUNIQUE DATA: '+str(unique_data))
        print('\tPERCENTAGE: '+str(percentage*100)+'%')
    
    if metric == 'missing':
        mis=aux_dict[0]
        percentage=float(mis/total)
        print('--------------MISSING')
        print('\tTOTAL DATA: '+str(total))
        print('\tMISSING DATA: '+str(mis))
        print('\tPERCENTAGE: '+str(percentage*100)+'%')
    
def duplicated(col_list):
    aux=col_list.value_counts()
    aux_dict={}
    for reg in aux.keys():
        if(aux[reg]==1):
            break
        if(reg=='*'):
            continue
        aux_dict[reg]=aux[reg]
    report('duplicated', aux_dict, len(col_list))

def uniquiness(col_list):
    aux=col_list.value_counts()
    aux_dict={}
    for reg in aux.keys():
        if(aux[reg]>1):
            continue
        aux_dict[reg]=aux[reg]
    report('uniquiness', aux_dict, len(col_list))

def missing(col_list): #quantidade de registros nao vazios
    mis=0
    aux_dict={}
    for reg in col_list:
        if reg == '*':
	        mis+=1
    aux_dict[0]=mis
    report('missing',aux_dict,len(col_list))