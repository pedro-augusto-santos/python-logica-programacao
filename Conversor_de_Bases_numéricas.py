largura = 40
titulo = "CONVERSOR DE BASES NUMÉRICAS"

print("*" * largura)
print(f"{titulo:^{largura}}")
print("*" * largura)

print("\n")

while True:
    try:
        n = int(input("\nDigite um número inteiro: "))
        break 
        
    except ValueError:
        print("Erro: Por favor, digite apenas números inteiros.")


print("\n")

print("[1] Binário")
print("[2] Octal")
print("[3] Hexadecimal")

print("\n")

while True:

    conversor = int(input("Escolha um tipo de conversão: "))

    if conversor == 1:
        print(f"{n} em binário é {n:b}")
    elif conversor == 2:
        print(f"{n} em octal é {n:o}")
    elif conversor == 3:
        print(f"{n} em hexadecimal é {n:X}")
    else:
        print("Opção inválida")

    sair = input("Quer sair? (s/n): ")
    if sair == "s":
        print("Programa encerrado")
        break
       