import random

def jogar_rodada():
    
    print("********************")
    print("***Bem vindo no jogo de Forca***")
    print("********************")

    numero_secreto = random.randrange(0,10)
    total_tentativas = 0
    pontos = 1000

    print("Qual nivel dificultade")
    print("(1) Fácil, (2) Medio, (3) Dificil")

    nivel = int(input("Defina o nível: "))

    if nivel == 1:
        total_tentativas=20
    elif nivel == 2:
        total_tentativas=10
    else:
        total_tentativas=5

    for rodada in range(total_tentativas):   
        print(f'Tentativa {rodada+1} de {total_tentativas}')
        chute = int(input("Digite o seu numero entre 1 e 100: "))   
        if chute < 1 or chute > 100:
            print("Deve digitar num entre um e 100")
            continue 
        if chute == numero_secreto:
            print(f'Ganhou! Você digitou o {chute} e fez {pontos}')
            break
        elif chute == 30:
            print(f"Chutou para baixo!")        
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            print("Final do jogo")      

    print(f'o numero secreto foi {numero_secreto}')

if(__name__=="__main__"):
    jogar_rodada()