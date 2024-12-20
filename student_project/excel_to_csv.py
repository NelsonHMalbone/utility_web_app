import pandas as pd

filename = 'europe.xlsx'
new_filename = 'europe.csv'

def excel_to_csv_convertor(filename):
    df = pd.read_excel(filename)
    csv_data = df.to_csv(index=False)

    return csv_data


