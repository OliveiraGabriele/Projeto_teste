a = float(input('Primeiro comprimento:'))
b = float(input('Segundo comprimento:'))
c = float(input('Terceiro comprimento:'))
if a < b + c  and b < a + c and c < a + b:
    print('Com as medidas {}, {} e  {} � poss�vel formar um tri�ngulo!'.format(a, b, c))
else:
  print('Com as medidas {}, {} e {} n�o � poss�vel formar um trin�ngulo!'.format(a, b, c))