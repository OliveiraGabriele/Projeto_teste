numero = int(input('Digite um n�mero:'))
a, b = numero * 2, numero * 3    
import math 
d = math.sqrt(numero)
print(' o dobro de  {} � {} \n o triplo de {} � {} \n e a raiz quadrada de {} � {:.2f}.'.format(numero, a, numero, b,numero, d))