import streamlit as st
from multipage import MultiPage
from apps import a, main
# import SessionState
# import random


app = MultiPage()
q = 0


def mai():
    st.title("Python POC")
    # session_state = SessionState.get(random_number=random.random())
    # st.write("This number should be unique for each browser tab:", session_state.random_number)
    # main.k = session_state.random_number
    app.add_page("login/logout", main.main)
    app.add_page("app", a.appn)
    app.run()


if __name__ == '__main__':
    mai()
