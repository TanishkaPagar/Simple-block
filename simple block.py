import streamlit as st

# Title
st.title("Simple Blockchain Block Creator")

# Inputs for block details
st.header("Enter Block Information")

index = st.number_input("Block Index", min_value=1, step=1, value=1)
data = st.text_input("Block Data", value="patient A - X-ray scan")
timestamp = st.text_input("Timestamp", value="2025-04-05 10:00:00")
previous_block = st.text_input("Previous Block Hash (optional)", value="None")

# Button to create the block
if st.button("Create Block"):
    block = {
        "index": index,
        "data": data,
        "timestamp": timestamp,
        "previous_block": None if previous_block == "None" else previous_block
    }

    # Display the block
    st.subheader("Created Block")
    st.json(block)
