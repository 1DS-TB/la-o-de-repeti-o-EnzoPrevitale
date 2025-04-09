# 09 - Números perfeitos
perfeitos = []

for num in range(10000):
    divisores = []

    for i in range(1, num):
        if num % i == 0:
            divisores.append(i)

    soma = 0

    for x in divisores:
        soma += x

    if num == soma and num != 0:
        perfeitos.append(num)
print(perfeitos)