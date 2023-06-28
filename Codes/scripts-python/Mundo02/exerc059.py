"""
    CRIE UM PROGRAMA QUE LEIA DOIS VALORES E MOSTRE UM MENU NA TELA:

    [1] SOMAR
    [2] DIMINUIR
    [3] MULTIPLICAR
    [4] DIVIDIR
    [5] MAIOR
    [6] NOVOS NÚMEROS
    [7] SAIR DO PROGRAMA
"""

print('\n')
print('{}-'.format('\033[1;32m')*48)
print('\n-------------- CALCULADORA PYTHON --------------\n')
print('-'*48)
print('\n')

valor1 = int(input('INSIRA O PRIMEIRO VALOR: '))
valor2 = int(input('INSIRA O SEGUNDO VALOR: '))

print('\n--------- MENU ---------')
print('| [1] SOMAR            |')
print('| [2] DIMINUIR         |')
print('| [3] MULTIPLICAR      |')
print('| [4] DIVIDIR          |')
print('| [5] MAIOR            |')
print('| [6] NOVOS NÚMEROS    |')
print('| [7] SAIR DO PROGRAMA |')
print('------------------------')

optionMenu = int(input('\nEscolha uma operação para ser realizada: '))