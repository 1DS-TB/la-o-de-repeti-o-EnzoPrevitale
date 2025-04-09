# 08 - Série harmônica

n = int(input("Digite um número: "))
soma = 0

for i in range(1, n + 1):
    soma += 1/i

print("%.2f" % soma)
