import random

opcoes = ('cachorro','gato','peixe','tartaruga','passarinho')
palavra_secreta = list(random.choice(opcoes))
palavra = [0]*len(palavra_secreta)


for i in range(len(palavra_secreta)):
    palavra[i] = "_"
    print (palavra[i], end = ' ')
print()
print (palavra_secreta)
print (len(palavra_secreta))
