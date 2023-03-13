"""
  DESENVOLVA PROGRAMA QUE PERGUNTE A DISTÂNCIA DE UMA VIAGEM EM
  KM.
  CALCULE O PREÇO DA PASSAGEM, COBRANDO R$0,50 POR KM PARA 
  VIAGENS ATÉ 200KM E R$0,45 PARA VIAGENS MAIS LONGAS.
"""

print('\n===== EXERCÍCIO 31 ======\n')

print('{}-=-'.format('\033[1;34m') * 20)
print('\n   PROGRAMA PARA CALCULAR O VALOR DE PASSAGENS!\n')
print('-=-' * 20)
print('\n')
print('---' * 20)
print('\nVALORES:\n')
print('\n => PARA VIAGENS ATÉ 200 KM, SÃO R$0,50 POR KM!')
print(' => PARA VIAGENS MAIS LONGAS, SÃO R$0,45 POR KM!\n')
print('---' * 20)

print('\n')

distViagem = float(input('Insira a distância da viagem(km): '))

if (distViagem <= 200):
  print('\nPara um total de {:.2f} km, o valor da sua passagem será R${:.2f}\n'.format(distViagem, distViagem * 0.50))
else:
  print('\nPara um total de {:.2f} km, o valor da sua passagem será R${:.2f}\n'.format(distViagem, distViagem * 0.45))