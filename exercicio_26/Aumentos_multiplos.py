salario = float(input('Digite um sal�rio do funcion�rio:'))
if salario > 1250:
    print('O aumento foi de 10% que � {:.2f} ent�o passar� a ganhar {:.2f}'.format(salario * 10 /100, salario * 10 /100 + salario))
else:
    salario <=  1250        
    print('O aumento foi de 15% que � {:.2f} ent�o passar� a ganhar {:.2f}'.format(salario * 15 /100, salario * 15 /100 + salario))

