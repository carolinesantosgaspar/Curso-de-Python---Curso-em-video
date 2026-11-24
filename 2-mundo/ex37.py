# 37 - Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

print("-" * 50)
print("\t Conversão de Bases")
print("-" * 50)

x = int(input("Digite um número inteiro: "))
print("- Escolha uma das bases para conversão -")
print("[1] - Binário\n[2] - Octal\n[3] - Hexadecimal")
conversao = int(input("Conversão: "))

match conversao:
    case 1:
        print("Convertendo para Binário")
        binario = bin(x)[2:]
        print(f"Número: {x}")
        print(f"Binário: {binario}")

    case 2:
        print("Convertendo para Octal")
        octal = oct(x)[2:]
        print(f"Número: {x}")
        print(f"Octal: {octal}")

    case 3: 
        print("Convertendo para Hexadecimal")
        hexadecimal = hex(x)[2:]
        print(f"Número: {x}")
        print(f"Hexadecimal: {hexadecimal}")    

    case _:
        print("\aERRO!")
        print("Encerrando O Programa")
