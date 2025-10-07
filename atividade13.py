# Peça ao usuário para digitar 3 notas e armazene em uma lista. Depois, calcule a média dessas notas.
notas = [float(input("Digite uma nota: ")), float(input("Digite outra nota: ")), float(input("Digite outra nota: "))]
media = (notas[0] + notas[1] + notas[2]) /3
print(f"{media:.2f}")
