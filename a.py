import streamlit as st
import mysql.connector
import ex

mydb = mysql.connector.connect(host='localhost', user='root', password='Zebronics1!', port='3306',
                               database='pythonpoc')
c = mydb.cursor()
st1 = "none"


def display():
    c.execute('select * from `accounts`;')
    data = c.fetchall()
    return data


def display2():
    st.write('adb')
    c.execute('select * from accounts;')
    data = c.fetchall()
    return data


def appn():
    if ex.q == 1:
        st.success("Logged In as {}".format(st1))
        menu1 = ["display", "display2"]
        coice = st.sidebar.selectbox("App Menu", menu1)
        if coice == "display":
            st.subheader("display")
            d = display()
            st.write(d)
        elif coice == "display2":
            st.subheader("display2")
            d = display2()
            st.write(d)
    else:
        st.warning("Login Please!")
