import  streamlit as st
from excel_to_csv import excel_to_csv_convertor

st.title("Excel to CSV File Converter")
st.write('Upload an Excel file to Convert to a CSV format')

# file selector
upload_file = st.file_uploader('Choose an Excel File', type=['xlsx', 'xls'])

if upload_file is not None:
    csv_data = excel_to_csv_convertor(upload_file)
    st.download_button(label='Download File',
                       data=csv_data,
                       file_name='converted.csv',
                       mime='application/csv')