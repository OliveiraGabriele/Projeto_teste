frase = input('Digite uma frase:').upper().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('Apareceu na posi��o {} na primeira vez'.format(frase.find('A')+1))
print('Apareceu na posi��o {} na �ltima vez'.format(frase.rfind('A')+1))
