""""

# 041 - A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER

"""

from datetime import date 

def atribuindo_categoria(idade: int):
    categoria = int
    match idade:
        case idade if idade >= 1 and idade <= 9:
            categoria = 1 # 1 = Mirim
        case idade if idade > 9 and idade <= 14:
            categoria = 2 # 2 = Infantil
        case idade if idade > 14 and idade <= 19:
            categoria = 3 # 3 = Júnior
        case idade if idade > 19 and idade <= 25:
            categoria = 4 # 4 = Sênior
        case _:
            categoria = 5 # 5 = Master

    return categoria

def main():

    ano_atual = date.today().year
    ano_nascimento = int(input("Ano de Nascimento: "))
    idade = ano_atual - ano_nascimento
    categoria = atribuindo_categoria(idade)
    print(f"Idade do Atleta: {idade}")
    match categoria:
        case 1:
            print("Categoria = Mirim") 
        case 2:
            print("Categoria = Infantil")
        case 3:
            print("Categoria = Júnior")
        case 4:
            print("Categoria = Sênior")
        case 5:
            print("Categoria = Master")

main()