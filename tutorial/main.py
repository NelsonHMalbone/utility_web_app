import streamlit as st
from excel_to_json import convert_excel_to_json

# difference between webapp and script
# webapp requires a frontend and backend frame works excel_to_json.py is the backend main.py
# is the front end best to keep these in separate files


st.title('Excel to Json File Convorter')
st.write("Upload an Excel file to Convert to a JSON format")


uploaded_file = st.file_uploader('Choose an Excel file', type=['xlsx', 'xls'])
# type allows to place the format of file to place insto drop box
# xls older excel file format
# xlsx newer excel file format

# logical for if file is None  will not run
if uploaded_file is not None:
    json_data = convert_excel_to_json(uploaded_file)
    st.json(json_data) # will display in json format on webpage

    st.download_button(label="Download Json",
                       data=json_data,
                       file_name='converted.json',
                       mime='application/json')
