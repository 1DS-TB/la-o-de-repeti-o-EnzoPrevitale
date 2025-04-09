# 05 - Número primo
n = int(input("Digite um número: "))
multiplos = 0

for i in range(2, n):
    if n % i == 0:
        multiplos += 1

if multiplos == 0 and n > 1:
    print("O número é primo.")
else:
    print("O número não é primo.")