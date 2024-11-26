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

# Entrada
print("=== Solicitando dados para o usuário ===")
while True:
    nome_frutas = input("Digite um nome de uma fruta: ")
    if nome_frutas.lower() == "sair":
        break
    else:
        lista_frutas.append(nome_frutas)

# Processamento
print("\nOrdenando lista...")
lista_ordenada = sorted(lista_frutas)
lista_inversa = sorted(lista_frutas, reverse=True)

# Saída 
def lista_original():
    print("=== Saída ===")
    print("Lista Original: ")
    print(lista_frutas)

def lista_ordenada():
    print("\nLista Ordenada: ")
    print(lista_ordenada)

def lista_inversa():
    print("\nLista Inversa: ")
    print(lista_inversa)    

lista_original()
lista_ordenada()
lista_inversa()

