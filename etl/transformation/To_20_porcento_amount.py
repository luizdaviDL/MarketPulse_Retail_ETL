from etl.transformation.Format_columns import format_columns_br, update_age_float
import pandas as pd

def pareto_amount(data):
    try:
        df = data[data['is_outlier_amount'] == True]
        
        if len(df) == 0:
            print("⚠️ No outliers found")
            return pd.DataFrame()
            
        n_20pct = max(1, int(len(df) * 0.2))
        top_20_amount = df.nlargest(n_20pct, 'Total_Amount')
        
        top_20_amount = format_columns_br(top_20_amount)
        top_20_amount = update_age_float(top_20_amount)
        
        return top_20_amount
        
    except KeyError as e:
        print(f"❌ Column error: {str(e)}")
        return pd.DataFrame()
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")
        return pd.DataFrame()
