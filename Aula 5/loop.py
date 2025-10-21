# Exibindo os elementos de uma lista
lista_frutas = ['banana', 'maçã', 'pera', 'banana']

print("Percorrendo a lista de frutas:\n")
for fruta in lista_frutas:
    print(f"🍎 Fruta: {fruta}")

# Exibindo as chaves e valores de um dicionário
dados_pessoais = {"nome": "Caique", "idade": 22}

print("\nPercorrendo as chaves do dicionário:\n")
for chave in dados_pessoais.keys():
    print(f"🔑 Chave: {chave}")

print("\nPercorrendo os valores do dicionário:\n")
for valor in dados_pessoais.values():
    print(f"📘 Valor: {valor}")

# Explicação didática no final (comentários)
"""
💡 Conceitos importantes:

1️⃣ Listas:
   - Estruturas ordenadas e mutáveis.
   - Ao iterar (for), percorremos cada item da lista em sequência.

2️⃣ Strings:
   - São iteráveis. Cada character pode ser acessado individualmente.

3️⃣ Tuplas:
   - Estruturas ordenadas e imutáveis.
   - Iterar percorre os elementos na ordem em que foram definidos.

4️⃣ Conjuntos (Sets):
   - Estruturas não ordenadas e sem valores repetidos.
   - Ao iterar, a ordem não é garantida.

🧠 Boas práticas aplicadas:
- Nomes de variáveis em snake_case (letras minúsculas e separadas por underscore).
- Mensagens claras e emojis para facilitar a leitura no terminal.
- Separação visual com quebras de linha (\n).
- Comentários explicativos curtos e objetivos.
"""