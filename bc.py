import streamlit as st
import pandas as pd

# Set the page configuration
st.set_page_config(
    page_title="Data Comparison Checker",
    page_icon="🔍",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Add a title and description
st.title("🔍 Data Comparison Checker")
st.markdown("""
    This app checks for repeated data and unique data between two predefined Excel files. 
    Click the button below to check for repeated and unique entries.
""")

# File paths on the backend
file1_path = 'BC3D_list_ 2024_06.xlsx'
file2_path = 'Bucket_Camera_Aug_21 2024.xlsx'

# Add a button to trigger the check
if st.button("Check Data"):
    # Load the files into dataframes
    df1 = pd.read_excel(file1_path)
    df2 = pd.read_excel(file2_path)

    # Identify common columns to check for repeated data
    common_columns = df1.columns.intersection(df2.columns).tolist()

    if common_columns:
        # Find repeated data between the two files
        repeated_data = pd.merge(df1, df2, on=common_columns, how='inner')

        # Find data unique to each file
        unique_to_file1 = df1[~df1.set_index(common_columns).index.isin(df2.set_index(common_columns).index)]
        unique_to_file2 = df2[~df2.set_index(common_columns).index.isin(df1.set_index(common_columns).index)]

        # Display the results
        if not repeated_data.empty:
            st.success("Repeated data found:")
            st.dataframe(repeated_data)
        else:
            st.info("No repeated data found.")

        if not unique_to_file1.empty:
            st.warning("Data unique to `BC3D_list_ 2024_06.xlsx`:")
            st.dataframe(unique_to_file1)

        if not unique_to_file2.empty:
            st.warning("Data unique to `Bucket_Camera_Aug_21 2024.xlsx`:")
            st.dataframe(unique_to_file2)
    else:
        st.warning("No common columns found between the two files.")
