dicionario = [{
    'nome': "João Pedro",
    'balance': 10000
}, {
    'nome': 'Sophia',
    'balance': 100000000
}, {
    'nome': 'Diego',
    'balance': 4
}, {
    'nome': 'Julianne',
    'balance': 0.54
}]

def rico(*args, **kwargs):
    for nome, balance in kwargs:
        if balance.values == 100:
            print('Rico')
        else:
            print('pobre')

map_dict = (list(map(rico(kwargs=dicionario), dicionario)))
print(map_dict)