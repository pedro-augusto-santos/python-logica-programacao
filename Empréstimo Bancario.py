from time import sleep

print("-=" * 20)
print(f"{'EMPRÉSTIMO BANCÁRIO':^40}")
print("-=" * 20)

vcasa = float(input(("Qual o valor da sua casa ?: ")))
salario = float(input(("Qual o seu salário ? : ")))
tempo = int(input(("Em quantos anos você pretende pagar a sua casa ? : ")))

prestacao = vcasa/(12*tempo)
limite = (0.30 * salario)

print("\nCARREGANDO VALORES...")
sleep(2)

if prestacao <= limite:
    print(f"Empréstimo aprovado! Parcela de R$ {prestacao:.2f}")
else:
    print(f"Empréstimo negado. A parcela de R$ {prestacao:.2f} excede 30% do seu salário")
