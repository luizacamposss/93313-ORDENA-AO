"""
Solicite que o usuário insira em uma lista cinco nomes e mostre na ordem alfabética.
"""

import os
os.system("cls || clear")

lista_nomes = []

# Entrada.
print("=== Solicitando dados para o usuário ===")

for i in range(5):
    nome = input("Digite um nome: ")
    lista_nomes.append(nome)

# Processamento
print("\nOrdenando lista...")
lista_ordenada = sorted(lista_nomes)

print("=== Saída ===")
print("Lista Original: ")
print(lista_nomes)

print("\nLista Ordenada: ")
for nome in lista_ordenada:
    print(nome)