"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horario = input("Que horas são? ")

if (horario.isdigit()):
    horarioInt = int(horario)
    if (horarioInt >= 0 and horarioInt <= 11):
        print ("Bom dia")
    elif (horarioInt >= 12 and horarioInt <= 17):
        print ("Boa tarde")
    elif (horarioInt >= 18 and horarioInt <= 23):
        print ("Boa noite")
    else:
        print ("Hora inválida")
else:
    print ("Coloque apenas digitos")
