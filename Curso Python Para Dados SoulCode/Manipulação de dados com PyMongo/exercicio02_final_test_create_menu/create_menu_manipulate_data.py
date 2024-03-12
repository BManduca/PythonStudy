from pymongo import collection

colors = (
    '\033[0m', # 0 - SEM COR
    '\033[0;31m', # 1 - VERMELHO
    '\033[0;32m', # 2 - VERDE
    '\033[0;33m', # 3 - AMARELO
    '\033[0;34m', # 4 - AZUL
    '\033[0;35m', # 5 - ROXO
    '\033[0;36m', # 6 - BRANCO
)


def imprimirMsgEstilizada(msg, cor=0):
    print(colors[cor], end='')
    print(f'{msg:^60}')
    print(colors[0], end='')

def imprimirMsg(msg):
    print(f'{msg}')

def imprimirLinha20(cor=0):
    print(colors[cor], end='')
    print('-=-'*20)
    print(colors[0], end='')

def imprimirLinha(cor=0):
    print(colors[cor], end='')
    print('-=-'*5)
    print(colors[0], end='')

def get_database():
    from pymongo import MongoClient
    import pymongo

    CONNECTION_STRING = "mongodb+srv://manduca:xmd8Xvu1XCcoIz6Q@mydatabase.8vdqilo.mongodb.net/"

    client = MongoClient(CONNECTION_STRING)

    imprimirLinha20(2)
    imprimirMsgEstilizada('CONECTADO AO BANCO COM SUCESSO!',2)
    imprimirLinha20(2)

    return client['exerciseDatabase']

def exibir_menu():
    imprimirLinha20(4)
    imprimirMsgEstilizada('BEM-VINDO AO PROGRAMA DE MANIPULAÇÃO DE DADOS!', 4)
    imprimirMsgEstilizada('SELECIONE UMA OPÇÃO: ', 4)
    print(' ')
    imprimirMsgEstilizada('1 => CADASTRO DE DOCUMENTO')
    imprimirMsgEstilizada('0 => FINALIZAR PROGRAMA')
    imprimirLinha20(4)
    # imprimirMsgEstilizada('2 => ')
    # imprimirMsgEstilizada('3 => ')

def cadastrarDocumento():
    dbname = get_database()
    collection_name = dbname['exerciseListDatabase']
    qtd = int(input('ENTRE COM A QUANTIDADE DE CAMPOS QUE O DOCUMENTO TERÁ: '))
    dct = dict(input('DIGITE A CHAVE E O VALOR SEPARADO POR ESPAÇOS: ').split() for _ in range(qtd))

    print()
    print(dct)
    collection_name.insert_one(dct)

    print()
    imprimirLinha20(2)
    imprimirMsgEstilizada('DADOS CADASTRADOS COM SUCESSO!', 2)
    imprimirLinha20(2)
    print()



def main():
    while True:
        exibir_menu()
        print( )
        theChoice = input('INSIRA A OPÇÃO DESEJADA: ')

        if theChoice == '1':
            cadastrarDocumento()
        elif theChoice == '0':
            print('\n')
            imprimirLinha20(1)
            imprimirMsgEstilizada('FINALIZANDO PROGRAMA!', 1)
            imprimirLinha20(1)
            print('\n')
            break
        else:
            print('OPÇÃO INVÁLIDA! POR FAVOR, INSIRA NOVAMENTE A OPÇÃO ESCOLHIDA!')


if __name__ == "__main__":
    main()