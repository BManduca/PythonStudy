

def imprimirLinha(mens):
    tam = len(mens) + 4

    print('~'*tam)
    print(f'{mens}')
    print('~'*tam)


def aumentar(valor, percent):
    valor += (valor * percent) / 100
    return valor


def diminuir(valor, percent):
    valor -= (valor*percent)/100
    return valor


def dobro(valor):
    return valor * 2


def metade(valor):
    return valor/2


def moeda(valor):
    return f'R${valor:.2f}'
