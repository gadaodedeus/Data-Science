def count_reg(data_list):
	dict={}
	for reg in data_list:
		if reg in dict:
			dict[reg]+=1
		else:
			dict[reg]=1
	return dict

def count_missing(data_list):
	mis=0
	for reg in data_list:
		if reg == '*':
			mis+=1
	return mis