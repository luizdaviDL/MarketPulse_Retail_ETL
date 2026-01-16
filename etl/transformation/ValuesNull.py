import pandas as pd

'''
i put e median to replace null values in numerics columns and add string 
Not Informed to null categorics columns

'''
def updateNullValues(data):
    try:
        df = data.copy()
        
        categorical_columns = ['City', 'State', 'Country', 'Gender', 'Customer_Segment', 
                              'Product_Category', 'Product_Brand', 'Shipping_Method',
                              'Payment_Method', 'Order_Status','Month','Income']

        for col in categorical_columns:
            df[col] = df[col].fillna('Not Informed')
        
        numerical_columns = ['Age', 'Amount', 'Total_Amount', 'Year','Total_Purchases']

        for col in numerical_columns:
            if col in df.columns:                               
                if pd.api.types.is_numeric_dtype(df[col]):
                    median_value = df[col].median()
                    df[col] = df[col].fillna(median_value)            
                else:    
                    df[col] = df[col].fillna('Not Informed')
        
        return df
        
    except Exception:
        return data
