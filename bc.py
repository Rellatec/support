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
    This app checks if there is any new data in `Bucket_Camera_Aug_21 2024.xlsx` that is not present in `BC3D_list_ 2024_06.xlsx`.
    Click the button below to start the process.
""")

# File paths on the backend
initial_file_path = 'BC3D_list_ 2024_06.xlsx'
new_file_path = 'Bucket_Camera_Aug_21 2024.xlsx'

# Add a button to trigger the check for new data
if st.button("Check for New Data"):
    # Load the initial and new files into dataframes
    df_initial = pd.read_excel(initial_file_path)
    df_new = pd.read_excel(new_file_path)

    # Identify common columns to check for new data
    common_columns = df_initial.columns.intersection(df_new.columns).tolist()

    if common_columns:
        # Check for new data in the new file that is not in the initial file
        new_data = df_new[~df_new.set_index(common_columns).index.isin(df_initial.set_index(common_columns).index)]

        # Display the results
        if not new_data.empty:
            st.success("New data found in `Bucket_Camera_Aug_21 2024.xlsx`:")
            st.dataframe(new_data)
        else:
            st.info("No new data found in `Bucket_Camera_Aug_21 2024.xlsx`.")
    else:
        st.warning("No common columns found between the two files.")
