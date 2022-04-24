import forca 
import rodada

def escolhe_jogo():
    print("********************")
    print("***Escolha o seu jogo***")
    print("********************")

    print("(1) Forca (2)Adivinicaçao")
    jogo=int(input("Qual jogo: "))

    if jogo == 1:
        print("jogando forca")
        forca.jogar_forca()
    elif jogo == 2:
        print("jogando adivinção")
        rodada.jogar_rodada()

if(__name__=="__main__"):
    escolhe_jogo()