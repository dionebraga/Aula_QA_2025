frutas = ["maçã", "banana", "laranja", "pera", "uva"]
alergias = ["morango", "kiwi"]

# Usuário escolhe uma fruta
nova_alergia = input("Digite uma fruta que causa alergia: ")
alergias.append(nova_alergia)

# Verificando frutas que estão nas duas listas
for fruta in frutas:
    if fruta in alergias:
        print(f"Atenção: {fruta} está na lista de alergias!")