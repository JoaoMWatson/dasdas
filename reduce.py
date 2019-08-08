from functools import reduce

soma = reduce((lambda x, y: x+y), [1, 2, 3, 4])
print('soma', soma)


lista = [23, 42, 6345, 12314, 52, 1 ,2453, 756, 
        23420003, 63, 123 ,55225, 2312]
maior = reduce((lambda x, y: x if(x>y) else y), lista)
print('maior', maior)


maior = reduce((lambda x, y: x if(x>y) else y), 
            [23, 42, 6345, 12314, 52, 1 ,2453, 
            756, 23420003, 63, 123 ,55225, 2312])
print('maior2', maior)


fatorial = reduce((lambda x, y: x*y), [1, 2, 4, 5,])
print('Fatorial', fatorial)
