import pandas as pd

def init_df(base):
    bd=pd.read_excel(base)
    bd=bd.values.tolist()
    bd=pd.DataFrame(bd[1:], columns=['nome', 'segmento', 'contato', 'redes', 'seguidores', 'ifood', 'link_ifood','plataforma', 'link','aval_google', 'aval_ifood', 'cnpj', 'endereço', 'bairro', 'cep', 'porte', 'cnae'])
    return bd