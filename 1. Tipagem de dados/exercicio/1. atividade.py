# um algoritimo ler 2 numeros(soma, subtracao, multiplicacao, divisao)
import os

os.system("cls || clear")

num1: int 
num2: int 
soma: int
subtr: int
multi: int
divi: float

num1 = int (input("Digite o primeiro numero: "))
num2 = int (input("Digite o segundo numero: "))

soma = num1 + num2
subtr = num1 - num2
multi = num1 * num2
divi = num1 / num2

print(" ===Resultado=== ")
print(f"PrimeiroNumero: {num1}")
print(f"SegundoNumero: {num2}")
print(f"soma: {soma}")
print(f"Subtracao: {subtr}")
print(f"Multiplicacao: {multi}")
print(f"Divisao: {divi}")
