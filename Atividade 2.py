"""
Dada uma lista de palavras, escreva um programa que receba uma lista de frutas e mostre:

- a lista original
- a lista ordenada
- a lista na ordem inversa

Caso o usuário digite sair, para de solicitar dados.

REFATORANDO CÓDIGO:
Crie uma função para:

- Ordenação
- Ordenação inversa
"""

import os
os.system("cls || clear")

lista_frutas = []

# Saída 
def lista_original(n1):
    print("Lista Original: ")
    print(n1)

def lista_ordenadas(n1):
    print("\nLista Ordenada: ")
    print(sorted(n1))
    
def lista_inversas(n1):
    print("\nLista Inversa: ")   
    print(sorted(n1, reverse=True))

def menu():
    print("="*40)
    print(f"{'Senai':^40}")
    print("="*40)
    print("""
    1 - Lista Original      
    2 - Lista Ordenada
    3 - Lista Inversa
    4 - Nenhuma das opções acima.
          """)

# Processamento

while True:
    fruta = input("\nDigite uma fruta para adicionar à lista: ").strip()
    lista_frutas.append(fruta)
    os.system("cls || clear")
    menu()
    opcao = int(input("Digite qual a lista que vc deseja ver: "))
    match opcao:
        case 1:
            lista_original(lista_frutas)
        case 2:
            lista_ordenadas(lista_frutas)
        case 3:
            lista_inversas(lista_frutas)
        case 4:
            print("Nenhuma das opções acima, ok!")
            break

 
# Solicitar a entrada de frutas


