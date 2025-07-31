import streamlit as st

with st.chat_message("user"):
    st.write("Hello 🐦 ")
prompt=st.chat_input("궁금한게 있으면 물어봐")
