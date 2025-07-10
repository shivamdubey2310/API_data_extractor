import streamlit as st
import time
import BackEnd
import os
from datetime import datetime

# Set page configuration
st.set_page_config(page_title="API Data Extractor", layout="centered", page_icon="🔍")

# ----- Main UI -----
st.title("🔍 API Data Extractor")
st.markdown("""
<div style='font-size:18px;'>
    Easily extract and download structured data from any <b>free public API</b>. Paste your link below to get started.
</div>
""", unsafe_allow_html=True)

# UI Styling - Section Separator
st.markdown("---")

# ----- Input Section -----
st.markdown("### 🔗 Enter Your API Link Below:")
API_link = st.text_input("API Endpoint", placeholder="https://example.com/api/data")
API_link = API_link.strip()

# Additional user options
with st.expander("⚙️ Advanced Options"):
    show_preview = st.checkbox("Show data preview after extraction", value=True)
    timestamp_file = st.checkbox("Add timestamp to downloaded file", value=False)

# Process the link if entered
if API_link:
    domain_name = BackEnd.extract_domain_name(API_link)

    if domain_name == API_link:
        st.error("❌ Invalid API link. Please check the URL format.")
    else:
        with st.spinner(f"🔄 Extracting data from `{domain_name}`..."):
            time.sleep(1)
            BackEnd.Extracting_data(API_link, domain_name)

        st.success(f"✅ Data extraction completed from `{domain_name}`")

        # UI Styling - Section Separator
        st.markdown("---")

        # File Path
        raw_file_name = f"raw_json/{domain_name}_raw.json"

        # Check file existence
        if os.path.exists(raw_file_name):
            st.markdown("### 📥 Download Extracted Data")
            download_file_name = f"{domain_name}_data.json"
            if timestamp_file:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                download_file_name = f"{domain_name}_{timestamp}.json"

            with open(raw_file_name, "rb") as fileReader:
                st.download_button(
                    label="⬇️ Download JSON File",
                    data=fileReader,
                    file_name=download_file_name,
                    mime="application/json"
                )

            # Optional Preview
            if show_preview:
                st.markdown("### 👁️ Data Preview")
                with open(raw_file_name, "r") as preview_file:
                    json_data = preview_file.read()
                    st.code(json_data[:3000], language='json')  # preview first 3000 characters

        else:
            st.warning("⚠️ Data file not found. Please try again.")

# Footer
st.markdown("""
---
<div style='text-align: center; font-size: 14px;'>
    Made with ❤️ using Streamlit | Data Engineering Utility Tool
</div>
""", unsafe_allow_html=True)
