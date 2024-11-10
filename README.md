# Mercado Livre -MongoDB e Redis

## Clone o projeto e acesse a branch `lista03`
```bash
git clone https://github.com/joycesilvaaa/NoSQL-BD.git
cd NoSQL-BD
git checkout lista03
````

## 1. Configuração do MongoDB

  1.1 Criar Conta no MongoDB Atlas
  
  - Acesse o MongoDB Atlas (https://www.mongodb.com/cloud/atlas) e crie uma conta ou faça login.
  - Crie um novo cluster e configure o banco de dados conforme as instruções do MongoDB Atlas.
  - No painel do MongoDB Atlas, gere a URI de Conexão
  
1.2 Alterar o Arquivo connection_mongo dentro da pasta `config`

No arquivo de configuração para o MongoDB, substitua as credenciais da URI de conexão com o MongoDB Atlas:

- Substitua `username`, `password` e `cluster` com as suas credenciais reais do MongoDB Atlas.

## 2. Configuração do Redis

2.1 Criar Conta no Redis Cloud

- Acesse Redis Cloud (https://redis.com/redis-cloud/) e crie uma conta.
- Após a criação da conta, crie um novo banco de dados Redis e obtenha as credenciais necessárias (host, port e password).

2.2 Alterar o Arquivo connection_redis

No arquivo de configuração para o Redis, substitua as credenciais com as informações da sua conta no Redis Cloud:

- Substitua `host`, `port` e `password` com as credenciais reais obtidas ao criar seu banco Redis.

## 3. Instalar as Dependências

- Crie um ambiente virtual e instale as dependências utilizando o pip:

  1. Criação do Ambiente Virtual:
     - No terminal, navegue até a pasta do projeto e execute:
       ````
       python -m venv venv
       ````

  2. Ativar o Ambiente Virtual:
     - Em Windows:
       ````
       venv\Scripts\activate

     - Em Mac/Linux:
       ````
       source venv/bin/activate

  3. Instalar as Dependências:
     - Com o ambiente virtual ativado, execute o seguinte comando:
       ````
       pip install -r requirements.txt

 ## 4. Rodar o Projeto
- Para rodar o projeto, execute o seguinte comando:
  ```
  python main.py
