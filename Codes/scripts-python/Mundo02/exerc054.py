"""
CRIE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE SETE PESSOAS. NO FINAL MOSTRE QUANTAS PESSOAS
AINDA NÃO ATINGIRAM A MAIORIDADE E QUANTAS JÁ ATINGIRAM 
"""

print('\n')
print('-'*84)
print('\n------------------------ PROGRAMA PARA VERIFICAR MAIORIDADE ------------------------\n')
print('-'*84)
print('\n')

vetMaiorIdade = []
vetMenorIdade = []

anoAtual = int(input('Insira o ano atual: '))
print('')

for i in range(0,8):
    print('ANO NASCIMENTO DA PESSOA {}: '.format(i), end="")
    anoNasc = int(input(''))

    idade = anoAtual - anoNasc

    if idade >= 18:
        print('Pessoa {} nasceu no ano de {} e é maior de idade({} ano(s))\n'.format(i+1, anoNasc, idade))
        vetMaiorIdade.append(anoNasc)
    else:
        print('Pessoa {} nasceu no ano de {} e não é maior de idade({} ano(s))\n'.format(i+1, anoNasc, idade))
        vetMenorIdade.append(anoNasc)

print('-'*50)
print('Maiores de idade: {}'.format(vetMaiorIdade))
print('\nMenores de idade: {}'.format(vetMenorIdade))
print('-'*50)