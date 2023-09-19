"""
    CRIE UM PROGRAMA QUE LEIA O NOME, SEXO E A IDADE DE VÁRIAS PESSOAS,
    GUARDANDO OS DADOS DE CADA PESSOA EM UM DICIONÁRIO E TODOS OS
    DICIONÁRIOS EM UMA LISTA. NO FINAL, MOSTRE:
    A) QUANTAS PESSOAS FORAM CADASTRADAS
    B) A MÉDIA DE IDADE DO GRUPO
    C) UMA LISTA COM TODAS AS MULHERES
    D) UMA LISTA COM TODAS AS PESSOAS COM IDADE ACIMA DA MÉDIA
"""
import os
import time
from os import system

print()
print('-'*50)
print('{:^50}'.format(' RELAÇÃO DE CADASTRO '))
print('-'*50)
print()

pessoas = {}
listaGeral = []
totalIdade = 0
resposta = 'S'

while True:
    pessoas.clear()
    print('-='*20)
    pessoas['nome'] = str(input('Nome: '))

    while True:
        pessoas['sexo'] = str(input('SEXO[M/F]: ')).upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('RESPOSTA INCORRETA! FAVOR INSERIR M OU F. ')

    pessoas['idade'] = int(input('IDADE: '))
    listaGeral.append(pessoas.copy())
    print('-=' * 20)
    while True:
        resposta = str(input('\nGOSTARIA DE INSERIR OUTRO REGISTRO? [S/N]:  ')).upper()[0]
        print()

        if resposta in 'SN':
            break
        print('RESPOSTA INCORRETA! FAVOR INSERIR S OU N. ')
    if resposta == 'N':
        break


print(listaGeral)


#     resposta = str(input('GOSTARIA DE INSERIR OUTRO REGISTRO? [S/N]:  ')).upper()
#     time.sleep(0.5)
#
#     while resposta not in 'SN':
#         resposta = str(input('A RESPOSTA INSERIDA ESTÁ INCORRETA!\nPOR FAVOR, TENTE NOVAMENTE: '))
#         time.sleep(0.5)
#     print()
#     system('clear')
#
#
# print()
# print('-'*15)
# print('{:^30}'.format(' LISTAGEM FINAL '))
# print('-'*15)
# print()
# print('-='*40)
# print(f'A) TOTAL DE PESSOAS CADASTRADAS: {} pessoas')




