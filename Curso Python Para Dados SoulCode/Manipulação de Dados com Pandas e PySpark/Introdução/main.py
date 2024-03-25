import numpy as np
import pandas as pd

colors = (
    '\033[0m', # 0 - SEM COR
    '\033[0;31m', # 1 - VERMELHO
    '\033[0;32m', # 2 - VERDE
    '\033[0;33m', # 3 - AMARELO
    '\033[0;34m', # 4 - AZUL
    '\033[0;35m', # 5 - ROXO
    '\033[0;36m', # 6 - BRANCO
)

def messageCentralized(msg, wid):
    tam = len(msg)
    space = (wid - tam) // 2
    text = ' ' * space + msg + ' ' * space
    # Se o texto não puder ser centralizado perfeitamente, ajuste uma posição para a direita
    if len(text) < wid:
        text += ' '
        
    return text

def printTextCentralized(msg, wid, cor=0):
    message = messageCentralized(msg, wid)
    print(colors[cor], end='')
    print(message)
    print(colors[0], end='')

def imprimirLinha20(cor=0):
    print(colors[cor], end='')
    print('-=-'*20)
    print(colors[0], end='')

notas = pd.Series([10, 5, 7.5, 9, 10])

notas2 = pd.Series([10, 5, 7.5, 9, 10], index=['José', 'Carlos', 'André', 'João', 'Débora'])
# print(notas2)

# método describe exibe informações estatísticas
imprimirLinha20(2)
# print(notas.describe())
printTextCentralized(f'Média: {notas.mean()}', 60, 2)
imprimirLinha20(2)
print()
imprimirLinha20(2)
printTextCentralized('IMPRIMINDO O DOBRO DAS NOTAS: ', 60, 2)
print(f'{notas**2}')
imprimirLinha20(2)

# imprimirLinha20(2)
# print(notas)
# imprimirLinha20(2)
# print(notas.values)
# print(notas.index)