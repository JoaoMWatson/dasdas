dicionario = {
    "somar": lambda a, b: a + b,
    "subtrair": lambda a, b: a - b,
    "multiplicar": lambda a, b: a * b,
    "dividir": lambda a, b: a / b,
}

mostrar = dicionario["somar"]
print(mostrar(1, 1))

try:
    print(dicionario["dividir"](10, 0))
except ZeroDivisionError:
    print("Erro ao dividir por 0")
finally:
    print(dicionario["multiplicar"](10, 0))