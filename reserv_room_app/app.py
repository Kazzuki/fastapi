import streamlit as st
import random
import requests
import json

page = st.sidebar.selectbox(
    "which page do you want to see users,rooms and bookings",
    ("users", "rooms", "bookings")
)

if page == "users":
    st.title('APIテスト画面（ユーザ）')
    with st.form(key='user'):
        user_id: int = random.randint(0, 10)
        user_name: str = st.text_input('ユーザ名', max_chars=12)
        data = {
            "user_id" : user_id,
            "user_name" : user_name
        }
        # form_submit_buttonは、formに紐づくもの
        submit_button = st.form_submit_button(label="リクエスト送信")
    if submit_button:
        st.write("## 送信データ")
        st.json(data)
        st.write("## レスポンス結果")
        url = 'http://127.0.0.1:8000/users'
        res = requests.post(
            url,
            data=json.dumps(data)
        )
        st.write(res.status_code)
        st.json(res.json())

elif page == "rooms":
    st.title('APIテスト画面(会議室）')
    with st.form(key='room'):
        room_id: int = random.randint(0, 10)
        room_name: str = st.text_input('会議室名', max_chars=12)
        capacity: int = st.number_input('収容人数', step=1)
        data = {
            "room_id" : room_id,
            "room_name" : room_name,
            "capacity" : capacity
        }
        # form_submit_buttonは、formに紐づくもの
        submit_button = st.form_submit_button(label="リクエスト送信")

    if submit_button:
        st.write("## 送信データ")
        st.json(data)
        st.write("## レスポンス結果")
        url = 'http://127.0.0.1:8000/rooms'
        res = requests.post(
            url,
            data=json.dumps(data)
        )
        st.write(res.status_code)
        st.json(res.json())
elif page == "bookings":
    st.title('APIテスト画面（予約）')

    with st.form(key='user'):
        user_id: int = random.randint(0, 10)
        user_name: str = st.text_input('ユーザ名', max_chars=12)
        data = {
            "user_id" : user_id,
            "user_name" : user_name
        }
        # form_submit_buttonは、formに紐づくもの
        submit_button = st.form_submit_button(label="リクエスト送信")

    if submit_button:
        st.write("## 送信データ")
        st.json(data)
        st.write("## レスポンス結果")
        url = 'http://127.0.0.1:8000/users'
        res = requests.post(
            url,
            data=json.dumps(data)
        )
        st.write(res.status_code)
        st.json(res.json())