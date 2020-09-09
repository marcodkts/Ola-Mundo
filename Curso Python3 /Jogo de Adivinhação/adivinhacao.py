import random

def jogar():

    print('********************************')
    print('Bem vindo ao jogo de Adivinhação')
    print('********************************')

    numero_secreto = round(random.randrange(1,100,1))
    acerto = False
    tentativa = 1

    while (acerto == False):
        print("Tentativa número ", tentativa)
        chute = input("Digite o seu número: ")
        numero = int(chute)


        if (numero == numero_secreto) :
            print ("Você acertou!")
            acerto = True
            break

        else:

            if (numero > numero_secreto):
                print("O seu chute foi maior que o número secreto")

            elif(numero < numero_secreto):
                print("O seu chute foi menor que o número secreto")
        tentativa = tentativa + 1

    print ('Fim de Jogo')

if(__name__ == '__main__'):
    jogar()