import os
import sys
import streamlit as st

# Add current directory to Python path for Streamlit Cloud
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from langgraph_backend import chatbot



config = {"configurable": {"thread_id": "user-2"}}

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

        def stream_response():
            for chunk, metadata in chatbot.stream({'messages': [user_input]}, 
                config=config,
                stream_mode="messages"
            ):
                if chunk.content:
                    yield chunk.content


    # 3. Stream response live to the UI and store full text in session history ------> (st.write_stream is inbuilt in streamlit to make UI using genertor function)
        with st.chat_message("assistant"):
            full_response = st.write_stream(stream_response)

        st.session_state['message_history'].append({'role': 'assistant', 'content': full_response})