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
from time import sleep
from os import system
from lib.interface import *


# PROGRAMA PRINCIPAL
cabecalho('SISTEMA MANDUCA v1.0')

while True:
    resp = menu(['CADASTRAR NOVO COLABORADOR', 'LISTAR COLABORADORES', 'SAIR DO SISTEMA'], 2)

    if resp == 1:
        print('Opção 1')
    elif resp == 2:
        print('Opção 2')
        sleep(1.5)
        system('clear')
    elif resp == 3:
        txtExit = 'SAINDO DO SISTEMA.... ATÉ LOGO!'
        imprimirMensagem(f'{txtExit:^50}', 5)
        break
    else:
        txterror = 'ERRO! INSIRA UMA OPÇÃO VALÍDA!'
        imprimirMensagem(f'{txterror:^50}', 1)
        sleep(1.5)
        system('clear')
