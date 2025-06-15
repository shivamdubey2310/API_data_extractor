import streamlit as st
import time
import BackEnd
import os

# Set page config
st.set_page_config(page_title="API Data Extractor", layout="centered")

# Main Title and Subtitle
st.title("API Data Extractor")
st.subheader("Extract and Download Data from Any Free Public API")

# UI Styling - Section Separator
st.markdown("---")

# Input Field
st.markdown("### Paste your API Link below:")
API_link = st.text_input("API Endpoint", placeholder="https://example.com/api/data")
API_link = API_link.strip()

# Validate and Process the Link
if API_link:
    domain_name = BackEnd.extract_domain_name(API_link)

    if domain_name == API_link:
        st.error("Invalid API link. Please check the URL format.")
    else:
        with st.spinner(f"Extracting data from `{domain_name}`..."):
            time.sleep(5)  # Optional spinner delay for better UX
            BackEnd.Extracting_data(API_link, domain_name)
        st.success(f"Data extraction completed from `{domain_name}`")

        # UI Styling - Section Separator
        st.markdown("---")

        # File Path
        raw_file_name = f"raw_json/{domain_name}_raw.json"

        # Check if the file exists before attempting to download
        if os.path.exists(raw_file_name):
            st.markdown("### Download your extracted JSON data")
            with open(raw_file_name, "rb") as fileReader:
                st.download_button(
                    label="Download JSON File",
                    data=fileReader,
                    file_name=f"{domain_name}_data.json",
                    mime="application/json"
                )
        else:
            st.warning("Data file not found. Please try again.")
