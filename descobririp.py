def retorna(x, *args):
    return x(args)


x = lambda args: sum(args)
y = retorna(x, 2, 2)
print(y)
