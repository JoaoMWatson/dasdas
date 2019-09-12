# limite = int(input("de um limite: "))
limite = 1000
i = 0
x = 0
primos = []

for i in range(1, limite+1):
    x = 0
    for il in range(1, limite+1):
        if(i % il == 0):
            x += 1
    if(x == 2):
        primos.append(i)

print(primos)
print(len(primos))