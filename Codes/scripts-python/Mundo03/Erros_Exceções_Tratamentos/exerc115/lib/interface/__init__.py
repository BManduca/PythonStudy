from time import sleep


colors = ('\033[0m',  # 0 - SEM CORES
          '\033[0;31m',  # 1 - VERMELHO
          '\033[0;32m',  # 2 - VERDE
          '\033[0;33m',  # 3 - AMARELO
          '\033[0;34m',  # 4 - AZUL
          '\033[0;35m',  # 5 - ROXO
          '\033[0;30m'  # 6 - BRANCO
          )


def imprimirLinha(tam=50, cor=0):
    print(colors[cor], end='')
    print('-' * tam)
    print(colors[0], end='')


def imprimirMensagem(msg, cor=0):
    tam = len(msg)
    print()
    print(colors[cor], end='')
    print('~' * 50)
    print(f'{msg}')
    print('~' * 50)
    print(colors[0], end='')
    print()


def cabecalho(txt):
    imprimirMensagem(f'{txt:^50}', 4)


def leiaInt(msg):
    """

        ==> IMPRIMIR MENSAGEM APÓS VALIDAR O VALOR INTEIRO INSERIDO PELO USUÁRIO.
        :param msg: A MENSAGEM(NO CASO O VALOR) INSERIDO ATRAVÉS DO TECLADO PELO USUÁRIO.
        :return: MENSAGEM IMPRESSA DIZENDO QUAL O VALOR QUE O USUÁRIO INSERIU ATRAVÉS DO TECLADO.
    """
    while True:
        try:
            valInteiro = int(input(msg))
        except (ValueError, TypeError):
            msgerro1 = 'ERRO! POR FAVOR, INSIRA UM INTEIRO VÁLIDO!'
            imprimirMensagem(f'{msgerro1:^50}', 1)
            sleep(1.5)
            # joga para o while novamente
            continue
        except KeyboardInterrupt:
            msgerro2 = 'ENTRADA DE DADOS INTERROMPIDA PELO USUÁRIO!'
            imprimirMensagem(f'{msgerro2:^50}', 1)
            sleep(1.5)
            break
        else:
            return valInteiro


def menu(lista, cor=0):
    txt = 'MENU PRINCIPAL'
    imprimirMensagem(f'{txt:^50}', 2)
    cont = 1
    for i in lista:
        print(colors[cor], end='')
        print(f'{cont} - {i}')
        print(colors[0], end='')
        cont += 1
    imprimirLinha(50, 2)
    print()
    opcuser = leiaInt('INSIRA UMA OPÇÃO: ')
    return opcuser
