# 11 - Jogo
import random

turno = 1
vida_maxima = random.randint(200, 1000)

entidade = {
    "jogador": {
        "vida": vida_maxima,
        "ataque": random.randint(1, 50),
        "defesa": random.randint(1, 50),
        "dano": 0,
        "itens": {
            "Poção de Força": 2,
            "Poção de Regeneração": 2,
            "Poção de Fraqueza": 2,
            "Frasco de Veneno": 2,
        },
        "turnos": {
            "força": 0,
            "regeneração": 0,
            "fraqueza": 0,
            "veneno": 0
        },
        "efeitos": {
            "Poção de Força": False,
            "Poção de Regeneração": False,
            "Poção de Fraqueza": False,
            "Frasco de Veneno": False
        },
    },

    "inimigo": {
        "vida": vida_maxima,
        "ataque": random.randint(1, 50),
        "defesa": random.randint(1, 50),
        "dano": 0,
        "itens": {
            "Poção de Força": 2,
            "Poção de Regeneração": 2,
            "Poção de Fraqueza": 2,
            "Frasco de Veneno": 2,
        },
        "turnos": {
            "força": 0,
            "regeneração": 0,
            "fraqueza": 0,
            "veneno": 0
        },
        "efeitos": {
            "Poção de Força": False,
            "Poção de Regeneração": False,
            "Poção de Fraqueza": False,
            "Frasco de Veneno": False
        }
    }
}

status = {
    "Buffer Overflow": "",
    "Loop Infinito": "",
    "Tela Azul": "",
    "Cache Hit": "",
    "Turnos Tela Azul": 2
}

while entidade["jogador"]["ataque"] <= entidade["inimigo"]["defesa"]:
    entidade["jogador"]["ataque"] = random.randint(1, 50)
while entidade["inimigo"]["ataque"] <= entidade["jogador"]["defesa"]:
    entidade["inimigo"]["ataque"] = random.randint(1, 50)

cura_maxima = vida_maxima // 20

multiplayer = input("""
=== JOGO DO BALACOBACO ===
[1] Um jogador | [2] Multijogador
""")

while multiplayer != '1' and multiplayer != '2':
    multiplayer = input("""
    === JOGO DO BALACOBACO ===
    [1] Um jogador | [2] Multijogador
    """)
else:
    if multiplayer == '1':
        multiplayer = False
    elif multiplayer == '2':
        multiplayer = True

print(f"""
    === JOGADOR            ===
    Vida: {entidade["jogador"]["vida"]}
    Ataque: {entidade["jogador"]["ataque"]} | Defesa: {entidade["jogador"]["defesa"]}

    === INIMIGO            ===
    Vida: {entidade["inimigo"]["vida"]}
    Ataque: {entidade["inimigo"]["ataque"]} | Defesa: {entidade["inimigo"]["defesa"]}
    """)

entidade["jogador"]["dano"] = entidade["jogador"]["ataque"] - entidade["inimigo"]["defesa"]
entidade["inimigo"]["dano"] = entidade["inimigo"]["ataque"] - entidade["jogador"]["defesa"]

entidade["jogador"]["dano_base"] = entidade["jogador"]["dano"]
entidade["inimigo"]["dano_base"] = entidade["inimigo"]["dano"]

