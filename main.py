import streamlit as st
from io import StringIO
from base_module.convert_file import convert_string_to_csv

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
    st.write(csv_data)
    st.download_button('Download CSV', csv_data.to_csv(header=True), 'text.csv')

    # Can be used wherever a "file-like" object is accepted:
    # dataframe = pd.read_csv(uploaded_file)
    # dataframe.to_csv('dd.csv')
