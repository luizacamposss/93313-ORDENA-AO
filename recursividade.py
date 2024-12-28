import os
from time import sleep
os.system("cls || clear")

"""
Criando uma função para contagem regressiva.
Iniciando contagem com o número 10
"""


# def contagem_regressiva(numero):
#     for i in range(numero, 0, -1):
#         print(f"Contagem.: {i}")
#         sleep(1)

def contagem_regressiva(numero):
    if numero < 0:
        return 
    print(numero)
    sleep(1)

    contagem_regressiva(numero -1)

contagem_regressiva(10)


    