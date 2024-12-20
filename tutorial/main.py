import streamlit as st
import openpyxl as op
from excel_to_json import convert_excel_to_json

# difference between webapp and script
# webapp requires a frontend and backend frame works excel_to_json.py is the backend main.py
# is the front end best to keep these in separate files


st.title('Excel to Json File Convorter')
st.write("Upload a excel file to convert")

