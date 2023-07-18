def count_reg(data_list): #total de registros diferentes  #PODE SER SUBSTITUIDO POR BD.COLUMN.value_conts()
	dict={}
	for reg in data_list:
		if reg in dict:
			dict[reg]+=1
		else:
			dict[reg]=1
	return dict

def count_missing(data_list): #quantidade de registros nao vazios
	mis=0
	for reg in data_list:
		if reg == '*':
			mis+=1
	return mis

