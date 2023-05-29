"""
Faça um programa em python de um autômato finito determinístico
que permita a entrada do alfabeto, dos estados, do estado inicial,
dos estados de aceitação, do delta de cada alfabeto com cada
estado e da palavra a ser verificada
"""

class AFD:
    # Vinculando os atributos com os argumentos enviados
    def __init__(self, alfabeto, estados, estado_inicial, estados_aceitacao, delta):
        self.alfabeto = alfabeto
        self.estados = estados
        self.estado_inicial = estado_inicial
        self.estados_aceitacao = estados_aceitacao
        self.delta = delta

    # Criando a verificação se a palavra é aceita pelo AFD
    def verifyWord(self, palavra):
        estado_atual = self.estado_inicial
        caminho = [estado_atual]

        for simbolo in palavra:
            if simbolo not in self.alfabeto:
                return False, caminho  # A palavra contém um símbolo inválido

            if estado_atual not in self.delta or simbolo not in self.delta[estado_atual]:
                return False, caminho  # Não há transição definida para o estado atual e o símbolo

            estado_atual = self.delta[estado_atual][simbolo]
            caminho.append(estado_atual)

        return estado_atual in self.estados_aceitacao, caminho


n = -1
while (n != 2):
    # Pedindo as informações
    alfabeto = input("Entre com o alfabeto: ").split(',')
    estados = input("Entre com os estados: ").split(',')
    estado_inicial = input("Entre com o estado inicial: ")
    estados_aceitacao = input("Entre com os estados de aceitação: ").split(',')

    # Obtendo as transições delta
    delta = {}
    for estado in estados:
        delta[estado] = {}
        for simbolo in alfabeto:
            transicao = input(f"Delta({estado},{simbolo}): ")
            delta[estado][simbolo] = transicao


    # Criando o autômato
    afd = AFD(alfabeto, estados, estado_inicial, estados_aceitacao, delta)

    x = -1
    while (x != 1):

        # Verifica a palavra
        palavra = input("Entre com a palavra a ser verificada: ")
        # Verifica a palavra e obtém o caminho percorrido
        aceita, caminho = afd.verifyWord(palavra)



        if aceita:
            print("A palavra é aceita pelo autômato!")
            print("\nCaminho:")
            print("---".join(caminho))
        else:
            print("A palavra não é aceita pelo autômato!")
            print("\nCaminho:")
            print("---".join(caminho))
        x = int(input("\nDigite um valor diferente de 1 para testar uma nova palavra : "))
    n = int(input("\nDigite um valor diferente de 2 para testar novo automato: "))
