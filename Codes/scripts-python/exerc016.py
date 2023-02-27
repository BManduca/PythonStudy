"""
    Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.

    Ex.: 
        Digite um número: 6.124
        A parte inteira do número 6.124 é 6.
"""
import math

print('===== EXERCÍCIO 16 ======\n')
print('-'*100)
valInicial = float(input('\nDigite um número: '))
print('A parte inteira do número {} é {}\n'.format(valInicial, math.trunc(valInicial)))
print('-'*100)