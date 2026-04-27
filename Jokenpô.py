from random import randint

largura = 40
titulo = "JOKENPÔ"

print("*" * (largura // 2))
print(f"{titulo:^{largura // 2}}")
print("*" * (largura // 2))

print("Bem vindo ao jogo !!!\n")

itens = ("PEDRA", "PAPEL", "TESOURA")

print("[0] PEDRA")
print("[1] PAPEL")
print("[2] TESOURA")

while True:

    jogador = int(input("Qual é a sua jogada? "))

    if jogador < 0 or jogador > 2:
        print("Número inválido")
        continue

    computador = randint(0, 2)

    print(f"Você jogou {itens[jogador]}")
    print(f"Computador jogou {itens[computador]}")

    if computador == 0:
        if jogador == 0:
            print("Empate")
        elif jogador == 1:
            print("Você venceu")
        else:
            print("Você perdeu")

    elif computador == 1:
        if jogador == 0:
            print("Você perdeu")
        elif jogador == 1:
            print("Empate")
        else:
            print("Você venceu")

    else:
        if jogador == 0:
            print("Você venceu")
        elif jogador == 1:
            print("Você perdeu")
        else:
            print("Empate")

    fim = input("Deseja continuar? (s/n): ").lower()

    if fim == "n":
        break