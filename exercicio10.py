# 10 - Números de Kaprekar

kaprekar = []

inicio = int(input("Digite o início do intervalo que deseja verificar: "))
fim = int(input("Digite o fim do intervalo que deseja verificar: "))

for numero in range(inicio, fim + 1): # Verificando se cada numero no intervalo e Kaprekar
    verificacao = "{:02d}".format(numero ** 2)

    # Separando em direita e esquerda
    esquerda = int(verificacao[0:len(verificacao)//2])
    direita = int(verificacao[len(verificacao)//2:len(verificacao)])

    numero_final = esquerda + direita

    if numero_final == numero and numero_final > 0:
        kaprekar.append(numero_final)

if len(kaprekar) > 0:
    print(f"Os números de Kaprekar no intervalo [{inicio}; {fim}] são {kaprekar}.")
else:
    print(f"Não existem números de Kaprekar no intervalo [{inicio}; {fim}].")
