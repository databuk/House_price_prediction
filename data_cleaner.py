from datetime import datetime
def clean_data(data):
    current_year = datetime.now().year
    if 'HouseAge' in data.columns:
        data['age'] = current_year - data['HouseAge']
        data.drop(columns=['HouseAge'], axis=1, errors='ignore', inplace=True)
    data.columns = data.columns.str.lower()
    return data
