numeros = list(map(lambda x: x-1, [2, 2, 4, 5, 6]))
print(numeros)

print(list(map(lambda x: x-1, [2, 2, 4, 5, 6])))

print(list(map(lambda x, y: x + y, [1, 2, 3, 4], [1, 2, 3, 4])))
print(list(map(lambda x: x + x, [1, 2, 3, 4], [1, 2, 3, 4]))) # Error positional argument 

