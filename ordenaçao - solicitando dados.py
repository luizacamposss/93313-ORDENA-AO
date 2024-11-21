import os
os.system("cls || clear")

lista_nomes = []

# Entrada.
print("=== Solicitando dados para o usuário ===")
while True:
    nome = input("Digite um nome: ")
    if nome.lower() == "sair":
        break
    else:
        lista_nomes.append(nome)

# Processamento
print("\nOrdenando lista...")
lista_ordenada = sorted(lista_nomes)
lista_inversa = sorted(lista_nomes, reverse=True)
# Saída 
print("=== Saída ===")
print("Lista Original: ")
print(lista_nomes)

print("\nLista Ordenada: ")
print(lista_ordenada)

print("\nLista Inversa: ")
print(lista_inversa)