while entidade["jogador"]["vida"] > 0 and entidade["inimigo"]["vida"] > 0:
    print(f"""
    --- TURNO {turno}     ---
    JOGADOR: {entidade["jogador"]["vida"]} | INIMIGO | {entidade["inimigo"]["vida"]}
    """)

    if status["Loop Infinito"] != "Jogador":
        # Acao do entidade["jogador"]
        escolha = input("Sua vez! Deseja [1] atacar, [2] curar ou [3] abrir mochila? ")

        while escolha != '1' and escolha != '2' and escolha != '3':
            escolha = input("Sua vez! Deseja [1] atacar, [2] curar ou [3] abrir mochila? ")
        if escolha == '1': # Jogador ataca
            critico = random.randint(1, 10) == 10
            if not critico:
                entidade["inimigo"]["vida"] -= entidade["jogador"]["dano"]
            else:
                entidade["inimigo"]["vida"] -= 2 * entidade["jogador"]["dano"]
                print("Golpe critico!")
            print(f"O jogador ataca! Inimigo perde {entidade["jogador"]["dano"] if not critico else 2 * entidade["jogador"]["dano"]} de vida.")
        elif escolha == '2': # Jogador cura
            vida_anterior = entidade["jogador"]["vida"]
            entidade["jogador"]["vida"] += cura_maxima
            if entidade["jogador"]["vida"] > vida_maxima:
                entidade["jogador"]["vida"] = vida_maxima
            cura = entidade["jogador"]["vida"] - vida_anterior
            print(f"O jogador se cura! Ganha {cura} de vida.")
        elif escolha == '3': # Abrir mochila
            itens_utilizaveis = []
            for i in entidade["jogador"]["itens"]:
                if entidade["jogador"]["itens"][i] > 0:
                    itens_utilizaveis.append(i)
            for i in range(len(itens_utilizaveis)):
                print(f"[{i + 1}]: {itens_utilizaveis[i]} | {entidade["jogador"]["itens"][itens_utilizaveis[i]]}")
            item = int(input("Selecione um item: "))
            while item <= 0 or item > len(itens_utilizaveis):
                item = int(input("Selecione um item: "))
            item_escolhido = itens_utilizaveis[item - 1]

            # Aplicando efeitos
            if not entidade["jogador"]["efeitos"][item_escolhido]:
                entidade["jogador"]["efeitos"][item_escolhido] = True
                print(f"O jogador utiliza {item_escolhido}!")
                entidade["jogador"]["itens"][item_escolhido] -= 1

    if status["Loop Infinito"] != "Inimigo":
        # Singleplayer
        if not multiplayer:
            # Acao do entidade["inimigo"]
            escolha = random.choice(['1', '2'])
            if escolha == '1': # Inimigo ataca
                critico = random.randint(1, 10) == 10
                if not critico:
                    entidade["jogador"]["vida"] -= entidade["inimigo"]["dano"]
                else:
                    entidade["jogador"]["vida"] -= 2 * entidade["inimigo"]["dano"]
                    print("O inimigo acertou um golpe critico!")
                print(f"O inimigo ataca! Jogador perde {entidade["inimigo"]["dano"] if not critico else 2 * entidade["inimigo"]["dano"]} de vida.")
            elif escolha == '2': # Inimigo cura
                vida_anterior = entidade["inimigo"]["vida"]
                entidade["inimigo"]["vida"] += cura_maxima
                if entidade["inimigo"]["vida"] > vida_maxima:
                    entidade["inimigo"]["vida"] = vida_maxima
                cura = entidade["inimigo"]["vida"] - vida_anterior
                print(f"O inimigo se cura! Ganha {cura} de vida.")

            # Multiplayer
        elif multiplayer:
            escolha = input("Sua vez! Deseja [1] atacar, [2] curar ou [3] abrir mochila? ")

            while escolha != '1' and escolha != '2' and escolha != '3':
                escolha = input("Sua vez! Deseja [1] atacar, [2] curar ou [3] abrir mochila? ")
            if escolha == '1':  # Jogador ataca
                critico = random.randint(1, 10) == 10
                if not critico:
                    entidade["jogador"]["vida"] -= entidade["inimigo"]["dano"]
                else:
                    entidade["jogador"]["vida"] -= 2 * entidade["inimigo"]["dano"]
                    print("Golpe critico!")
                print(
                    f"O inimigo ataca! Jogador perde {entidade["inimigo"]["dano"] if not critico else 2 * entidade["inimigo"]["dano"]} de vida.")
            elif escolha == '2':  # Jogador cura
                vida_anterior = entidade["inimigo"]["vida"]
                entidade["inimigo"]["vida"] += cura_maxima
                if entidade["inimigo"]["vida"] > vida_maxima:
                    entidade["inimigo"]["vida"] = vida_maxima
                cura = entidade["inimigo"]["vida"] - vida_anterior
                print(f"O inimigo se cura! Ganha {cura} de vida.")
            elif escolha == '3':  # Abrir mochila
                itens_utilizaveis = []
                for i in entidade["inimigo"]["itens"]:
                    if entidade["inimigo"]["itens"][i] > 0:
                        itens_utilizaveis.append(i)
                for i in range(len(itens_utilizaveis)):
                    print(f"[{i + 1}]: {itens_utilizaveis[i]} | {entidade["inimigo"]["itens"][itens_utilizaveis[i]]}")
                item = int(input("Selecione um item: "))
                while item <= 0 or item > len(itens_utilizaveis):
                    item = int(input("Selecione um item: "))
                item_escolhido = itens_utilizaveis[item - 1]

                # Aplicando efeitos
                if not entidade["inimigo"]["efeitos"][item_escolhido]:
                    entidade["inimigo"]["efeitos"][item_escolhido] = True
                    print(f"O inimigo utiliza {item_escolhido}!")
                    entidade["inimigo"]["itens"][item_escolhido] -= 1

    escolha = ''

    if status["Buffer Overflow"] == "Jogador":
        entidade["jogador"]["vida"] -= 1//20 * vida_maxima
    elif status["Buffer Overflow"] == "Inimigo":
        entidade["inimigo"]["vida"] -= 1//20 * vida_maxima

    # Contando os turnos com o efeito de força
    if entidade["jogador"]["efeitos"]["Poção de Força"]:
        entidade["jogador"]["turnos"]["força"] += 1
        entidade["jogador"]["dano"] = entidade["jogador"]["dano_base"] * 2
        # Retirando efeito de força
        if entidade["jogador"]["turnos"]["força"] >= 3:
            entidade["jogador"]["efeitos"]["Poção de Força"] = False
            entidade["jogador"]["dano"] = entidade["jogador"]["dano_base"]
            print("O efeito da poção de força do jogador acabou.")

    # Aplicando efeito de regeneração
    if entidade["jogador"]["efeitos"]["Poção de Regeneração"]:
        entidade["jogador"]["vida"] += vida_maxima // 20
        if entidade["jogador"]["vida"] > vida_maxima:
            entidade["jogador"]["vida"] = vida_maxima
        entidade["jogador"]["turnos"]["regeneração"] += 1
        # Retirando efeito de regeneração
        if entidade["jogador"]["turnos"]["regeneração"] >= 6:
            entidade["jogador"]["efeitos"]["Poção de Regeneração"] = False
            print("O efeito da poção de regeneração do jogador acabou.")

        # Aplicando efeito de fraqueza
    if entidade["jogador"]["efeitos"]["Poção de Fraqueza"]:
        entidade["inimigo"]["dano"] = entidade["inimigo"]["dano_base"] // 2
        entidade["jogador"]["turnos"]["fraqueza"] += 1
        # Retirando efeito de fraqueza
        if entidade["jogador"]["turnos"]["fraqueza"] >= 3:
            entidade["jogador"]["efeitos"]["Poção de Fraqueza"] = False
            entidade["inimigo"]["dano"] = entidade["inimigo"]["dano_base"]
            print("O efeito da poção de fraqueza do jogador acabou.")

    # Aplicando efeito de envenenamento
    if entidade["jogador"]["efeitos"]["Frasco de Veneno"]:
        entidade["inimigo"]["vida"] -= vida_maxima//50
        entidade["jogador"]["turnos"]["veneno"] += 1
        # Retirando efeito de envenenamento
        if entidade["jogador"]["turnos"]["veneno"] >= 6:
            entidade["jogador"]["efeitos"]["Frasco de Veneno"] = False
            print("O efeito do frasco de veneno do jogador acabou.")

    # INIMIGO
    # Contando os turnos com o efeito de força
    if entidade["inimigo"]["efeitos"]["Poção de Força"]:
        entidade["inimigo"]["turnos"]["força"] += 1
        entidade["inimigo"]["dano"] = entidade["inimigo"]["dano_base"] * 2
        # Retirando efeito de força
        if entidade["inimigo"]["turnos"]["força"] >= 3:
            entidade["inimigo"]["efeitos"]["Poção de Força"] = False
            entidade["inimigo"]["dano"] = entidade["inimigo"]["dano_base"]
            print("O efeito da poção de força do inimigo acabou.")

    # Aplicando efeito de regeneração
    if entidade["inimigo"]["efeitos"]["Poção de Regeneração"]:
        entidade["inimigo"]["vida"] += vida_maxima // 20
        if entidade["inimigo"]["vida"] > vida_maxima:
            entidade["inimigo"]["vida"] = vida_maxima
        entidade["inimigo"]["turnos"]["regeneração"] += 1
        # Retirando efeito de regeneração
        if entidade["inimigo"]["turnos"]["regeneração"] >= 6:
            entidade["inimigo"]["efeitos"]["Poção de Regeneração"] = False
            print("O efeito da poção de regeneração do inimigo acabou.")

        # Aplicando efeito de fraqueza
    if entidade["inimigo"]["efeitos"]["Poção de Fraqueza"]:
        entidade["jogador"]["dano"] = entidade["jogador"]["dano_base"] // 2
        entidade["inimigo"]["turnos"]["fraqueza"] += 1
        # Retirando efeito de fraqueza
        if entidade["inimigo"]["turnos"]["fraqueza"] >= 3:
            entidade["inimigo"]["efeitos"]["Poção de Fraqueza"] = False
            entidade["jogador"]["dano"] = entidade["jogador"]["dano_base"]
            print("O efeito da poção de fraqueza do inimigo acabou.")

    # Aplicando efeito de envenenamento
    if entidade["inimigo"]["efeitos"]["Frasco de Veneno"]:
        entidade["jogador"]["vida"] -= vida_maxima // 50
        entidade["inimigo"]["turnos"]["veneno"] += 1
        # Retirando efeito de envenenamento
        if entidade["inimigo"]["turnos"]["veneno"] >= 6:
            entidade["inimigo"]["efeitos"]["Frasco de Veneno"] = False
            print("O efeito do frasco de veneno do inimigo acabou.")



    if random.randint(1, 15) == 15:
        status_lista = []
        for i in status:
            status_lista.append(i)
        alvo = random.choice(["Jogador", "Inimigo"])
        status_aplicado = random.choice(status_lista)
        status[status_aplicado] = alvo if status[status_aplicado] == "" else "APLICADO"
        if status[status_aplicado] != "APLICADO":
            print(f"O {alvo} está com {status_aplicado}!")
        if status_aplicado == "Tela Azul" and status["Tela Azul"] != "APLICADO":
            defesa = entidade[status["Tela Azul"].lower()]["defesa"]

    if status["Cache Hit"] != "APLICADO" and status["Cache Hit"] != "":
        if entidade[status["Cache Hit"].lower()]["vida"] < 1/4 * vida_maxima:
            entidade[status["Cache Hit"].lower()]["vida"] += 3//10 * vida_maxima
            status["Cache Hit"] = "APLICADO"

    if status["Turnos Tela Azul"] > 0 and status["Tela Azul"] != "APLICADO" and status["Cache Hit"] != "":
        entidade[status["Tela Azul"]]["defesa"] = 0
        status["Turnos Tela Azul"] -= 1
    elif status["Turnos Tela Azul"] <= 0 and status["Tela Azul"] != "APLICADO" and status["Cache Hit"] != "":
        status["Tela Azul"] = "APLICADO"

    turno += 1

    for i in status:
        print(f"{i}: {status[i]}")
else:
    if entidade["jogador"]["vida"] <= 0:
        print("=== FIM DE JOGO. O JOGADOR FOI DERROTADO. ===")
    elif entidade["inimigo"]["vida"] <= 0:
        print("=== FIM DE JOGO. O JOGADOR VENCEU! ===")