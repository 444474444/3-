import streamlit as st
import ollama



def init_session_state(keys: dict):
    for key,value in keys.items():
        if key not in st.session_state:
            st.session_state[key]=value
            
def chat_message_user(prompt:str) ->dict:
  with st.chat_message("user"):
     st.markdown(prompt)
    return dict(role="user",content=prompt)

def chat_message_llm(role:str,model:str, messages:list)->dict
  
  with st.chat_message(role):
    with st.spinner("적당히해라 유동성")
       print(role,model,messages)
       response=ollama.chat(model=model,messages=messages)
       msg_llm=response.get("messages,{}")
       st.markdown(msg_llm("content"))
  return msg_llm
if  __name__==  '__main__':
    st.set_page_config(layout='wide')
    st.title("사랑한다 하츠투하츠🌼")

    init_session_state(dict(msgs=[]))
    msgs=st.session_state['msgs']

    for row in msgs:
    with st.chat_message(row["role"]):
            st.markdown(row["content"])

    if prompt : =st.chat_input("여기에 대화를 입력하세요"):
        msgs_user=chat_message_user(prompt)
        msgs.append(msg_user)

        msg_llm =chat_message_llm("assistant","gemma2:9b",msgs)
        msgs.append(msg_llm)