import random
n1 = input('Digigite o primeiro nome:')
n2 = input('Digigite o  segundo nome:')
n3 = input('Digigite o  terceiro nome:')
n4 = input('Digigite o quarto nome:')
nomes = n1, n2 ,n3, n4
print(' O nome sorteado foi {}'.format(random.choice(nomes)))