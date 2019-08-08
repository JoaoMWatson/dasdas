# sintax => filter(funcao_aplicada, lista_elementos)
lista_par = [1, 2, 3, 4, 5, 6, 7, 23, 123, 52, 123, 52, 62, 99, 2345]
numeros_pares = list(filter(lambda x: x % 2 == 0, lista_par))
print(numeros_pares)

lista_range = range(-5, 5)
menor_que_zero = list(filter(lambda x: x < 0, lista_range))
print(menor_que_zero)
    