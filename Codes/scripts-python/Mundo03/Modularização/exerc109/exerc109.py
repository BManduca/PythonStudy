"""
    MODIFIQUE AS FUNÇÕES QUE FORAM CRIADAS NO DESAFIO 107 PARA QUE ELAS
    ACEITEM UM PARÂMETRO A MAIS, INFORMANDO SE O VALOR RETORNADO POR ELES
    VAI SER OU NÃO FORMATADO PELA FUNÇÃO MOEDA(), DESENVOLVIDA NO DESAFIO 108
"""

import moeda

moeda.imprimirLinha("   << MANDUCA'S CALCULADORA >>   ")

price = float(input('\n    INSIRA O PREÇO: R$ '))
print()
moeda.imprimirLinha(f' A) ==> A METADE DE {moeda.moeda(price)} É {moeda.metade(price, True)}  ')
moeda.imprimirLinha(f' B) ==> O DOBRO DE {moeda.moeda(price)} É {moeda.dobro(price, True)}   ')
moeda.imprimirLinha(f' C) ==> AUMENTANDO 10%, TEMOS {moeda.aumentar(price, 10, True)}   ')
moeda.imprimirLinha(f' D) ==> DIMINUINDO 13%, TEMOS {moeda.diminuir(price, 13, True)}   ')
print()
moeda.imprimirLinha('   ==> AGRADECEMOS A PREFERÊNCIA!   ')
moeda.imprimirLinha('   ==> VOLTE SEMPRE!  ')
