km = float(input(' Qual foi a quantidade de km percorridos por dia com o carro alugado?'))
dias = int(input('O carro foi alugado por quantos dias?'))
resultado = (60 * dias) + 0.15 * km
print ('O pre�o a se pagar pelo carro � de R$ {:.2f}'.format(resultado)) 