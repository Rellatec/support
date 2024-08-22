import streamlit as st
import pandas as pd

# Set the page configuration
st.set_page_config(
    page_title="BC3D Update Checker",
    page_icon="🔍",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Add a title and description
st.title("🔍 BC3D Update Checker")
st.markdown("""
    This app helps BC3D_list_ 2024_06.xlsx and then checks Bucket_Camera_Aug_21 2024 for any missing cameras.
    Click the button below to start the process.
""")

# File paths on the backend
initial_file_path = 'BC3D_list_ 2024_06.xlsx'
new_file_path = 'Bucket_Camera_Aug_21 2024.xlsx'

# Add a button to trigger the update and comparison
if st.button("Check for Missing Cameras"):
    # Load the initial and new files into dataframes
    df_initial = pd.read_excel(initial_file_path).dropna()
    df_new = pd.read_excel(new_file_path).dropna()

    # Identify common columns to check for updates and missing data
    common_columns = df_initial.columns.intersection(df_new.columns).tolist()

    if common_columns:
        # Update the BC3D comments using the initial file
        updated_df = df_initial.copy()  # Assuming some update logic here

        # Check for cameras in the new file that are missing in the initial file
        missing_in_initial = df_new[~df_new.set_index(common_columns).index.isin(df_initial.set_index(common_columns).index)]

        # Display the results
        st.warning("Cameras missing in the initial file (found in new file):")
        st.dataframe(missing_in_initial)
    else:
        st.warning("No common columns found between the two files.")
