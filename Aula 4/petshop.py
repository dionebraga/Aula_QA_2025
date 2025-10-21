nome = input("Digite o nome do seu pet: ")
idade_humana = int(input("Digite a idade humana do seu pet: "))
porte = input("Digite o porte do seu pet (pequeno, médio, grande): ").lower()
banhos = int(input("Digite o número de banhos que seu pet tomou este mês: "))

idade_cachorro = idade_humana * 7

if porte == "pequeno":
    valor_banho = 30
    custo_banho = 20
elif porte == "médio":
    valor_banho = 50
    custo_banho = 35
elif porte == "grande":
    valor_banho = 70   
    custo_banho = 50 
else:
    print("Porte inválido. Por favor, escolha entre pequeno, médio ou grande.")
    exit()

lucro_por_banho = valor_banho * custo_banho
lucro_total = lucro_por_banho * banhos

# Saída final
print(f"Olá, {nome} tem {idade_cachorro} anos e nos últimos 12 meses o lucro com este animal foi de R${lucro_total:.2f}.")