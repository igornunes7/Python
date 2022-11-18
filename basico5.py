"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input("Digite um número inteiro: ")

if (numero.isdigit()):
    numeroInteiro = int(numero)
    if (numeroInteiro % 2 == 0):
        print (f"{numeroInteiro} é par")
    else:
        print (f"{numeroInteiro} é ímpar")
else:
    print ("Não é um número inteiro")
