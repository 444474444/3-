import streamlit as st
if 'counter' not in st.session_state:
    st.session_state.counter=1
    st.session_state.count = 1


increment = st.button("1원씩 증가하는 버튼")

if increment:
    st.session_state.counter+=1
   
   
    st.write('counter=',st.session_state.counter)
    st.write('count=',st.session_state.count)