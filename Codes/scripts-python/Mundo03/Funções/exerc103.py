"""
    FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA ficha(), QUE RECEBA DOIS PARÂMETROS
    OPCIONAIS: O NOME DE UM JOGADOR E QUANTOS GOLS ELE MARCOU.

    O PROGRAMA DEVERÁ SER CAPAZ DE MOSTRAR A FICHA DO JOGADOR, MESMO QUE ALGUM DADO
    NÃO TENHA SIDO INFORMADO CORRETAMENTE.
"""


def mostraLinha(text):
    print('-' * len(text))
    print()


def mostraLinha2():
    print('~' * 80)


def ficha(jog='<desconhecido>', qtdGols=0):

    """
    :param jog: NOME DO JOGADOR QUE VAI ESTAR PRESENTE NA FICHA
    :param qtdGols: QUANTIDADE DE GOLS QUE O JOGADOR MARCOU NO CAMPEONATO
    :return: SEM RETURN
    """

    msg = f'    O jogador {jog} fez {qtdGols} gol(s) no campeonato!    \n'

    print()
    mostraLinha(msg)
    print('{:^50}'.format(msg))
    mostraLinha(msg)


# programa principal

nome = str(input('INSIRA O NOME DO JOGADOR: '))
gols = str(input(f'INSIRA A QUANTIDADE DE GOLS MARCADOS PELO JOGADOR {nome.upper()}: '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome.strip() == '':
    ficha(qtdGols=gols)
else:
    ficha(nome, gols)

