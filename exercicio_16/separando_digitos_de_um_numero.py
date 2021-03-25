num = int(input('Digite um número:'))
print('Unidade:{}'.format(num // 1 % 10),'\nDezena:{}'.format(num // 10 % 10),'\nCentena:{}'.format(num // 100 % 10),'\nMilhar:{}'.format(num // 1000 % 10))