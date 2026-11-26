"""

42) Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes

"""
def tipo_triangulo(l1: int, l2: int, l3: int):
    if l1 + l2 <= l3 or l1 + l3 <= l2 or l2 + l3 <= l1:
        return "inválido (não forma um triângulo)"
    
    if l1 == l2 and l2 == l3:
        resultado = "Equilátero"
    elif l1 == l2 or l1 == l3 or l2 == l3:
        resultado = "Isósceles"
    else:
        resultado = "Escaleno"
        
    return resultado

def main():
    l1 = int(input("Lado 1 = "))
    l2 = int(input("Lado 2 = "))
    l3 = int(input("Lado 3 = "))
    resultado = tipo_triangulo(l1, l2, l3)
    print(f"Os segmentos formam um triângulo {resultado}")

main()