"""
  Crie um programa que leia o nome completo de uma pessoa e mostre:
    - O nome com todas as letras maiúsculas
    - O nome com todas as letras minúsculas
    - Quantas letras ao todo(sem considerar espaços)
    - Quantas letras tem o primeiro nome
"""

print('\n===== EXERCÍCIO 22 ======\n')

nome = str(input('Insira o seu nome completo: '))
print('\n')


nomeMaiusc = nome.upper()
nomeMinusc = nome.lower()
nomeSemEspaço = nome.replace(' ', '')
qtdLetrasNome = len(nomeSemEspaço)
dividirNome = nome.split()
tamanhoPrimeiroNome = len(dividirNome[0])

print('-'*100)
print('\nSeu nome completo em caixa alta: {}'.format(nomeMaiusc))
print('Seu nome completo em caixa baixa: {}'.format(nomeMinusc))
print('Total de letras do seu nome completo: {}'.format(qtdLetrasNome))
print('Quantidade de letras no seu primeiro nome: {}\n'.format(tamanhoPrimeiroNome))
print('-'*100)