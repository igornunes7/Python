from random import randint

maquina = randint(0 , 50)
print ("PENSANDO EM UM NÚMERO DE 0 A 50...")

print ("TENTE ADVINHAR NO NUMERO QUE PENSEI")

while True:
    numero = int(input("Digite o número que você deseja: "))
    if numero < 0 and numero > 50:
        print ("Numéro inválido. Tente novamente: ")
    else:
        if numero == maquina:
            print ("Você acertou o número!")
            break
        else:
            if numero < maquina:
                print ("Quasee! Tente um número um pouco mais pra cima")
            else:
                print ("Quasee! Tente um número um pouco mais pra baixo")
