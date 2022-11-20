"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Digite seu nome: ")

if (nome.isdigit()):
    print ("Digite apenas letras")
else:
    tamanhoNome = len(nome)
    if tamanhoNome <= 1:
        print ("Digite mais letras")
    else:
        if (tamanhoNome <= 4):
            print ("Seu nome é curto")
        elif (tamanhoNome >= 5 and tamanhoNome <=6):
            print ("Seu nome é normal")
        else:
            print("Seu nome é muito grande")
