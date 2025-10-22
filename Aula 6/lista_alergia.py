# Listas de frutas e alergias
frutas = ["maçã", "banana", "laranja", "pera", "uva"]
alergias = ["morango", "kiwi"]

# Adicionando uma fruta da lista de frutas na lista de alergias
alergias.append(frutas[1])  # adiciona a banana, por exemplo

# Verificando se há frutas alérgicas
for fruta in frutas:
    if fruta in alergias:  # verifica se a fruta está na lista de alergias
        print(f"Atenção: {fruta} está na lista de alergias!")

print("Verificação de alergias concluída!")