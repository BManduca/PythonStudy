"""
  ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO.

  SE ELE ULTRAPASSAR 80 KM/H, MOSTRE UMA MENSAGEM DIZENDO
  QUE ELE FOI MULTADO.

  A MULTA VAI CUSTAR R$7,00 POR CADA KM ACIMA DO LIMITE.
"""

print('\n===== EXERCÍCIO 29 ======\n')

print('{}-=-'.format('\033[1;34m') * 20)
print('   PROGRAMA PARA MONITORAR EXCESSO DE VELOCIDADE!')
print('-=-' * 20)

print('\n')

nomeCondutor = str(input('Nome do condutor: '))

velocidadeVeiculo = int(input('\nVelocidade do veículo(km/h): '))

valorMulta = (velocidadeVeiculo - 80) * 7

if velocidadeVeiculo > 80: 
    print('\nVocê acabou de ser multado em R${},00\n'.format(valorMulta))
else:
    print('\nLimite de velocidade respeitado!\nTenha uma boa viagem!')