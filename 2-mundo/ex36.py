# 36 - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print("-" * 70)
print("\tSistema de Aprovação de Compra de Imóvel")
print("-" * 70)

valor_casa = float(input("Valor da casa: "))
salario_comprador = float(input("Valor do Salário do Comprador: "))
anos_prestacao = int(input("Anos a Pagar Prestação: "))

prestacoes_mensais = (anos_prestacao * 12) # Calcula o número de prestações
valor_prestacao = valor_casa / prestacoes_mensais # Calcula o valor mensal a ser pago
limite_salario = salario_comprador * 0.30 # Calcula quanto é 30% do salário do comprador

if(valor_prestacao <= limite_salario):
    print("Compra Liberada!")
    print(f"Valor das Prestações: {valor_prestacao:.2f}")
else:
    print("Compra Negada!")