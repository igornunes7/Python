"""
Faça um programa que gere um número aleátorio entre 0 e 50 e o usuário deve acertá-lo
"""

from random import randint
from time import sleep

maquina = randint(0 , 50)
cont = 0
print ("GERANDO UM NÚMERO ENTRE 0 E 50...")
print ("-"*40)
sleep (2.5)
print ("TENTE ADVINHAR NO NUMERO QUE PENSEI")

while True:
    numero = int(input("Digite o número que você deseja: "))
    if numero < 0 or numero > 50:
        print ("Numéro inválido. Tente novamente!")
    else:
        if numero == maquina:
            print ("Você acertou o número!")
            print ("Número de tentativas: {}".format(cont))
            break
        else:
            if numero < maquina:
                print ("Quasee! Tente um número um pouco mais pra cima")
                cont = cont + 1
            else:
                print ("Quasee! Tente um número um pouco mais pra baixo")
                cont = cont + 1
