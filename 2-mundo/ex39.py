# 39 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

print("-" * 70)
print("\tVerificação de Alistamento Militar")
print("-" * 70)

ano_atual = date.today().year
nascimento = int(input("Digite o seu ano de nascimento: "))
idade = ano_atual - nascimento
ano_alistamento = nascimento + 18

print(f"Você tem {idade} anos")

if idade > 18:
    ano_de_pendencia = ano_atual - ano_alistamento
    print(f"Você deveria ter se alistado há {ano_de_pendencia} ano(s)")
    print(f"Seu alistamento foi em {ano_alistamento}")
elif idade == 18:
    print(f"Você deve se alistar.")
else:
    anos_restantes = ano_alistamento - ano_atual
    print(f"Ainda faltam {anos_restantes} ano(s) para você se alistar")
    print(f"Seu alistamento será em {ano_alistamento}")