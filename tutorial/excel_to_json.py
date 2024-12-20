import pandas as pd



# requires a input of excel file
def convert_excel_to_json(excel_file):

    df = pd.read_excel(excel_file)
    json_data = df.to_json(orient='records')

    # output json data
    return json_data

# get rid of europe.json to print in console
# print(convert_excel_to_json('europe.xlsx'))
