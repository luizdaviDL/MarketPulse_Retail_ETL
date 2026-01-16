import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from .transformation.Drops import drop_columns, drop_duplicates
from .transformation.ValuesNull import updateNullValues
from .transformation.To_Mounth import month_to_number

def transformation(value):
    try:
        print("🚀 Starting data transformation...")
        
        # 1. Drop columns
        print("📊 Dropping columns...")
        data = drop_columns(value)
        data = drop_duplicates(data)
        print(f"✅ Columns dropped. Current shape: {data.shape}")
        
        # 2. Identify outliers
        print("🔍 Identifying outliers in Total_Amount...")
        Q1 = data['Total_Amount'].quantile(0.25)
        Q3 = data['Total_Amount'].quantile(0.75)
        IQR = Q3 - Q1
        limite_inferior = Q1 - 1.5 * IQR
        limite_superior = Q3 + 1.5 * IQR
        
        data['is_outlier_amount'] = (
            (data['Total_Amount'] < limite_inferior) | 
            (data['Total_Amount'] > limite_superior)
        )
        outliers_count = data['is_outlier_amount'].sum()
        print(f"✅ Outliers identified: {outliers_count} found ({outliers_count/len(data)*100:.2f}%)")
        
        # 3. Update null values
        print("🔄 Updating null values...")
        data = updateNullValues(data)
        null_count = data.isnull().sum().sum()
        print(f"✅ Null values updated. Remaining nulls: {null_count}")
        
        # 4. Convert month to number
        print("📅 Converting month names to numbers...")
        data = month_to_number(data)
        print(f"✅ Month conversion completed")
        
        # Final summary       
        print("🎯 TRANSFORMATION COMPLETED SUCCESSFULLY!")               
        return data
        
    except KeyError as e:
        print(f"❌ ERROR: Column not found - {e}")
        print("Check if 'Total_Amount' column exists in the dataset")
        raise
    except AttributeError as e:
        print(f"❌ ERROR: DataFrame method failed - {e}")
        raise
    except Exception as e:
        print(f"❌ UNEXPECTED ERROR during transformation: {type(e).__name__}")
        print(f"Error details: {str(e)}")
        print("Stopping transformation process...")
        raise