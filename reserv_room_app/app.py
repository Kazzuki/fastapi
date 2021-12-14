import streamlit as st
import random
import requests
import json

st.title('APIテスト画面（ユーザ）')

with st.form(key='user'):
    user_id: int = random.randint(0, 10)
    username: str = st.text_input('ユーザ名', max_chars=12)
    data = {
        "user_id" : user_id,
        "username" : username
    }
    # form_submit_buttonは、formに紐づくもの
    submit_button = st.form_submit_button(label="リクエスト送信")

if submit_button:
    st.write("## 送信データ")