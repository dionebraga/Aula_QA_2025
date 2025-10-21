print("Percorrendo a lista de frutas:\n")

# Função que percorre e retorna uma lista de frutas
def frutas():
    lista_de_frutas = ["maçã", "banana", "uva", "laranja", "mamão"]
    for fruta in lista_de_frutas:
        print(fruta)
    return lista_de_frutas

# Executando a função
frutas()

print("\nExibindo o elemento selecionado da lista:\n")

# Criando uma nova lista
frutas_lista = ["maçã", "banana", "uva"]

# Adicionando frutas com append()
frutas_lista.append("laranja")
frutas_lista.append("pera")

# Recebendo nova fruta pelo input do usuário
nova_fruta = input("Insira uma nova fruta: ")
frutas_lista.append(nova_fruta)

# Exibindo a fruta recém-adicionada (último item da lista)
print(f"\nFruta adicionada com sucesso: {frutas_lista[-1]}")

# Exibindo a lista final completa
print(f"Lista final de frutas: {frutas_lista}")