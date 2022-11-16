#Exercicio: comparar 2 valores dados pelo usuário e dizer se eles são iguais, se um é maior ou menor que o outro

primeiroValor = int(input("Digite o primeiro valor: "))
segundoValor = int(input("Digite o segundo valor: "))
linha1 = f'O primeiro valor {primeiroValor} é maior que o segundo valor {segundoValor}'
linha2 = f'O segundo valor {segundoValor} é maior que o primeiro valor {primeiroValor}'
linha3 = f'Os valores {primeiroValor} e {segundoValor} sao iguais'

if (primeiroValor > segundoValor):
    print(linha1)
elif (primeiroValor < segundoValor):
    print(linha2)
else:
    print(linha3)
