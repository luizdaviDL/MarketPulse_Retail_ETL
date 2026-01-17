import pandas as pd

def format_columns_br(df):
    try:
        df_formatted = df.copy()
        columns_to_format = ['Total_Purchases', 'Amount', 'Total_Amount']
        
        for col in columns_to_format:
            if col in df_formatted.columns:
                if pd.api.types.is_numeric_dtype(df_formatted[col]):
                    if pd.api.types.is_float_dtype(df_formatted[col]):
                        df_formatted[col] = df_formatted[col].apply(
                            lambda x: f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
                            if pd.notnull(x) else ""
                        )
                    else:  # int
                        df_formatted[col] = df_formatted[col].apply(
                            lambda x: f"{x:,}".replace(",", ".")
                            if pd.notnull(x) else ""
                        )
        
        return df_formatted
    
    except Exception as e:
        print(f"Erro em format_columns_br: {e}")
        return df

def update_age_float(df, colum='Age'):
    try:
        df_corrigido = df.copy()
        
        if colum in df_corrigido.columns:
            if pd.api.types.is_numeric_dtype(df_corrigido[colum]):
                df_corrigido[colum] = df_corrigido[colum].astype(int)
        
        return df_corrigido
    
    except Exception as e:
        print(f"Erro em update_age_float: {e}")
        return df