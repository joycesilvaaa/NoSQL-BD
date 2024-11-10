# Mercado Livre - MongoDB

## Clone o projeto e acesse a branch `lista02`
```bash
git clone https://github.com/joycesilvaaa/NoSQL-BD.git
cd NoSQL-BD
git checkout lista02
````

## 1. Configuração do MongoDB

  ### 1.1 Criar Conta no MongoDB Atlas
  
  - Acesse o MongoDB Atlas (https://www.mongodb.com/cloud/atlas) e crie uma conta ou faça login.
  - Crie um novo cluster e configure o banco de dados conforme as instruções do MongoDB Atlas.
  - No painel do MongoDB Atlas, gere a URI de Conexão
  
### 1.2 Alterar o Arquivo connection_mongo dentro da pasta `config`

No arquivo de configuração para o MongoDB, substitua as credenciais da URI de conexão com o MongoDB Atlas:

- Substitua `username`, `password` e `cluster` com as suas credenciais reais do MongoDB Atlas.

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
