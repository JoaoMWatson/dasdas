n1 = 5779
i = 0
x = 0

for i in range(1, n1+1):
    if(n1 % i == 0):
        x += 1

if(x == 2):
    print("Primo")
else:
    print("Padrao xDxD")
