# 6 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

from math import sqrt

x = int(input("x = "))

dobro = x * 2
triplo = x * 3
raiz_quadrarada = sqrt(x)

print(f"Número digitado = {x}")
print(f"Dobro de {x} = {dobro}")
print(f"Triplo de {x} = {triplo}")
print(f"Raiz quadrada de {x} = {raiz_quadrarada:.2f}")