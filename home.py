import streamlit as st

import firebase


def login():
    email = st.empty()
    email = email.text_input("Email アドレスを入力してください")
    password = st.text_input("パスワードを入力してください", type="password")
    submit = st.button("ログイン")
    if submit and firebase.authenticate(email, password):
        st.experimental_rerun()


def index():
    if not firebase.refresh():
        st.experimental_rerun()
        return
    st.text("ログインしました")


if "user" not in st.session_state:
    login()
else:
    index()
