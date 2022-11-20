"""
Desenvolva um programa que pergunte a distância de uma viagem 
em KM. Calcule o preço da passagem,cobrando R$0,50 por KM para
viagens em até 200Km e R$0,45 para viagens mais longas
"""

from time import sleep

distancia = float(input("Digite, em Km, a distancia da sua viagem: "))

print("{:-^50}".format("CALCULANDO O PREÇO DA SUA PASSAGEM"))
sleep(2.5)

if distancia <= 200:
    preço = distancia * 0.5
    print ("A sua viagem terá {:0.1f}Km".format(distancia))
    print("A sua passagem irá custar: R${:0.2f}".format(preço))
else:
    preço = distancia * 0.45
    print ("A sua viagem terá {:0.1f} Km".format(distancia))
    print("A sua passagem irá custar: R${:0.2f}".format(preço))
