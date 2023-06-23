"""
CRIE UM PROGRAMA QUE LEIA UMA FRASE QUALQUER E DIGA SE A PALAVRA É PALÍNDROME, DESCONSIDERANDO OS ESPAÇOS!
"""

print('\n')
print('-'*109)
print('\n------------------------ PROGRAMA PARA VERIFICAR SE O TEXTO INSERIDO É PALÍNDROME OU NÃO ------------------------\n')
print('-'*109)
print('\n')


frase = str(input('Insira uma frase: ')).upper().replace(' ', '')

if frase == frase[:: - 1]:
    print('O TEXTO INSERIDO É PALÍNDROME!','\n')
    print('O TEXTO INVERTIDO: {}'.format(frase), '\n')
else:
    print('A TEXTO NÃO É PALÍNDROME!','\n')

print('texto inserido: {}'.format(frase), '\n')

