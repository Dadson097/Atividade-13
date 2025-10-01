# Peça ao usuário para digitar 3 notas e armazene em uma lista. Depois, calcule a média dessas notas.
nota1 = float(input("Digite uma nota:  "))
nota2 = float(input("Digite outra nota: "))
nota3 = float(input("Digite outra nota: "))
notas = [nota1,nota2,nota3]
print(f"As notas dos alunos foram:\n{notas} e a média foi: {(nota1+nota2+nota3)/3:.2f}")