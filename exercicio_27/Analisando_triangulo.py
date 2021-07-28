a = float(input('Primeiro comprimento:'))
b = float(input('Segundo comprimento:'))
c = float(input('Terceiro comprimento:'))
if a < b + c  and b < a + c and c < a + b:
    print('Com as medidas {}, {} e  {} é possível formar um triângulo!'.format(a, b, c))
else:
  print('Com as medidas {}, {} e {} não é possível formar um trinângulo!'.format(a, b, c))