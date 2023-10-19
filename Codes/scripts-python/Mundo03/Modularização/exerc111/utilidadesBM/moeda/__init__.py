

def imprimirTitulo(mens):
    tam = len(mens)

    print('~'*tam)
    print(f'{mens}')
    print('~'*tam)


def imprimiLinha():
    print()
    print('~'*55)
    print()


def imprimirRelacao(mens):
    tam = len(mens)
    print(f'{mens:^{tam}}')


def aumentar(valor, percent, sit=False):
    valor += (valor * percent) / 100

    if sit:
        return f'R$ {valor:.2f}'
    else:
        return valor


def diminuir(valor, percent, sit=False):
    valor -= (valor*percent)/100

    if sit:
        return f'R$ {valor:.2f}'
    else:
        return valor


def dobro(valor, sit=False):
    if sit:
        return f'R$ {(valor * 2):.2f}'
    else:
        return valor * 2


def metade(valor, sit=False):
    if sit:
        return f'R$ {(valor / 2):.2f}'
    else:
        return valor / 2


def moeda(valor):
    return f'R$ {valor:.2f}'


def resumo(valor, percentAum=0, percentDim=0):
    imprimirTitulo("   << RESUMO DAS OPERAÇÕES >>   ")
    imprimiLinha()
    imprimirRelacao(f'   PREÇO ANALISADO ==> {moeda(valor):>25}')
    imprimirRelacao(f'   DOBRO DO PREÇO  ==> {dobro(valor, True):>25}')
    imprimirRelacao(f'   METADE DO PREÇO ==> {metade(valor, True):>25}')
    imprimirRelacao(f'   {percentAum}% DE AUMENTO  ==> {aumentar(valor, percentAum, True):>25}')
    imprimirRelacao(f'   {percentDim}% DE REDUÇÃO  ==> {diminuir(valor, percentDim, True):>25}')
    imprimiLinha()

