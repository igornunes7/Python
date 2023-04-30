#Escreva uma função que receba uma string como entrada e retorne o número de
#palavras nessa string . Considere que uma palavra é definida como uma sequência de
#caracteres alfanuméricos separados por um ou mais caracteres não alfanuméricos.


import re

string = input("Digite a frase: ")

palavras = re.findall(r'\w+', string)

cont = len(palavras)

print (cont)
