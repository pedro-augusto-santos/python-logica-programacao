largura = 40
titulo = "GERENCIADOR DE PAGAMENTOS"

print("-=" * 20 )
print(f"{titulo:^{largura}}")
print("-=" * 20 )

print("\n")

preço_do_produto = float(input("Digite o valor do produto:  "))

print("\n")

print("[1] À vista dinheiro/cheque (10% de desconto)")
print("[2] À vista no cartão (5% de desconto)")
print("[3] Em até 2x no cartão (sem juros)")
print("[4] 3x ou mais no cartão (20% de juros)")
print("\n")

forma_de_pagamento = int(input("Escolha sua forma de pagamento: "))

if forma_de_pagamento == 1:
    print(f"O preço do produto é R$ {preço_do_produto * 0.90:.2f}")
elif forma_de_pagamento == 2:
     print(f"O preço do produto é R$ {preço_do_produto * 0.95:.2f}")
elif forma_de_pagamento == 3:
     parcela = preço_do_produto/2 
     print(f"2x de R$ {parcela :.2f} (sem juros)")
elif forma_de_pagamento == 4:
     parcelas = int(input("Você deseja pagar em quantas parcelas ? "))
     if  parcelas <3:
        print("Essa opção é apenas para 3x ou mais")
     else:
         total = preço_do_produto * 1.20
         preco = total/parcelas
         #preco porque não quis repetir o nome "parcela"
         print(f"{parcelas} x de R$ {preco:.2f} com juros")
         print(f"Total: R$ {total:.2f}")
else:
    print("Opção inválida")
