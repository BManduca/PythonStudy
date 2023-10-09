"""
    EXERCÍCIO 101 - CRIE UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA VOTO()
    QUE VAI RECEBER COMO PARÂMETRO O ANO DE NASCIMENTO DE UMA PESSOA, RETORNANDO
    UM VALOR LITERAL INDICANDO SE A PESSOA TEM SEU VOTO NEGADO, OPCIONAL OU
    OBRIGATÓRIO NAS ELEIÇÕES.
"""


def mostraLinha():
    print()
    print('-='*30)


def voto(ano):
    idade = 2023 - ano

    if idade < 16:
        print(f'\n   COM {idade}: VOTO NEGADO! ')
    elif 16 < idade < 18 & idade > 70:
        print(f'\n   COM {idade}: VOTO OPCIONAL! ')
    elif idade >= 18:
        print(f'\n   COM {idade}: VOTO OBRIGATÓRIO! ')


mostraLinha()
anoNasc = int(input('\n   INSIRA O SEU ANO DE NASCIMENTO: '))
voto(anoNasc)
mostraLinha()
print()
