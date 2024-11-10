# Mercado Livre - Cassandra
## Clone o projeto e acesse a branch `lista04`
```bash
git clone https://github.com/joycesilvaaa/NoSQL-BD.git
cd NoSQL-BD
git checkout lista04
````

## 1. Criar um Cluster Cassandra chamado `mercado_livre`

### 1.1 Criar Cluster na Nuvem

- Acesse [Datastax Astra](https://astra.datastax.com/).
- Crie uma conta ou faça login.
- Crie um novo **database** e configure o cluster.
- Baixe o arquivo `secure connect bundle`.
  
## 2. Configuração do Arquivo `connection_cassandra`

- O arquivo `secure connect bundle` do Cassandra Cloud e coloque na pasta `config/`.
-  Altere o nome do arquivo no código:
  ```python
     cloud_config = {
                'secure_connect_bundle': 'config/nome_do_seu_arquivo.zip'
            }
  ````
- No código, insira o **token** de acesso no trecho:

  ```python
  auth_provider = PlainTextAuthProvider(username='token', password='SEU_TOKEN_AQUI')

## 2. Criar Ambiente Virtual

### Usando `venv` (Python 3.x):

1. **Criação do Ambiente Virtual**:
   - No terminal, navegue até a pasta do projeto e execute:
     ```bash
     python -m venv venv
     ```

2. **Ativar o Ambiente Virtual**:

   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```

   - **Mac/Linux**:
     ```bash
     source venv/bin/activate
     ```

3. **Instalar as Dependências**:
   - Com o ambiente virtual ativado, instale as dependências necessárias:
     ```bash
     pip install -r requirements.txt
     ```

## 4. Rodar o Projeto
  - Utilize o comando:
      ```python
      python main.py
      ```
