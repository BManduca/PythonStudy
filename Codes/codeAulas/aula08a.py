import math

num = int(input('Digite um número: '))
expoente = int(input('Insira o valor do expoente: '))

raizQuadrada = math.sqrt(num)
pot = math.pow(num, expoente)

print('\n')
print('-'*100)
print('\nA raiz quadrada de {} é {:.2f}'.format(num, raizQuadrada))
print('\nAo arredondar o resultado da raiz de {} elevado a {}º potência para cima é  {:.2f}'.format(num, expoente, math.ceil(raizQuadrada)))
print('\nAo arredondar o resultado da raiz de {} elevado a {}º potência para baixo é {:.2f}'.format(num, expoente, math.floor(raizQuadrada)))
print('\nO número {} elevado a {}º potência é {:.2f}\n'.format(num, expoente, pot))
print('-'*100)
