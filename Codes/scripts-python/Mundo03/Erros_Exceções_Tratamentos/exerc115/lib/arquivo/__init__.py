colors = ('\033[0m',  # 0 - SEM CORES
          '\033[0;31m',  # 1 - VERMELHO
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
    print('~' * 50)
    print(f'{msg:^50}')
    print('~' * 50)
    print(colors[0], end='')
    print()


def archiveExist(archiveName):
    try:
        """ r => leitura(read) && t => texto(text) | abrir arquivo em modo texto """
        archive = open(archiveName, 'rt')
        archive.close()
    except FileNotFoundError:
        return False
    else:
        return True


def createArchive(archiveName):
    try:
        """
            w -> escrita(write)
            t -> texto(text)
            + -> verificação de existência do arquivo, caso não exista, será criado.
        """
        archive = open(archiveName, 'wt+')
        archive.close()
    except:
        msgErro = 'HOUVE UM ERRO NA CRIAÇÃO DO ARQUIVO!'
        imprimirMensagem(f'{msgErro}', 1)
    else:
        msg = f'ARQUIVO {archiveName.upper()} CRIADO COM SUCESSO!'
        imprimirMensagem(msg, 2)

