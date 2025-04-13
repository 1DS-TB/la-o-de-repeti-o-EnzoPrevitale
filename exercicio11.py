# 11 - Jogo
import random

turno = 1
vida_maxima = random.randint(200, 1000)

jogador = {
    "vida": vida_maxima,
    "ataque": random.randint(1, 50),
    "defesa": random.randint(1, 50),
}

inimigo = {
    "vida": vida_maxima,
    "ataque": random.randint(1, 50),
    "defesa": random.randint(1, 50),
}

print(f"""
=== JOGO DO BALACOBACO ===

=== JOGADOR            ===
Vida: {jogador["vida"]}
Ataque: {jogador["ataque"]} | Defesa: {jogador["defesa"]}

=== INIMIGO            ===
Vida: {inimigo["vida"]}
Ataque: {inimigo["ataque"]} | Defesa: {inimigo["defesa"]}
""")

while jogador["vida"] > 0 and inimigo["vida"] > 0:
    print(f"""
--- TURNO {turno}             ---
JOGADOR: {jogador["vida"]} | INIMIGO: {inimigo["vida"]}
""")

    # Acao do jogador
    escolha = input("Sua vez! Deseja [1] atacar ou [2] curar? ")

    while escolha != '1' and escolha != '2':
        escolha = input("Sua vez! Deseja [1] atacar ou [2] curar? ")
    if escolha == '1': # Jogador ataca
        dano = jogador["ataque"] - inimigo["defesa"]
        print(dano)
        if dano <= 0:
            dano = 0
        inimigo["vida"] -= dano
        print(f"O jogador ataca! Inimigo perde {dano} de vida.")
    elif escolha == '2': # Jogador cura
        vida_anterior = jogador["vida"]
        jogador["vida"] += 50
        if jogador["vida"] > vida_maxima:
            jogador["vida"] = vida_maxima
        cura = jogador["vida"] - vida_anterior
        print(f"O jogador se cura! Ganha {cura} de vida.")

'''
    # Acao do inimigo
    escolha = random.choice(['1', '2'])
    if escolha == '1': # Inimigo ataca
        dano_maximo = inimigo["ataque"] - jogador["defesa"]
        if dano_maximo <= 0:
            dano_maximo = 1
        dano_causado = random.randint(0, dano_maximo)
        jogador["vida"] -= dano_causado
        print(f"O inimigo ataca! Jogador perde {dano_causado} de vida.")
    elif escolha == '2': # Inimigo cura
        vida_anterior = inimigo["vida"]
        inimigo["vida"] += 50
        if inimigo["vida"] > vida_maxima:
            inimigo["vida"] = vida_maxima
        cura = inimigo["vida"] - vida_anterior
        print(f"O inimigo se cura! Ganha {cura} de vida.")
'''