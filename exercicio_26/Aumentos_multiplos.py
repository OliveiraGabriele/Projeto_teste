salario = float(input('Digite um salário do funcionário:'))
if salario > 1250:
    print('O aumento foi de 10% que é {:.2f} então passará a ganhar {:.2f}'.format(salario * 10 /100, salario * 10 /100 + salario))
else:
    salario <=  1250        
    print('O aumento foi de 15% que é {:.2f} então passará a ganhar {:.2f}'.format(salario * 15 /100, salario * 15 /100 + salario))

