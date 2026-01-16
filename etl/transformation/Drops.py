

def drop_columns(data):
    try:
        values = [
            'Transaction_ID', 'Customer_ID', 'Name', 'Email',
            'Phone', 'Address', 'Zipcode', 'Feedback', 'Ratings','Time','Date'
        ]
        data = data.drop(columns=values, errors='ignore')
        return data
    except Exception as e:
        print(f"Erro to remove columns: {e}")
        return data
