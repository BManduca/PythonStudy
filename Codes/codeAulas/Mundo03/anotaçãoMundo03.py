'''
- AULA 16

    - Estruturas/varíaveis compostas
    - Rotinas
    - tratamentos de erros

    => VARÍAVEIS COMPOSTAS(TUPLAS)
        - EXISTEM 3 TIPOS DE VARÍAVEIS COMPOSTAS EM PYTHON:
            - TUPLAS
            - LISTAS
            - DICIONÁRIOS

        => BASE DE FUNDAMENTOS(TEORIA)
            - VARÍAVEIS SIMPLES: PODE RECEBER SOMENTE UM VALOR PRA "DENTRO" DELA
            - VARÍAVEIS COMPOSTAS: sÃO CONHECIDAS COMO TUPLAS E 
            PODEM RECEBER MAIS DE UM VALOR "DENTRO" DELA

                - OS ELEMENTOS DE UM TUPLA SÃO ACESSADOS ATRAVÉS DE ÍNDICES E 
                OS ÍNDICES SÃO NÚMERICOS, COMO DEMOSTRADO LOGO ABAIXO:

                VARÍAVEL COMPOSTA lanche
                |___|___|___|___|
                  0   1   2   3
                
                -  para acessar os lanches fazemos o seguinte: 
                    PARA ACESSAR O LANCHE PRESENTE NA PRIMEIRA POSIÇÃO: lanche[0]

                - TEM UM ASSUNTO QUE FOI ALINHADO NO MUNDO01, QUE TAMBÉM É CONHECIDO
                COMO TUPLA => AS PRÓPRIAS STRINGS
                    - O NOME EM SI NA VERDADE, ELE É CONSIDERADO UMA LISTA
                    - POR EXEMPLO: 
                        O NOME BRUNNO É CONSIDERADO UMA VARÍAVEL COMPOSTA -> O B É A 
                        POSIÇÃO 0 DA STRING, O R É A POSIÇÃO 1 DA STRING E ASSIM POR DIANTE...

                - FATIAMENTO DE STRINGS:
                    => print(lanche[2]) -> vai 'printar' o elemento da tupla lanche que esta 
                    presente na posição 2

                    => print(lanche[0:2]) -> vai 'printar' os elementos presentes na posição 0 e 1, 
                    pois, ao colocar de 0 a 2, automaticamente o elemento dois é ignorado

                    => print(lanche[1:]) -> vai 'printar' do elemento 1 ate o final da tupla, ou seja, fatiamento
                    simples

                    => print(lanche[-1]) -> vai printar o último elemento da tupla, se fosse -2, 
                    seria o penúltimo elemento da tupla e assim por diante...

                    => len() -> é uma função/método que vem de length, que é comprimento e ao utilizar 
                    o len, por exemplo na variável lanche, iria retornar quantos elementos tem em lanche

                    => estrutura de repetição:

                        for c in lanche:
                            print(c) 

                        => no for acima será 'printado' todos os itens presentes em lanche
                        => no for pode ser usado tanto com o metódo range, com coleções, para varíaveis compostas, 
                        para tuplas...

            => AS TUPLAS SÃO IMUTÁVEIS => NÃO É POSSÍVEL ALTERAR OS VALORES PRESENTES EM UM TUPLA EM PYTHON
                - para poder mudar uma tupla, caso o programa já esteja rodando, vai ser preciso parar o mesmo, 
                alterar o valor contido na tupla e rodar o programa novamente

            => NO PYTHON A GENTE DIFERENCIA AS VARÍAVEIS COMPOSTAS DA SEGUINTE FORMA:
                - () => TUPLAS
                - [] => LISTAS
                - {} => DISCIONÁRIOS

        -> EXISTE UM MÉTODO DENTRO DA ÁREA DE TUPLAS EM PYTHON, QUE SE CHAMA SORTED
            -> ONDE NO CASO VAI ORGANIZAR(DEIXAR EM ORDEM) O ELEMENTO AO QUAL FOI APLICADO O SORTED


    => OPERAÇÕES COM TUPLAS EM  PYTHON

        - AO REALIZAR UMA SOMA ENTRE TUPLAS, NA VERDADE, VOCÊ ESTARÁ REALIZANDO UMA CONCATENAÇÃO
            a = (1, 5, 4)
            b = (5, 8, 1, 2)

            c = a + b 

            print(c) => (1, 5, 4, 5, 8, 1, 2)

            - a ordem sempre irá influenciar na ordem do resultado em tuplas

        - PROPRIEDADE COUNT -> SERVE PARA MOSTRAR QUANTAS VEZEZ APARECE UM ELEMENTO DENTRO DA TUPLA
        - PROPRIEDADE INDEX -> SERVE PARA MOSTRAR O INDEX/POSIÇÃO QUE SE ENCONTRA UM DETERMINADO VALOR
        - PARA APAGAR UMA DETERMINADA VARÍAVEL DENTRO DO PYTHON, NOS USAMOS A PALAVRA RESERVADA => DEL()

        - métodos para verificação de maior e menor valor de uma tupla => max() e min()

'''

a = (1, 5, 4)
b = (5, 8, 1, 2)

ab = a + b 
ba = b + a

print(f'CONCATENAÇÃO AB => {ab}')
print(f'CONCATENAÇÃO BA => {ba}')

pessoa = ('Brunno Manduca', 31, 'M', 78.3)
print(pessoa)

