numero_secreto = 12
acertou = False

while not acertou:
    palpite = int(input("Digite um número entre 1 e 100: "))

    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número secreto!")
        acertou = True
    elif palpite < numero_secreto:
        print("O número secreto é maior. Tente novamente.")
    else:
        print("O número secreto é menor. Tente novamente.")

print("Fim do jogo")