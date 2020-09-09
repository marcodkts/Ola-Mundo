import random

def jogar():

    print('********************************')
    print('***Bem vindo ao jogo da Forca***')
    print('********************************')

    opcoes = ('cachorro','gato','peixe','tartaruga','passarinho')
    palavra_secreta = list(random.choice(opcoes))
    palavra = [0]*len(palavra_secreta)
    for i in range(len(palavra_secreta)):
        palavra[i] = "_"
        print (palavra[i], end = ' ')

    tentativa = 1
    print ()
    while (tentativa <= 6):
        erro = 0

        print()
        print("Tentativa número ", tentativa, end="\n\n")
        chute = input("Digite uma letra: ")
        print ()
        for i in range(len(palavra_secreta)):
            if (chute == palavra_secreta[i]):
                palavra[i] = palavra_secreta[i]
            else:
                erro = erro + 1

        if (erro >= len(palavra_secreta)):
            tentativa = tentativa + 1
        
        for i in range(len(palavra_secreta)):
            print (palavra[i], end = ' ')
        print ()

        if (palavra == palavra_secreta):
            print ()
            print("Parabéns, você acertou!")
            break

    print ()
    print ('Fim de Jogo')

if(__name__ == '__main__'):
    jogar() 