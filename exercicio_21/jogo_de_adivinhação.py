from random import randint
maquina = randint(0, 5)
usuario = int(input('Em que número eu pensei?:'))
if usuario == maquina:
    print("Você conseguiu adivinhar!")
else:
    print('Infelismente você não conseguiu adivinhar, pois pensei no numero {} não no {}.'.format(maquina, usuario))
