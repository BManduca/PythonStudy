"""
    Crie um programa que faça o computador jogar jokenpô com você
"""

from os import system
from random import randint
import time

itens = ('Pedra', 'Papel', 'Tesoura')

computer = randint(0, 2)

print('\n')
print('-'*50)
print('\n-------------JO KEN PÔ-------------\n')
print('-'*50)
print('\n')

print('\nGOSTARIA DE INICIAR O JOGO?\n')
print('-'*17)
print('| S - Para sim |\n| N - Para não |')
print('-'*17)

question = str(input('\nResposta: '))
print('\n')

while question != 'N':

    print('''Escolha uma das opções para jogar:
        [ 1 ] PEDRA
        [ 2 ] PAPEL
        [ 3 ] TESOURA
    ''')

    opcao = int(input('Insira a sua jogada: '))

    print('-='*15)
    print('\nO COMPUTADOR JOGOU {}\n'.format(itens[computer]))
    print('O JOGADOR JOGOU {}\n'.format(itens[opcao]))
    print('-='*15)
    print('\n')