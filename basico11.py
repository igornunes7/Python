#Escreva um programa em que o usuário insira uma string e o programa deve
#imprimir "SIM" se a string conter pelo menos um caractere maiúsculo e "NÃO" caso
#contrário. Exemplo de entrada e saída para teste


str = input("Digita ai: ")
aux = 0

for char in str:
    if (char.isupper()):
        aux = aux + 1

if aux >= 1:
    print ("SIM")
else:
    print ("NAO")
        
