velocidade = float(input('Qual a velocidade do carro?:'))
multa = (velocidade - 80) * 7.00
if velocidade > 80:
    print('Voc� excedeu o limite de 80km/h e foi multado no valor de R${:.2f}!'.format(multa))
print('Tenha um �timo dia e dirija com seguran�a!')