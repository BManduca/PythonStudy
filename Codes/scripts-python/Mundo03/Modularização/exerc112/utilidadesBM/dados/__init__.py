from time import sleep
from os import system


def leiaDinheiro(mens):
    valid = False
    while not valid:
        entrada = str(input(mens)).replace(',', '.').strip()
        # verificando se é alfa-númerico ou testando se esta cheio de espaços em branco ou se esta vazio
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31m  >> ERRO: \"{entrada}\" É UM PREÇO INVÁLIDO!\033[m')
            sleep(0.7)
            # system('clear')
        else:
            valid = True
            return float(entrada)
