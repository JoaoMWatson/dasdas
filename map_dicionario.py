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

print(list(map(lambda x: x['balance'] > 10000, dicionario)))

map_dict = (list(
    map(lambda x: True if x['balance'] > 10000 else False, dicionario)))
print(map_dict)

for balance in map_dict:
    if True:
        print('Rico')
    elif False:
        print('menos rico')
