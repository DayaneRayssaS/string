import forca
import adivinhacao

    def escolha_jogos():
    print("******")
        print("**escolha o jogo**")
        print("*****")
        print("(1)forca, (2)adivinhacao")
        jogo = int(input("qual jogo gostaria de jogar"))

        if (jogo == 1):
            print("jogando forca")
            forca.jogar()
        elif(jogo == 2):
            print("jogando adivinhacao")
            adivinhacao.jogar()

    if(__name__== "__main__"):
    escolhe_jogo()
