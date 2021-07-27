frase = input('Digite uma frase:').upper().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('Apareceu na posição {} na primeira vez'.format(frase.find('A')+1))
print('Apareceu na posição {} na última vez'.format(frase.rfind('A')+1))
