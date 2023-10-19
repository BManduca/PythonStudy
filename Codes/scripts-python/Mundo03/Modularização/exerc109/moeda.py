

def imprimirLinha(mens):
    tam = len(mens) + 4

    print('~'*tam)
    print(f'{mens}')
    print('~'*tam)


def aumentar(valor, percent, sit=False):
    valor += (valor * percent) / 100

    if sit:
        return f'R${valor:.2f}'
    else:
        return valor


def diminuir(valor, percent, sit=False):
    valor -= (valor*percent)/100

    if sit:
        return f'R${valor:.2f}'
    else:
        return valor


def dobro(valor, sit=False):
    if sit:
        return f'R${(valor * 2):.2f}'
    else:
        return valor * 2


def metade(valor, sit=False):
    if sit:
        return f'R${(valor / 2):.2f}'
    else:
        return valor / 2


def moeda(valor):
    return f'R${valor:.2f}'
