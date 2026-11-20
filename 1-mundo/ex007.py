# 7 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

from keyboard import wait
from os import system

nome = str(input("Digite o nome do aluno: ")).strip().title()
prova1 = int(input("Nota da Prova 1 = "))
prova2 = int(input("Nota da Prova 2 = "))
media = (prova1 + prova2) / 2

print("Pressione ENTER para continuar...")
wait("enter")
system("cls") # Limpa o terminal

print(f"Nome do aluno: {nome}")
print(f"Nota da Prova 1 = {prova1}")
print(f"Nota da Prova 2 = {prova2}")
print(f"Média final = {media}")