# import module
import streamlit as st
import time

# Title
st.title("Hello Title!!!")

# Subheader
st.subheader("Hello Subheader!!!")

# Header
st.header("Hello Header!!!")

# Markdown
st.markdown("Hello Markdown!!!")

# Text
st.text("Hello Text!!!")

# Code
st.code("print('Hello Code!!!')", language='python')

# Latex
st.latex(r"""
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
""")

# Write
st.write("Hello Write!!!")

# Caption
st.caption("This is a caption for the title.")

# Emoji
st.write("Hello :smile: Emoji!!!")

# Image
st.image("https://www.streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png", caption="Streamlit Logo")

# Audio
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3")

# Video
st.video("https://www.youtube.com/watch?v=2Vv-BfVoq4g", format="video/mp4")

# JSON
st.json({"name": "Streamlit", "type": "Web App Framework"})

# DataFrame
import pandas as pd
data = {
    'Column 1': [1, 2, 3],
    'Column 2': ['A', 'B', 'C']
}
df = pd.DataFrame(data)
st.dataframe(df, width=500, height=300)

# Table
st.table(df)

# Write a message
st.write("This is a simple Streamlit app demonstrating various components.")

# Checkbox
if st.checkbox("Show DataFrame"):
    st.dataframe(df)

# Radio buttons
option = st.radio("Choose an option:", ["Option 1", "Option 2", "Option 3"])
st.write(f"You selected: {option}")

# Selectbox
options = ["Option A", "Option B", "Option C"]
selected_option = st.selectbox("Select an option:", options)
st.write(f"You selected: {selected_option}")

# Multiselect
selected_options = st.multiselect("Select multiple options:", options)
st.write(f"You selected: {selected_options}")

# Slider
slider_value = st.slider("Select a value:", min_value=0, max_value=100, value=50)
st.write(f"Slider value: {slider_value}")

# Text input
text_input = st.text_input("Enter some text:")
st.write(f"You entered: {text_input}")

# Text area
text_area = st.text_area("Enter a longer text:")
st.write(f"You entered: {text_area}")

# Number input
number_input = st.number_input("Enter a number:", min_value=0, max_value=100, value=50)
st.write(f"You entered: {number_input}")

# Date input
date_input = st.date_input("Select a date:")
st.write(f"You selected: {date_input}")

# Time input
time_input = st.time_input("Select a time:")
st.write(f"You selected: {time_input}")

# File uploader
uploaded_file = st.file_uploader("Upload a file", type=["csv", "txt", "pdf"])
if uploaded_file is not None:
    st.write("File uploaded successfully!")
    # You can read the file content here if needed
    # For example, if it's a CSV file:
    if uploaded_file.type == "text/csv":
        df_uploaded = pd.read_csv(uploaded_file)
        st.dataframe(df_uploaded)

# Button
if st.button("Click Me"):
    st.write("Button clicked!")

# Progress bar
progress = st.progress(0)
for i in range(100):
    progress.progress(i + 1)
    time.sleep(0.05)  # Simulate some work being done

# Spinner
with st.spinner("Loading..."):
    time.sleep(2)  # Simulate some loading time

# Sidebar
st.sidebar.title("Sidebar Title")
st.sidebar.write("This is a sidebar.")

# Sidebar checkbox
if st.sidebar.checkbox("Show Sidebar DataFrame"):
    st.sidebar.dataframe(df)

# Sidebar selectbox
sidebar_option = st.sidebar.selectbox("Select an option in sidebar:", options)
st.sidebar.write(f"You selected: {sidebar_option}")

# Layouts
st.write("### Layouts")
col1, col2 = st.columns(2)
col1.write("This is the first column.")
col2.write("This is the second column.")

# Expander
with st.expander("Click to expand"):
    st.write("This is the content inside the expander.")

# Tabs
tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
with tab1:
    st.write("This is the content of Tab 1.")
with tab2:
    st.write("This is the content of Tab 2.")

# Footer
st.write("### Footer")
st.write("This is a simple footer message.")