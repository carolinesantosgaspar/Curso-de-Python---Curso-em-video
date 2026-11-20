# 5 - Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

x = int(input("Digite um número: "))

antecessor = x - 1
sucessor = x + 1

print(f"Antecessor: {antecessor}")
print(f"Número digitado: {x}")
print(f"Sucessor: {sucessor}")