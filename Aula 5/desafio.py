# 🐍 Desafio do Caique - Estruturas de Dados

# 1️⃣ Criar uma tupla com 5 dados
tupla_dados = ("banana", "maçã", "uva", "pera", "laranja")
print(f"Tupla original: {tupla_dados}\n")

# 2️⃣ Converter a tupla para uma lista (tuplas são imutáveis)
lista_dados = list(tupla_dados)
print(f"Lista convertida: {lista_dados}\n")

# 3️⃣ Inserir 2 novos dados na lista
lista_dados.append("abacaxi")   # insere no final
lista_dados.append("mamão")
print(f"Lista após inserções: {lista_dados}\n")

# 4️⃣ Remover o primeiro dado da lista
lista_dados.pop(0)  # remove o elemento de índice 0
print(f"Lista após remover o primeiro dado: {lista_dados}\n")

# 5️⃣ Remover o último dado da lista
lista_dados.pop()   # remove o último elemento
print(f"Lista após remover o último dado: {lista_dados}\n")

# 6️⃣ Exibir o primeiro dado da lista
print(f"Primeiro dado atual da lista: {lista_dados[0]}\n")

# 7️⃣ Exibir a quantidade de dados da lista
print(f"Quantidade total de dados na lista: {len(lista_dados)}\n")

# 8️⃣ Criar um dicionário com Nome, Idade e Profissão
informacoes = {
    "Nome": "Caique Silva",
    "Idade": 25,
    "Profissão": "Desenvolvedor"
}

# 9️⃣ Exibir somente o valor contido na chave 'Nome'
print(f"Nome no dicionário: {informacoes['Nome']}\n")

print("✅ Fim do desafio!")