import streamlit as st

st.markdown('<div style="text-align: center; margin-bottom: -30px;"><h1>Code Mix Text Translation!</h1></div>', unsafe_allow_html=True)

st.markdown(
    '<div style="text-align: center; margin-bottom: 50px;"><h3 style="font-size:18px;">Translate code-mixed Marathi into pure English for improved clarity and understanding</h3></div>',
    unsafe_allow_html=True
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    if msg['role'] == 'user':
        st.markdown(
            f'''
            <div style="text-align: right; margin-bottom: 20px;">
                <div style="background-color: #26272D; color: white; border-radius: 5px; padding: 5px 14px; max-width: 70%; width: fit-content; overflow-wrap: break-word; display: inline-block; text-align: left;">
                    {msg["content"]}
                </div>
            </div>
            ''',
            unsafe_allow_html=True
        )
    else:
        col1, col2 = st.columns([1, 20])
        with col1:
            st.image("emoji.png", width=25)
        with col2:
            st.markdown(
                f'<div style="text-align: left; margin-bottom: 20px; max-width: 70%; width: fit-content; overflow-wrap: break-word;">{msg["content"]}</div>',
                unsafe_allow_html=True
            )

if prompt := st.chat_input("Translate your message.."):
    st.session_state.messages.append({'role': 'user', 'content': prompt})

    st.markdown(
        f'''
        <div style="text-align: right; margin-bottom: 20px;">
            <div style="background-color: #26272D; color: white; border-radius: 5px; padding: 5px 14px; max-width: 70%; width: fit-content; overflow-wrap: break-word; display: inline-block; text-align: left;">
                {prompt}
            </div>
        </div>
        ''',
        unsafe_allow_html=True
    )

    response = prompt

    col1, col2 = st.columns([1, 20])
    with col1:
        st.image("emoji.png", width=25)
    with col2:
        st.markdown(
            f'<div style="text-align: left; margin-bottom: 20px; max-width: 70%; width: fit-content; overflow-wrap: break-word;">{response}</div>',
            unsafe_allow_html=True
        )

    st.session_state.messages.append({'role': 'assistant', 'content': response})
