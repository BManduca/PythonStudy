"""
    CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR CINCO VALORES NUMÉRICOS
    E CADASTRE-OS EM UMA LISTA, JÁ NA POSIÇÃO CORRETA DE INSERÇÃO (SEM USAR O
    SORT()).

    NO FINAL, MOSTRE A LISTA ORDENADA NA TELA
"""

print('\n')
print('='*60)
print('{:=^60}'.format(' EXERCÍCIO 80 '))
print('='*60)
print('\n')

valores = []

for v in range(0, 5):
    aux = int(input('INSIRA UM VALOR: '))

    if v == 0 or aux > valores[len(valores)-1]:
        valores.append(aux)
    else:
        p = 0
        while p < len(valores):
            if aux <= valores[p]:
                valores.insert(p, aux)
                break
            p += 1

print()
print('='*60)
print(f'LISTAGEM DOS VALORES DIGITADOS: {valores}')
print('='*60)

