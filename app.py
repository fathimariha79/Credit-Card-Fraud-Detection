import streamlit as st

st.title("Credit Card Fraud Detection")

amount = st.number_input("Enter Transaction Amount")

if st.button("Predict"):

    # Simple fraud rule

    if amount < 25000:
        st.success("Legitimate Transaction")

    else:
        st.error("Fraudulent Transaction")