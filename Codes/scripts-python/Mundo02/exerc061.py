"""
    REFAÇA O DESAFIO 51, LENDO O PRIMEIRO TERMO E A RAZÃO DE UMA PA, 
    MOSTRANDO OS 10 PRIMEIROS TERMOS DA PROGRESSÃO ARITMÉTICA USANDO
    A ESTRUTURA WHILE
"""

print('\n')
print('-'*90)
print('\n------------------------ PROGRAMA PARA REALIZAR CÁLCULO DE UMA PA ------------------------\n')
print('-'*90)
print('\n')

firstTerm = int(input('INSIRA O PRIMEIRO TERMO DA PA: '))
print('')
razao = int(input('INSIRA A RAZÃO DA PA: '))
print('')

termo = firstTerm
contPA = 1

## PA = a1, (a1 + r), (a1 + 2r), (a1 + 3r), (a1 + 4r), (a1 + 5r)....

while contPA <= 10:
    print('{} '.format(termo), end='➙ ')
    termo += razao
    contPA += 1
print('ACABOU!!')
