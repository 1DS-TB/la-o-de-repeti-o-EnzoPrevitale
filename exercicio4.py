# 04 - Fatorial
n = int(input("Digite um número: "))
fatorial = 1

for i in range(1, n + 1):
    fatorial = i * fatorial

print(f"{n}! = {fatorial}")