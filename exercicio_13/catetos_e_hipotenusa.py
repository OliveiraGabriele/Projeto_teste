oposto = float(input('Digite o comprimento do cateto oposto:'))
adjacente = float(input('Digite o comprimento do cateto adjacente:'))
cal1 = (oposto**2 + adjacente**2) ** (1/2)
print('O comprimento da hipotenusa é de {:.2f}'.format(float(cal1)))