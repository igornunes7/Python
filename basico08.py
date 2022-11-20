"""
Faça um programa que calcule o valor a ser pago por um produto
.á vista dinheiro/cheque: 10% de desconto
.á vista no cartão: 5% de desconto
.em até 2x no cartão: preço normal
.3x ou mais no cartão: 20% de juros
"""


print ('{:-^30}'.format('LOJA'))
preço = float(input("O preço do produto é R$"))
print ('''OPÇÕES DE PAGAMENTO:
(1) À VISTA EM DINHEIRO/CHEQUE
(2) À VISTA NO CARTÃO
(3) EM ATÉ 2x NO CARTÃO
(4) 3x OU MAIS NO CARTÃO''')
opcao = int(input("Escolha uma opção: "))

if opcao == 1:
    desconto = preço - ((10 * preço) / 100)
    print ("Você escolheu pagar á vista em dinheiro/cheque")
    print ("Por escolher essa opção, você ganhará 10% de desconto")
    print ("Preço a pagar: R${:.2f}".format(desconto))
elif opcao == 2:
    desconto = preço - ((5 * preço) / 100)
    print ("Você escolheu pagar á vista no cartão")
    print ("Por escolher essa opção, você ganhará 5% de desconto")
    print ("Preço a pagar: R${:.2f}".format(desconto))
elif opcao == 3:
    total = preço / 2
    print ("Você escolheu pagar em até 2x no cartão")
    print ("Por escolher essa opção, você pagará o preço normal")
    print ("Preço a pagar: 2 parcelas de R${:.2f}".format(total))
elif opcao == 4:
    print ("Você escolheu pagar em 3x ou mais no cartão")
    print ("Por escolher essa opção, você pagará com 20% de juros")
    parcelas = int(input("Digite o numero de parcelas que você deseja: "))
    if parcelas < 3:
        print ("Número de parcelas inválido")
    else:
        juros = preço + ((20 * preço) / 100)
        parcelasPagar = juros / parcelas
        print ("Preço a pagar: {} parcelas de R${:.2f}".format(parcelas,parcelasPagar))
else:
    print ("Opção inválida! Digite um número de 1 à 4")
