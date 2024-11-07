def create_collection(session):
    try:
        session.execute("USE mercado_livre")

        session.execute("""
            CREATE TYPE IF NOT EXISTS produto(
                produto_id UUID,
                nome_produto TEXT,
                marca_produto TEXT,
                valor DECIMAL,
                vendedor_id UUID,
                nome_vendedor TEXT, 
                email_vendedor TEXT,
                cnpj_vendedor TEXT
            )
        """)

        session.execute("""
            CREATE TYPE IF NOT EXISTS compra (
                produto_id UUID,
                nome_produto TEXT,
                marca_produto TEXT,
                valor DECIMAL,
                quantidade INT,
                vendedor_id UUID,
                nome_vendedor TEXT, 
                email_vendedor TEXT,
                cnpj_vendedor TEXT
            )
        """)

        session.execute("""
            CREATE TYPE IF NOT EXISTS endereco (
                rua TEXT,
                numero TEXT,
                tipo_imovel TEXT,
                complemento TEXT,
                bairro TEXT,
                cidade TEXT,
                estado TEXT
            )
        """)

        session.execute("""
            CREATE TABLE IF NOT EXISTS user (
                id UUID PRIMARY KEY,
                nome TEXT,
                email TEXT,
                cpf TEXT,
                senha TEXT,
                endereco LIST<FROZEN<endereco>>,  
                favoritos LIST<FROZEN<produto>>,  
                compras LIST<FROZEN<compra>>       
            )
        """)

        session.execute("""
            CREATE TABLE IF NOT EXISTS purchase (
                id UUID PRIMARY KEY,
                user_id UUID, 
                data_compra TIMESTAMP,
                valor_total DECIMAL,
                produtos LIST<FROZEN<compra>>, 
                endereco_entrega FROZEN<endereco>,
                status TEXT
            )
        """)

        session.execute("""
            CREATE TABLE IF NOT EXISTS seller (
                id UUID PRIMARY KEY,
                nome TEXT,
                email TEXT,
                cnpj TEXT,
                avaliacao INT,
                endereco LIST<FROZEN<endereco>>,  
                produtos LIST<FROZEN<produto>>  
            )
        """)

        session.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id UUID PRIMARY KEY,
                nome_produto TEXT,
                marca_produto TEXT,
                valor DECIMAL,
                estoque INT,
                vendas INT,
                vendedor_id UUID, 
                nome_vendedor TEXT, 
                email_vendedor TEXT,
                cnpj_vendedor TEXT
            )
        """)
        return
    except Exception as e:
        print(f'Erro ao criar coleções: {e}')
        return
