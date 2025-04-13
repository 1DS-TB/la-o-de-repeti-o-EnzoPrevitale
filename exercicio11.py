# 11 - Jogo
import random

turno = 1
vida_maxima = random.randint(200, 1000)

jogador = {
    "vida": vida_maxima,
    "ataque": random.randint(1, 50),
    "defesa": random.randint(1, 50),
    "dano": 0
}

inimigo = {
    "vida": vida_maxima,
    "ataque": random.randint(1, 50),
    "defesa": random.randint(1, 50),
    "dano": 0
}

while jogador["ataque"] <= inimigo["defesa"]:
    jogador["ataque"] = random.randint(1, 50)
while inimigo["ataque"] <= jogador["defesa"]:
    inimigo["ataque"] = random.randint(1, 50)

cura_maxima = vida_maxima // 20

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
    jogador["dano"] = jogador["ataque"] - inimigo["defesa"]
    inimigo["dano"] = inimigo["ataque"] - jogador["defesa"]

    print(f"""
--- TURNO {turno}             ---
JOGADOR: {jogador["vida"]} | INIMIGO: {inimigo["vida"]}
""")

    # Acao do jogador
    escolha = input("Sua vez! Deseja [1] atacar ou [2] curar? ")

    while escolha != '1' and escolha != '2':
        escolha = input("Sua vez! Deseja [1] atacar ou [2] curar? ")
    if escolha == '1': # Jogador ataca
        critico = random.randint(1, 10) == 10
        if not critico:
            inimigo["vida"] -= jogador["dano"]
        else:
            inimigo["vida"] -= 2 * jogador["dano"]
            print("Golpe critico!")
        print(f"O jogador ataca! Inimigo perde {jogador["dano"] if not critico else 2 * jogador["dano"]} de vida.")
    elif escolha == '2': # Jogador cura
        vida_anterior = jogador["vida"]
        jogador["vida"] += cura_maxima
        if jogador["vida"] > vida_maxima:
            jogador["vida"] = vida_maxima
        cura = jogador["vida"] - vida_anterior
        print(f"O jogador se cura! Ganha {cura} de vida.")

    # Acao do inimigo
    escolha = random.choice(['1', '2'])
    if escolha == '1': # Inimigo ataca
        critico = random.randint(1, 10) == 10
        if not critico:
            jogador["vida"] -= inimigo["dano"]
        else:
            jogador["vida"] -= 2 * inimigo["dano"]
            print("O inimigo acertou um golpe critico!")
        print(f"O inimigo ataca! Jogador perde {inimigo["dano"] if not critico else 2 * inimigo["dano"]} de vida.")
    elif escolha == '2': # Inimigo cura
        vida_anterior = inimigo["vida"]
        inimigo["vida"] += cura_maxima
        if inimigo["vida"] > vida_maxima:
            inimigo["vida"] = vida_maxima
        cura = inimigo["vida"] - vida_anterior
        print(f"O inimigo se cura! Ganha {cura} de vida.")

    escolha = ''
    turno += 1
else:
    if jogador["vida"] <= 0:
        print("=== FIM DE JOGO. O JOGADOR FOI DERROTADO. ===")
    elif inimigo["vida"] <= 0:
        print("=== FIM DE JOGO. O JOGADOR VENCEU! ===")