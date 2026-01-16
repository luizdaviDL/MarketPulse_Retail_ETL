def month_to_number(data):
    try:
        month_map = {
            'January': 1, 'February': 2, 'March': 3, 'April': 4,
            'May': 5, 'June': 6, 'July': 7, 'August': 8,
            'September': 9, 'October': 10, 'November': 11, 'December': 12,
            'Not Informed': None
        }
        
        if 'Month' in data.columns:
            data['Month_Number'] = data['Month'].map(month_map)
        
        return data
        
    except Exception:
        return data