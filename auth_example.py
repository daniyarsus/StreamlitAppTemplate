import json
import streamlit as st
import jwt
import datetime

SECRET_KEY = "your_secret_key"


def generate_jwt(username: str) -> str:
    payload = {
        "username": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token


def verify_jwt(token: str) -> bool:
    try:
        jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return True
    except jwt.ExpiredSignatureError:
        st.error("Session expired. Please log in again.")
        return False
    except jwt.InvalidTokenError:
        st.error("Invalid token. Please log in again.")
        return False


def login() -> None:
    st.title("Login")
    username = st.text_input(label="Username")
    password = st.text_input(label="Password", type="password")

    if st.button(label="Login"):
        if username == "admin" and password == "admin":
            token = generate_jwt(username)
            st.session_state["jwt_token"] = token
            st.session_state["authenticated"] = True
            st.success("Logged in successfully")
            st.rerun()
        else:
            st.error("Invalid username or password")


def render_main_page() -> None:
    st.title("Main Page")
    st.write("Welcome to the main page!")
    st.session_state["authenticated"] = True
    if st.button("Logout"):
        st.session_state.pop("jwt_token", None)
        st.session_state["authenticated"] = False
        st.rerun()


def main() -> None:
    if "jwt_token" in st.session_state:
        if verify_jwt(st.session_state["jwt_token"]):
            print("JWT is here")
            st.session_state["authenticated"] = True
        else:
            st.session_state["authenticated"] = False
            st.session_state.pop("jwt_token", None)
    else:
        st.session_state["authenticated"] = False

    if st.session_state["authenticated"]:
        render_main_page()
        print("User is authenticated")
    else:
        login()


if __name__ == '__main__':
    main()
