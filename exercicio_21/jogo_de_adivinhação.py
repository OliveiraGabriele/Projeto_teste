from random import randint
maquina = randint(0, 5)
usuario = int(input('Em que n�mero eu pensei?:'))
if usuario == maquina:
    print("Voc� conseguiu adivinhar!")
else:
    print('Infelismente voc� n�o conseguiu adivinhar, pois pensei no numero {} n�o no {}.'.format(maquina, usuario))
