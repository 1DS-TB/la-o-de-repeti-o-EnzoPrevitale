# 02 - Soma até n

n = int(input("Digite um número inteiro positivo: "))
contador = 0
soma = 0

while contador < n:
    contador += 1
    soma += contador

print(f"A soma é {soma}.")
