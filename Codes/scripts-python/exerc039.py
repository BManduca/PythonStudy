"""
faça um programa que leia o ano de nascimento de um jovem
e informe, de acordo com a sua idade:

- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo de alistamento

    => seu programa também deve mostrar o tempo que falta ou que
    passou do prazo.

"""

from os import system
import time

print('\n')
print('-'*60)
print('\nPROGRAMA PARA VERIFICAR O ALISTAMENTO MILITAR!\n')
print('-'*60)
print('\n')

print('\nGostaria de iniciar o processo de verificação?\n')
print('-'*17)
print('| S - Para sim |\n| N - Para não |')
print('-'*17)


question = str(input('Resposta: '))
print('\n')

while question != 'N':

    print('-'*50)
    name = str(input('Insira o seu nome: '))
    age = int(input('\nInsira a sua idade: '))

    if age > 18:
        tempoAlistamento = age - 18
        print('Já passou do tempo de alistamento! ')
