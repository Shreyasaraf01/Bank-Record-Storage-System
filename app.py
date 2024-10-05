import streamlit as st
from blockchain import Block, Blockchain  # Assume the blockchain code is in `blockchain.py`
import datetime

# Create the Blockchain only once using session state
if 'blockchain' not in st.session_state:
    st.session_state.blockchain = Blockchain()

# Streamlit UI
st.title("Bank Record Storage System Using Blockchain")

# Input form
sender = st.text_input("Sender")
receiver = st.text_input("Receiver")
amount = st.number_input("Amount", min_value=0.0, format="%.2f")

if st.button("Add Block"):
    if sender and receiver and amount:
        new_record = {"sender": sender, "receiver": receiver, "amount": amount}
        new_block = Block(len(st.session_state.blockchain.chain), datetime.datetime.now(), new_record, st.session_state.blockchain.get_latest_block().hash)
        st.session_state.blockchain.add_block(new_block)
        st.success("Block added successfully!")
    else:
        st.error("Please fill out all fields.")

# Display Blockchain
st.subheader("PyChain Ledger")
for block in st.session_state.blockchain.chain:
    st.write(block.__dict__)

# Validate Blockchain
if st.button("Validate Chain"):
    if st.session_state.blockchain.is_chain_valid():
        st.success("Blockchain is valid.")
    else:
        st.error("Blockchain is invalid.")
