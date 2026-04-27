largura  = 40
titulo = "SISTEMA DE NOTAS"

print("-=" * (largura//2))
print(f"{titulo:^{largura}}")
print("-=" * (largura//2))

print("Olá seja bem vindo ao Sistema de notas !!")

while True:
  while True:
   try:
      nota = float(input("Digite sua nota:  "))
      break
   except ValueError:
      print("Nota invalida")

      continue

  if nota > 10 or nota < 0:
      print("nota inválida")
  elif nota <= 5:
      print("Reprovado")
  elif nota < 7:
      print("Recuperação")
  else:
      print("Aluno aprovado")
      break