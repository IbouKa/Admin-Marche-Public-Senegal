import pandas as pd
import streamlit as st
from io import StringIO
from base_module.convert_file import convert_string_to_csv
from base_module.preprocessing_data import *

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    # st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    # st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    # st.write(string_data)

    csv_data = convert_string_to_csv(string_data)
    #st.write(csv_data)
    #st.download_button('Download CSV', csv_data.to_csv(header=True), 'text.csv')



    # Can be used wherever a "file-like" object is accepted:
    # dataframe = pd.read_csv(uploaded_file)
    # dataframe.to_csv('dd.csv')

    # Normaliser avec le bon Orthographe
    csv_data.Type = csv_data.Type.apply(normalize_Type)

    csv_data.Mode_passation = csv_data.Mode_passation.apply(normalize_mode_passation)

    csv_data["Clean_Date"] = csv_data.Date.apply(normalize_date)
    csv_data["Year"] = csv_data.Clean_Date.apply(get_year)
    csv_data["Month"] = csv_data.Clean_Date.apply(get_month)
    csv_data["Day"] = csv_data.Clean_Date.apply(get_day)
    csv_data["Trimestre"] = csv_data.Clean_Date.apply(get_trimestre)

    csv_data['Montant_cfa'] = csv_data.apply(lambda x: normalize_montant_in_fca_W_date(x.Clean_Date, x.Montant), axis=1)
    csv_data["Montant_cfa"] = pd.to_numeric(csv_data["Montant_cfa"])

    replace_comma_to_espace_in_df(csv_data)

    st.write(csv_data)
