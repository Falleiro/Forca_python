def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
    palavra_secreta = "Banana".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    enforcou = False
    acertou = False
    erros = 0
    print(letras_acertadas)

    while (not enforcou and not acertou):

        index = 0
        chute = input("Digite uma letra:").strip().upper()
        if (chute in palavra_secreta):
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = chute
                index += 1
        else:
            erros += 1
            if(erros == 6):
                print("Que pena, você perdeu.")
            else:
                print("Você errou, faltam {} tentativas".format(6-erros))
        print(letras_acertadas)
        if("_"not in letras_acertadas):
            acertou = True
            print("Parabéns, você ganhou!")
    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()
