import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def get_db_engine():
    try:
        print("🔌 Connecting to database...")
        engine = create_engine(
            f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
            f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
        )
        print("✅ Database connection successful")
        return engine
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return None
    
def get_table_name(): 
    return os.getenv('DB_NAME', 'marketpulse_retail')  # default    

def table_pareto_top_20(): 
    return os.getenv('DB_PARETO_NAME', 'top_20_porcent_amount')  # default   