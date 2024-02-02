## Manipulação de dados com PyMongo

- Install your driver
    - python -m pip install "pymongo[srv]"
<br><br>
- Iniciando:
    - Inicialmente criar uma conta no MondoDB
    - criar uma database
    - Criar um user -> Database Access
    - Para fazer a conexão, é necessário 'pegar' uma connection string e adicionar dentro da aplicação => essa connection string é possível pegar dentro do mongo, na área de connect da sua database.
        - database -> Connect
    - Sempre validar se o IP esta pegando corretamente
        - é possível verificar dentro da pagina do mongodb atlas em: Security -> Network Access


- ## Inserindo coleções nas databases
    - 'dentro' de uma database podemos criar um document e inserir ele via mongodb, através de uma estrutura JSON e logo em seguida inserir os dados 


- ## Acessando Banco de Dados MongoDB com Python
    - ### Estrutura do Mongodb - Aula 24
        - O Mongodb é contruído por uma base de dados
        - Essa base de dados vai ter coleções
            - São unidades básicas de dados. 
            - Formatados como Binary JSON
            - esses documentos podem armazenar vários tipos de dados e ser distribuídos para diversos sistemas.
        - As coleções vão ter documentos
        - Os documentos são inseridos por nós usuários.


- ## Coleções - Aula 25
    - 