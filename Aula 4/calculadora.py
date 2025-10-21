num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))

operacao = input("Insira a operação que deseja realizar (somar, subtrair, multiplicar, dividir, potencializar): ").lower()

if operacao == "multiplicar":
    print(num1 * num2)

elif operacao == "somar":
    print(num1 + num2)

elif operacao == "dividir":
    if num2 == 0:
        print("Erro: não é possível dividir por zero.")
    else:
        print(num1 / num2)

elif operacao == "subtrair":
    print(num1 - num2)

elif operacao == "potencializar":
    print(num1 ** num2)

else:
    print("Operação inválida. Escolha entre: somar, subtrair, multiplicar, dividir ou potencializar.")
