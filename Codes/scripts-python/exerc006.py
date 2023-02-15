"""
    Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
"""
import math

print('===== EXERCÍCIO 06 ======\n')

valorEnt = int(input('Digite um número: '))
vDobro = valorEnt * 2
vTriplo = valorEnt * 3
vRaizQuadrada = math.pow(valorEnt, 1/2)

print('Valor inicial inserido: {}\nO dobro de é {}\nO triplo é {}\nA raiz quadrada é {}'.format(valorEnt, int(vDobro), int(vTriplo), int(vRaizQuadrada)))

