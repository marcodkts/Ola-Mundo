print('********************************')
print('Bem vindo ao jogo de Adivinhação')
print('********************************')


acerto = False
tentativa = 1
numero_secreto = 42

while (acerto == False):
    print("Tentativa número ", tentativa)
    chute = input("Digite o seu número: ")
    numero = int(chute)


    if (numero == numero_secreto) :
        print ("Você acertou!")
        acerto = True
        print ("Fim de Jogo")

    else:

        if (numero > numero_secreto):
            print("O seu chute foi maior que o número secreto")

        elif(numero < numero_secreto):
            print("O seu chute foi menor que o número secreto")
    tentativa = tentativa + 1
        