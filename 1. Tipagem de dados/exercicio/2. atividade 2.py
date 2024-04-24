#elabora algoritimo pra ler nome 2 notas (media) (nome idade  notas media)

import os

os.system("cls || clear")

nome: str
idade: int
nota1: float
nota2: float
media: float

nome = str (input("Digite o seu nome: "))
idade = int (input("Digite a sua idade: "))
nota1 = float (input("Digite a sua 1° nota: "))
nota2 = float (input("Digite a 2° nota: "))

media = float (nota1 + nota2) / 2

print("\n")
print("=== Resutado ===")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"1° Nota: {nota1}")
print(f"2° Nota: {nota2}")
print(f"Media: {media}")


