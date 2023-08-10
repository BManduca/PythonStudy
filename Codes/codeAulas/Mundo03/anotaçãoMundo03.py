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

----------------------------------------------------------------------------------------------------------

- Aula 17

    => LISTAS: são compostas por [] e não parentêses como nas tuplas 

    => principal diferença entre listas e tuplas, é que a tupla é imutável e as listas
    não são

    => para adicionar elementos na lista, usamos o comando append()
        -> lista.append('')

    => para adicionarmos elementos em posições específicas na lista, usaremos o 
    comando insert()
        -> lista.insert(posição,'')

    => métodos para eliminar elementos de uma lista:
        -> del lista[3]
        - lista.pop(3) -> ao colocar somente lista.pop(), será eliminado
        o último elemento
        - lista.remove('') -> não indica o index e sim o valor que será eliminado e sempre elimina
        o primeiro valor encontrado, caso exista mais de um mesmo valor escolhido

    => condicionais com lista:
        if '' in lista:
            lista.remove('')

    => criando listas através de rand's
        -> valores = list(range(4,11))
        -> essa lista vira totalmente ordenada

    => criando lista desordenada
        -> valores = [8, 4, 9, 3, 1, 7, 0]
            -> valores.sort() => ordenando a lista

            -> aplicando metodo sort com ordem inversa
                - valores.sort(reverse=True)

    => Sabendo o tamanho da lista
        -> valores = [8, 1, 6, 9, 4, 5, 0]
        -> len(valores)
    
        
    ----------------------------------------------------------------
    aux = ['Brunno', 'João', 'Maria', 'Felipe']

    print(aux)

    aux[2] = 'Rodrigo'

    print(aux)

    => as respostas serão diferentes..
    ----------------------------------------------------------------

    => Funcionalidades com listas:
        - ao igualar uma lista com outra, ou seja, fazer uma lista receber outra:
            a = [2, 8, 6, 1]
            b = a

            - automaticamente quando fazemos a operação de uma lista receber outra, 
            elas criam uma ligação entre si e desta forma se alterarmos algum valor,
            por exemplo em b, na lista a também será alterada

        - mas podemos fazer com que a lista b recebe todos os elementos da lista a, 
        através de fatiamento:
            - b = a[:]
            - desta forma, não é criado uma 'ligação' entre as listas como vimos
            anteriomente... e sim vai ser feito uma cópia 



'''

# a = (1, 5, 4)
# b = (5, 8, 1, 2)

# ab = a + b 
# ba = b + a

# print(f'CONCATENAÇÃO AB => {ab}')
# print(f'CONCATENAÇÃO BA => {ba}')

# pessoa = ('Brunno Manduca', 31, 'M', 78.3)
# print(pessoa)


aux = ['Brunno', 'João', 'Maria', 'Felipe']

# print(aux)

aux[2] = 'Rodrigo'

print(aux)