import streamlit as st
from datetime import datetime

 

# Set the maximum number of units allowed for trading
MAX_UNITS = 100  # Adjust this value to fit your investment strategy

 

# Initialize session state to store asset data and investment status
if 'assets' not in st.session_state:
    st.session_state.assets = {}
if 'investing' not in st.session_state:
    st.session_state.investing = {}

 

# Function to start investing in a particular asset
def start_investing(asset_name):
    st.session_state.investing[asset_name] = datetime.now()

 

# Function to end the investment in a particular asset
def end_investing(asset_name):
    if asset_name in st.session_state.investing:
        start_time = st.session_state.investing.pop(asset_name)
        elapsed_time = datetime.now() - start_time
        st.session_state.assets[asset_name] = st.session_state.assets.get(asset_name, 0) + elapsed_time.total_seconds() / 3600

 

# Page layout: create columns to organize the UI elements
col1, col2 = st.columns([1, 3])

 

with col1:
    st.header("Your Financial Assets")
    total_units = 0
    for asset, units in st.session_state.assets.items():
        st.write(f"**{asset}**: {units:.2f} units traded")
        if asset in st.session_state.investing:
            if st.button(f"End trading for {asset}", key=f"end_{asset}"):
                end_investing(asset)
        else:
            if st.button(f"Start trading {asset}", key=f"start_{asset}"):
                start_investing(asset)
        total_units += units

 

with col2:
    st.title("Manage Your Money Wisely")

    # UI for adding a new financial asset
    asset_name = st.text_input("Enter asset name (e.g., gold, dollar):")
    if st.button("Add Asset"):
        if asset_name:
            st.session_state.assets[asset_name] = 0
            st.success(f"Successfully added {asset_name}.")
        else:
            st.error("Please enter an asset name.")

 

    # Display total traded units and check if it exceeds the maximum
    if total_units > MAX_UNITS:
        st.warning(f"Warning: You have exceeded the maximum allowed units! Total traded units: {total_units:.2f}")
    else:
        st.info(f"Total traded units: {total_units:.2f} / {MAX_UNITS} units")