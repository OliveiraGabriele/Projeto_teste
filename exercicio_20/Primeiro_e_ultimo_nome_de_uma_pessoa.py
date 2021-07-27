
nome = str(input('Digite seu nome comleto:').strip())
primeiro, ultimo = nome.split(), nome.split()
print('Primeiro nome: {}'.format(primeiro[0]),('\nUltimo nome: {}'.format(ultimo[len(ultimo)-1])))