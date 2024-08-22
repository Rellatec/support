import streamlit as st
import pandas as pd

# Set the page configuration
st.set_page_config(
    page_title="Repeated Data Checker",
    page_icon="🔍",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Add a title and description
st.title("🔍 Repeated Data Checker")
st.markdown("""
    This app checks for repeated data between two predefined Excel files. 
    Click the button below to check for repeated entries.
""")

# File paths on the backend
file1_path = 'BC3D_list_ 2024_06.xlsx'
file2_path = 'Bucket_Camera_Aug_21 2024.xlsx'

# Add a button to trigger the check
if st.button("Check for Repeated Data"):
    # Load the files into dataframes
    df1 = pd.read_excel(file1_path)
    df2 = pd.read_excel(file2_path)

    # Identify common columns to check for repeated data
    common_columns = df1.columns.intersection(df2.columns).tolist()

    if common_columns:
        # Find repeated data between the two files
        repeated_data = pd.merge(df1, df2, on=common_columns, how='inner')

        if not repeated_data.empty:
            st.success("Repeated data found:")
            st.dataframe(repeated_data)
        else:
            st.info("No repeated data found.")
    else:
        st.warning("No common columns found between the two files.")
