def create_collection(session):
    try:
        session.execute("USE mercado_livre")

        # session.execute("DROP TABLE IF EXISTS user")
        # session.execute("DROP TABLE IF EXISTS purchase")
        # session.execute("DROP TABLE IF EXISTS seller")
        # session.execute("DROP TABLE IF EXISTS products")

        session.execute("""
            CREATE TABLE IF NOT EXISTS user (
                id UUID PRIMARY KEY,
                nome TEXT,
                email TEXT,
                cpf TEXT,
                senha TEXT,
                enderecos LIST<FROZEN<MAP<TEXT, TEXT>>>,  -- Lista de mapas congelados para endereços
                favoritos LIST<FROZEN<MAP<TEXT, TEXT>>>,  -- Lista de mapas congelados para favoritos
                compras LIST<FROZEN<MAP<TEXT, TEXT>>>     -- Lista de mapas congelados para compras
            )
        """)

        session.execute("""
            CREATE TABLE IF NOT EXISTS purchase (
                id UUID PRIMARY KEY,
                user_id UUID,
                data_compra TIMESTAMP,
                valor_total DECIMAL,
                produtos LIST<FROZEN<MAP<TEXT, TEXT>>>,         -- Lista de produtos como mapas congelados
                endereco_entrega FROZEN<MAP<TEXT, TEXT>>,       -- Endereço de entrega como mapa congelado
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
                enderecos LIST<FROZEN<MAP<TEXT, TEXT>>>,  -- Lista de endereços como mapas congelados
                produtos LIST<FROZEN<MAP<TEXT, TEXT>>>    -- Lista de produtos como mapas congelados
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

        print("Todas as tabelas foram criadas com sucesso.")
    except Exception as e:
        print(f'Erro ao criar tabelas: {e}')
