# 38 - Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))

if x > y:
    print("X é maior do que Y")
elif x == y:
    print("X e Y são iguais")
else:
    print("X é menor do que Y")