from datetime import date

largura = 40
titulo = "VERIFICADOR DE IDADE"

print("-=" * 20)
print(f"{titulo:^40}")
print("-=" * 20)
print()

# Pega o ano atual automaticamente
ano_atual = date.today().year

maiores = 0
menores = 0

# O for repete o processo para 7 pessoas
for c in range(1, 8):
    
    # Garante que o input seja válido
    while True:
        # O try/except trata erros
        try:
            ano = int(input(f"Pessoa {c}, digite seu ano de nascimento: "))
            
            if ano < 1900 or ano > ano_atual:
                print("Ano fora do intervalo válido")
            else:
                break
                
        except ValueError:
            print("Digite apenas números.")

    # Calcula a idade
    idade = ano_atual - ano

    # Classifica e atualiza os contadores
    if idade >= 18:
        maiores += 1
    else:
        menores += 1

print(f"\nExistem {maiores} pessoas maiores de idade")
print(f"Existem {menores} pessoas menores de idade")