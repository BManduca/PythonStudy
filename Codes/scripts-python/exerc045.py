"""
    Crie um programa que faça o computador jogar jokenpô com você
"""

from os import system
from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')

print('\n')
print('-'*51)
print('\n---------------------JO KEN PÔ---------------------\n')
print('-'*51)
print('\n')

print('\nGOSTARIA DE INICIAR O JOGO?\n')
print('-'*17)
print('| S - Para sim |\n| N - Para não |')
print('-'*17)

question = str(input('\nResposta: '))
print('\n')

while question != 'N' and question != 'n':

    opcaoComputer = randint(0, 2)

    print('''Escolha uma das opções para jogar:
        [ 0 ] PEDRA
        [ 1 ] PAPEL
        [ 2 ] TESOURA
    ''')

    opcaoJogador = int(input('Insira a sua jogada: '))
    print('\n')
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    sleep(1)

    print('\n')
    print('-='*15)
    print('\nO COMPUTADOR JOGOU {}\n'.format(itens[opcaoComputer]))
    print('O JOGADOR JOGOU {}\n'.format(itens[opcaoJogador]))
    print('-='*15)
    print('\n')

    if opcaoComputer == 0:
        if opcaoJogador == 0:
            print('==> EMPATE\n')
        elif opcaoJogador == 1:
            print('==> O JOGADOR VENCEU!\n')
        elif opcaoJogador == 2:
            print('==> O COMPUTADOR VENCEU!\n')
        else:
            print('==> JOGADA INVÁLIDA!\n')
    elif opcaoComputer == 1:
        if opcaoJogador == 0:
            print('==> O COMPUTADOR VENCEU!\n')
        elif opcaoJogador == 1:
            print('==> EMPATE\n')
        elif opcaoJogador == 2:
            print('==> O JOGADOR VENCEU!\n')
        else:
            print('==> JOGADA INVÁLIDA!\n')
    elif opcaoComputer == 2:
        if opcaoJogador == 0:
            print('==> O JOGADOR VENCEU!\n')
        elif opcaoJogador == 1:
            print('==> O COMPUTADOR VENCEU!\n')
        elif opcaoJogador == 2:
            print('==> EMPATE\n')
        else:
            print('==> JOGADA INVÁLIDA!\n')
    else:
        print('==> JOGADA INVÁLIDA!\n')

        
    sleep(5)
    system('clear')
    print('\n\nGOSTARIA DE JOGAR NOVAMENTE?\n')
    print('-'*17)
    print('| S - Para sim |\n| N - Para não |')
    print('-'*17)
    question = str(input('\nResposta: '))
    system('clear')

print('\nOBRIGADO POR JOGAR COM A GENTE!\n')

print('A TELA SERÁ LIMPA EM 5 SEGUNDOS!\n')
sleep(5)

system('clear')