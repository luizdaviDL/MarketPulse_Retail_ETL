import pandas as pd

def extract():
    try:
        data = pd.read_csv("data/retail_data.csv")
        print("✅ Data uploaded successfully")
        print(f"   • Memory: {data.memory_usage(deep=True).sum() / 1024 / 1024:.2f} MB")
        return data
    except FileNotFoundError:
        print("Erro: arquivo não encontrado.")
    except Exception as e:
        print(f"Erro ao extrair dados: {e}")
