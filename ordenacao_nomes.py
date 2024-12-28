"""
Insira em uma lista cinco nomes e mostre na ordem alfabética.
"""

import os
os.system("cls || clear")

lista_numeros = ["Luiza", "Jaqueline", "Ricardo", "Pedro, Tainá"]

lista_organizada = sorted(lista_numeros)

print("Lista original: ")
print(lista_numeros)

print("\nLista ordenada: ")
print(lista_organizada)