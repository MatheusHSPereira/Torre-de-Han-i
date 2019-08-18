import sys

h1 = []
h2 = []
h3 = []

def tabuleiro():
    print('')
    print('Haste 1:',h1)
    print('Haste 2:',h2)
    print('Haste 3:',h3)
    print('')
    
print('--------------------------TORRE DE HANOI--------------------------')
print('')
print('O seu objetivo e mover as peças de lugar usando as regras de pilhas')
print('Boa sorte :D')
print('')

numero = int(input('Digite a quantidade de peças que voce deseja jogar: '))
for peça in range(1, numero + 1):
    h1.append(peça)
while True:
    if len(h1) == 0 and len(h2) == 0:
        print('')
        print('PARABENS, VOCE GANHOU!!!!')
        print('')
        print('Saindo...')
        exit()
    else:
        tabuleiro()
        jogada = int(input('Digite a haste que voce deseja mover peças: '))
        while jogada != 1 and jogada != 2 and jogada != 3:
            print('Valor invalido!!!')
            jogada = int(input('Digite a haste que voce deseja mover peças: '))
        if jogada == 1:
            if len(h1) == 0:
                print('Valor invalido!!!')
                print('Saindo...')
                exit()
        elif jogada == 2:
            if len(h2) == 0:
                print('Valor invalido!!!')
                print('Saindo...')
                exit()
        elif jogada == 3:
            if len(h3) == 0:
                print('Valor invalido!!!')
                print('Saindo...')
                exit()
        jogada2 = int(input('Digite para que haste voce deseja jogar: '))
        while jogada2 != 1 and jogada2 != 2 and jogada2 != 3:
            print('Valor invalido!!!')
            jogada2 = int(input('Digite para que haste voce deseja jogar: '))
        if jogada == 1:
            if len(h1) == 0:
                print('Valor invalido!!!')
                print('Saindo...')
                exit()
        elif jogada == 2:
            if len(h2) == 0:
                print('Valor invalido!!!')
                print('Saindo...')
                exit()
        elif jogada == 3:
            if len(h3) == 0:
                print('Valor invalido!!!')
                print('Saindo...')
                exit()
            
        ##MOVIMENTO

        if jogada == 1:
            if jogada2 == 2:
                h2.insert(0, h1[0])
                del(h1[0])
                if len(h2) >= 2:
                    if max(h2) == h2[0]:
                        print('MOVIMENTO INVALIDO!!!')
                        h1.insert(0, h2[0])
                        del(h2[0])                
            elif jogada2 == 3:
                h3.insert(0, h1[0])
                del(h1[0])
                if len(h3) >= 2:
                    if max(h3) == h3[0]:
                        print('MOVIMENTO INVALIDO!!!')
                        h1.insert(0, h3[0])
                        del(h3[0])  
            else:
                pass
        elif jogada == 2:
            if jogada2 == 1:
                h1.insert(0, h2[0])
                del(h2[0])
                if len(h1) >= 2:
                    if max(h1) == h1[0]:
                        print('MOVIMENTO INVALIDO!!!')
                        h2.insert(0, h1[0])
                        del(h1[0])  
            elif jogada2 == 3:
                h3.insert(0, h2[0])
                del(h2[0])
                if len(h3) >= 2:
                    if max(h3) == h3[0]:
                        print('MOVIMENTO INVALIDO!!!')
                        h2.insert(0, h3[0])
                        del(h3[0])  
            else:
                pass
        elif jogada == 3:
            if jogada2 == 1:
                h1.insert(0, h3[0])
                del(h3[0])
                if len(h1) >= 2:
                    if max(h2) == h2[0]:
                        print('MOVIMENTO INVALIDO!!!')
                        h3.insert(0, h1[0])
                        del(h1[0])  
            elif jogada2 == 2:
                h2.insert(0, h3[0])
                del(h3[0])
                if len(h2) >= 2:
                    if max(h2) == h2[0]:
                        print('MOVIMENTO INVALIDO!!!')
                        h2.insert(0, h3[0])
                        del(h3[0])  
            else:
                pass
