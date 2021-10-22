import hashlib
import mysql.connector
import streamlit as st
import ex
from apps import a


def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()


def check_hashes(password, hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False


mydb = mysql.connector.connect(host='localhost', user='root', password='Zebronics1!', port='3306',
                               database='pythonpoc')
c = mydb.cursor()
# k = 0.1
# string1 = ""


def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')
    mydb.commit()


def add_userdata(username, password):
    c.execute('INSERT INTO userstable(username,password) VALUES (%s,%s)', (username, password))
    mydb.commit()


def login_user(username, password):
    c.execute('SELECT * FROM userstable WHERE username = %s AND password =  %s', (username, password))
    data = c.fetchall()
    return data


def view_all_users():
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data


def main():
    """Simple Login App"""
    menu = ["Home", "Login", "SignUp", "Logout"]
    coice = st.sidebar.selectbox("Login Menu", menu)
    if coice == "Home":
        st.subheader("Home")
    elif coice == "Login":
        st.subheader("Login Section")
        # st.write(k)
        if ex.q == 0:
            username = st.sidebar.text_input("User Name")
            password = st.sidebar.text_input("Password", type='password')
            if st.sidebar.button("Login"):
                create_usertable()
                hashed_pswd = make_hashes(password)
                result = login_user(username, check_hashes(password, hashed_pswd))
                if result:
                    ex.q = 1
                    a.st1 = username
                    st.success("Logged In as {}".format(username))
                else:
                    st.warning("Incorrect Username/Password")
        else:
            st.warning("Already logged in as {}. Please logout to login as different user.".format(a.st1))
    elif coice == "SignUp":
        if ex.q == 0:
            st.subheader("Create New Account")
            new_user = st.text_input("Username", key='1')
            new_password = st.text_input("Password", type='password', key='2')
            if st.button("Signup"):
                create_usertable()
                add_userdata(new_user, make_hashes(new_password))
                st.success("You have successfully created a valid Account")
                st.info("Go to Login Menu to login")
        else:
            st.warning("Logout to Sign up")
    elif coice == "Logout":
        ex.q = 0
        st.success("{} Logged Out ".format(a.st1))
        # st.subheader("Logged out")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
