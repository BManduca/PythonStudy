"""
DESENVOLVA UM PROGRAMA QUE LEIA SEIS NÚMEROS INTEIROS E MOSTRE A SOMA 
APENAS DAQUELES QUE FOREM PARES. SE O VALOR DIGITADO FOR ÍMPAR, DESCONSIDERE-O
"""

print('\n')
print('-'*123)
print('\n------------------------ PROGRAMA PARA LEVAR EM CONSIDERAÇÃO SOMENTE NÚMEROS PARES E SOMÁ-LOS  ------------------------\n')
print('-'*123)
print('\n')


soma = 0
contador = 0
lista = []

for c in range(0,6):
    number = int(input('Insira um número: '))
    print('')
    #calcula os números PARES usando o resto da divisão
    if number % 2 == 0:
        soma += number
        #somar quantos números foram somados ao total
        contador += 1
        lista.append(number)

print('Os valores pares são: {}'.format(lista))

print('\nA soma de todos os {} valores é {}'. format(contador, soma))