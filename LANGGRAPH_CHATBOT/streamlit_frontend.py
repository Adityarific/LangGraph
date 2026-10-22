import streamlit as st

if 'message_history' not in st.session_state:
     st.session_state['message_history'] = []


user_input = st.chat_input('Ask Anything...')
for message in st.session_state['message_history']:
     with st.chat_message(message['role']):
        st.markdown(message['content'])


if user_input:
        #first add thr message to message_history
        st.session_state['message_history'].append({'role':'user' , 'content':user_input})
        with st.chat_message("user"):
            st.markdown(user_input)
        #first add thr message to message_history
        st.session_state['message_history'].append({'role':'assistant' , 'content':user_input})
        with st.chat_message("assistant"):
            st.markdown(user_input)