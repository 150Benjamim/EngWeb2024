# TPC2

**Cidades de Portugal**

- **Data de início:** 19/02/2024
- **Data de fim:** 26/02/2024


# Objetivos do trabalho

- Criar uma página estática para cada cidade.
- Criar uma página inicial com uma lista das cidades, em que cada cidade é um link (utilizando um serviço node.js por baixo).
- Cada página da cidade deve ter a informação respetiva, e as ligações com nome da cidade e link com chamada ao servidor (como em cima).

# Resumo do trabalho

- **Página Principal e Páginas das Cidades:**
Decidi usar Python de forma a desenvolver scripts de forma a automatizar a criação das páginas.

De forma a criar a página principal comecei por ler os dados de um arquivo JSON contendo informações sobre cidades e suas conexões. Em seguida, a partir destes dados gero uma página inicial listando todas as cidades por ordem alfabética, com links para páginas individuais de cada cidade.

Depois, para cada cidade, criei uma página dedicada com detalhes como população, descrição e distrito. Além disso, listei as cidades conectadas a essa cidade e a distância entre elas. As páginas são geradas em HTML e organizadas num folder chamado "mapa_site".


- **Servidor Node.js:**
De forma a implementar o serviçor node.js comecei por importar as bibliotecas necessárias: http, fs, e url. Em seguida, criei um servidor HTTP usando http.createServer(), onde tratei as requisições e respostas.

Dentro da função de callback, analisei o URL da requisição usando o módulo url. Dependendo do path URL, o servidor responde de diferentes maneiras:

    Se a URL corresponder ao padrão /c\d+, o servidor envia o arquivo HTML correspondente, ou com um erro 404 (Not Found) cajo a página não exista.
    Se a URL for /w3.css, o servidor envia o arquivo CSS.
    Se a URL for /, o servidor envia o arquivo "index.html".
    Para qualquer outro caminho, o servidor responde com um erro 400 (Bad Request).

Por fim, configurei o servidor para escutar na porta 7777. Com isso, o servidor está pronto para lidar com as requisições e fornecer as respostas adequadas.
