ano = int(input('Digite um ano:'))
if ano % 4 == 0  and ano % 100 != 0 or ano % 400 == 0: : 
    print('{} � um ano bissexto'.format(ano))
else:
  ano % 4 != 0
  print('{} N�o � um ano bissexto'.format(ano))
