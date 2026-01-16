from config.database import get_db_engine, get_table_name


def load_data(df):
    try:
        engine = get_db_engine()
        table_name = get_table_name()
        
        df.to_sql(
            table_name,    
            engine,
            if_exists='replace',
            index=False
        )
        
        print(f"✅ Datas already saved '{table_name}'")
        return True
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False
    