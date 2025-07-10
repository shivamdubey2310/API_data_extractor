# Front end design of the app

import streamlit as st
import time
import BackEnd

st.title("Api Data Extractor")
st.header("Here you can extract data from any Free Public API")

API_link = st.text_input("Paste the API Link here:")
API_link = API_link.strip()

domain_name = BackEnd.extract_domain_name(API_link)

if domain_name == API_link:
    st.write(f"Invalid link!!!")
else:
    st.write(f"Starting extraction from {domain_name}")
    BackEnd.Extracting_data(API_link, domain_name)

st.write("Download your json data file here")

raw_file_name = f"raw_json/{domain_name}_raw.json"


with open(raw_file_name, "r") as fileReader:
    st.download_button(f"Download", fileReader, file_name="Data.json")