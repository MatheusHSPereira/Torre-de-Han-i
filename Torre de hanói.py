def tabuleiro(casas):
    print('')
    print('\t [    %s    ]           [    %s    ]          [    %s    ]      ' % (casas[0], casas[1], casas[2]))
    print('\t [    %s    ]           [    %s    ]          [    %s    ]      ' % (casas[3], casas[4], casas[5]))
    print('\t [    %s    ]           [    %s    ]          [    %s    ]      ' % (casas[6], casas[7], casas[8]))
    print('')
casas = [1,'-','-',
         2,'-','-',
         3,'-','-']

print('Torre de Hanói')
print('')
print('Este é o tabuleiro:')
tabuleiro(casas)
print('O seu objetivo e mover as peças de lugar usando as regras de pilhas')
print('Boa sorte :D')

x = 0
while x != 'fim':
	jogada = int(input('Digite o numero da peça a ser movida: '))
	if jogada != 1 and jogada != 2 and jogada != 3:
		print('Valor invalido!!!')
		exit()
	elif casas[0] == 1 and casas[3] == 2 and casas[6] == 3:
		if jogada != 1:
                    print('Valor invalido!!!')
	elif casas[3] == 1 and casas[6] == 2:
		if jogada != 1:
                    print('Valor invalido!!!')
	elif casas[4] == 1 and casas[7] == 2:
		if jogada != 1:
                    print('Valor invalido!!!')
	elif casas[5] == 1 and casas[8] == 2:
		if jogada != 1:
                    print('Valor invalido!!!')
	elif casas[3] == 1 and casas[6] == 3:
		if jogada != 1:
                    print('Valor invalido!!!')
	elif casas[4] == 1 and casas[7] == 3:
		if jogada != 1:
                    print('Valor invalido!!!')
	elif casas[5] == 1 and casas[8] == 3:
		if jogada != 1:
                    print('Valor invalido!!!')
	elif casas[3] == 2 and casas[6] == 3:
		if jogada != 2:
                    print('Valor invalido!!!')
	elif casas[4] == 2 and casas[7] == 3:
		if jogada != 2:
                    print('Valor invalido!!!')
	elif casas[5] == 2 and casas[8] == 3:
		if jogada != 2:
                    print('Valor invalido!!!')
        else:
            jogada2 = int(input('Agora digite onde sera sua nova posiçao: '))
            if casas[jogada2 - 1] != '-':
                print('Valor invalido!!!')
            else:
                casas[jogada2 - 1] = jogada
                remover = casas.index(jogada)
                casas[remover] = '-'

        if casas[1] == 1 and casas[4] == 2 and casas[7] == 3:
            x = 'fim'
            print('Parabens voce conseguiu!!!')
            print('Saindo...')		
            exit()
        elif casas[2] == 1 and casas[5] == 2 and casas[8] == 3:
            x = 'fim'
            print('Parabens voce conseguiu!!!')
            print('Saindo...')		
            exit()
