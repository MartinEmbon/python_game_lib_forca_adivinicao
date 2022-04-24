
import random 

def imprime_abertura():
    print("********************")
    print("***Bem vindo no jogo de Forca***")
    print("********************")

def carga_palavra_secreto():
    arquivo = open("palavras.txt","r")
    palavras=[]
    for linha in arquivo:
        linha=linha.strip()
        palavras.append(linha)
    arquivo.close()
    numero = random.randrange(0,len(palavras))
    #print(palavras)
    palavra_secreta = palavras[numero].upper()
    #print(palavra_secreta)
    return palavra_secreta

def msg_perdeu():
    print("Perdeu`!")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def jogar_forca():
    imprime_abertura()
    palavra_secreta = carga_palavra_secreto()
    
    letras_acertadas = []
    enforcou = False 
    acertou = False 
    erros = 0

    for letra in palavra_secreta:
        letras_acertadas.append("_")
    

    print(letras_acertadas)
    while (not enforcou and not acertou):
        chute = input("Qual letra: ")
        chute = chute.strip().upper()
        if chute in palavra_secreta:            
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                # print(f'Encontrei a {letra} na posicião {index}')
                    letras_acertadas[index]=letra
                index = index +1
        else:
            erros = erros + 1
            desenha_forca(erros)
       
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

        if acertou:
            imprime_mensagem_vencedor()
        else:
            #msg_perdeu()
            #imprime_mensagem_perdedor(palavra_secreta)
            continue
        print(letras_acertadas) 

    print("fin do jogo")


if(__name__=="__main__"):
    jogar_forca()
