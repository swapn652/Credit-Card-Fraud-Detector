import streamlit as st
import json
import requests as re

st.markdown("<h1 style='text-align: center;'>CREDIT CARD FRAUD DETECTOR</h1>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

st.image("image_real.jpg")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Input Information related to the Transaction</h2>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

sender_name = st.text_input("""Enter Sender's ID""")
receiver_name = st.text_input("""Enter Receiver ID""")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

step = st.slider("""Number of Hours it took for the Transaction to complete: """)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

types = st.subheader(f"""
                 Enter Type of Transfer Made:\n\n\n\n
                 0 for 'Cash In' Transaction\n 
                 1 for 'Cash Out' Transaction\n 
                 2 for 'Debit' Transaction\n
                 3 for 'Payment' Transaction\n  
                 4 for 'Transfer' Transaction\n""")
types = st.selectbox("Enter Type of Transfer Made:",(0,1,2,3,4))


x = ''
if types == 0:
    x = 'Cash in'
if types == 1:
    x = 'Cash Out'
if types == 2:
    x = 'Debit'
if types == 3:
    x = 'Payment'
if types == 4:
    x =  'Transfer'
    
st.markdown("<br>", unsafe_allow_html=True)
amount = st.number_input("Amount",min_value=0, max_value=110000)
st.markdown("<br>", unsafe_allow_html=True)
oldbalanceorg = st.number_input("""Old Balance of Sender: """,min_value=0, max_value=110000)
st.markdown("<br>", unsafe_allow_html=True)
newbalanceorg= st.number_input("""New Balance of Sender: """,min_value=0, max_value=110000)
st.markdown("<br>", unsafe_allow_html=True)
oldbalancedest= st.number_input("""Old Balance of Receiver: """,min_value=0, max_value=110000)
st.markdown("<br>", unsafe_allow_html=True)
newbalancedest= st.number_input("""New Balance of Receiver: """,min_value=0, max_value=110000)
st.markdown("<br>", unsafe_allow_html=True)
isflaggedfraud = st.selectbox("""Specify if this was flagged as Fraud: """,(0,1))


if st.button("Get Result"):
    values = {
    "step": step,
    "types": types,
    "amount": amount,
    "oldbalanceorig": oldbalanceorg,
    "newbalanceorig": newbalanceorg,
    "oldbalancedest": oldbalancedest,
    "newbalancedest": newbalancedest,
    "isflaggedfraud": isflaggedfraud
    }

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.write(f"""### TRANSACTION DETAILS: \n
    Sender ID: {sender_name}
    Receiver ID: {receiver_name}
    1. Number of Hours it took to complete: {step}\n
    2. Type of Transaction: {x}\n
    3. Amount Sent: {amount}\n
    4. Sender Previous Balance Before Transaction: {oldbalanceorg}\n
    5. Sender New Balance After Transaction: {newbalanceorg}\n
    6. Recepient Balance Before Transaction: {oldbalancedest}\n
    7. Recepient Balance After Transaction: {newbalancedest}\n
    8. System Flag Fraud Status: {isflaggedfraud}
                """)

    res = re.post(f"http://backend.docker:8000/predict/",json=values)
    json_str = json.dumps(res.json())
    resp = json.loads(json_str)
    
    if sender_name=='' or receiver_name == '':
        st.write("Error! Please input Transaction ID or Names of Sender and Receiver!")
    else:
        st.write(f"""### The '{x}' transaction that took place between {sender_name} and {receiver_name} is {resp[0]}.""")









