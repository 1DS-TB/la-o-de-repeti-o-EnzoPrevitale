# 06 - Fibonacci
n = int(input("Digite um número: "))
fibonacci = [0, 1]

for i in range(0, n):
    numero = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(numero)

print(fibonacci)