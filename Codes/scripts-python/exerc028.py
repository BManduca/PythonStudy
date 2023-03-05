"""
  Escreva um programa que faça o computador "pensar" em um número 
  inteiro entre 0 e 5 e peça para o usuário tentar descobrir 
  qual foi o número escolhido pelo computador.

  O programa deverá escrever na tela se o usuário venceu ou 
  perdeu
"""

import random

print('\n===== EXERCÍCIO 27 ======\n')

print('{}-=-'.format('\033[1;34m') * 20)
print('   VERIFICADOR DE VALOR GERADO PELO COMPUTADOR')
print('-=-' * 20)

print('\n')

numComputer = random.randint(0, 5)

numUser = int(input('Qual valor escolhido pelo computador? '))

if numComputer == numUser:
    print('Parabéns jogador! Você acertou e ganhou o jogo!')
else:
    print('Infelizmente você perdeu o jogo! Insira uma ficha e tente novamente!\n')
