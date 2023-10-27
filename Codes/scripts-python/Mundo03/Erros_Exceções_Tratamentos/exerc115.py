"""
    CRIE UM PEQUENO SISTEMA MODULARIZADO QUE PERMITE CADASTRAR PESSOAS PELO SEU NOME E IDADE
    EM UM ARQUIVO DE TEXTO SIMPLES.

    O SISTEMA SÓ VAI TER 2 OPÇÕES: CADASTRAR UMA NOVA PESSOA E LISTAR TODAS AS PESSOAS CADASTRADAS.


    OPÇÕES PARA MANIPULAÇÃO DE ARQUIVOS PYTHON

    'r' ==> LEITURA
    'w' ==> ESCRITA. SUBSTITUI O CONTEÚDO DO ARQUIVO EXISTENTE
    'x' ==> ESCRITA. RETORNA ERRO CASO O ARQUIVO JÁ EXISTA
    'a' ==> ESCRITA. INSERE OS NOVOS DADOS NO FINAL DO ARQUIVO
    'b' ==> MONO BINÁRIO
    't' ==> MODO DE TEXTO (PADRÃO)
    '+' ==> ATUALIZAR. TANTO LEITURA QUANTO ESCRITA

"""

colors = ('\033[0m',  # 0 - SEM CORES
          '\003[0;31m',  # 1 - VERMELHO
          '\033[0;32m',  # 2 - VERDE
          '\033[0;33m',  # 3 - AMARELO
          '\033[0;34m',  # 4 - AZUL
          '\033[0;35m',  # 5 - ROXO
          '\033[0;30m'  # 6 - BRANCO
          )


def imprimirMensagem(msg, cor=0):
    tam = len(msg)
    print()
    print(colors[cor], end='')
    print('-'*tam)
    print(f'{msg}')
    print('-' * tam)
    print(colors[0], end='')
    print()


def cadastrar():
    print()


def listar():
    print()


def menu():
    print()


# PROGRAMA PRINCIPAL

