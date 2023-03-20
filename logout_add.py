import streamlit as st
import pandas as pd
import hashlib
import sqlite3 

# Security
def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password, hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False

# DB Management
conn = sqlite3.connect('data.db')
c = conn.cursor()

# DB Functions
def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')

def add_userdata(username,password):
    c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
    conn.commit()

def login_user(username,password):
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
    data = c.fetchall()
    return data

def view_all_users():
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data

def main():
    """Simple Login App"""
    st.set_page_config(page_title="Login App", page_icon=":guardsman:", layout="wide")

    st.title("Simple Login App")

    menu = ["Home","Login","SignUp","Logout","Reset Password"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.subheader("Home")

    elif choice == "Login":
        st.subheader("Login Section")

        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password",type='password')
        if st.sidebar.checkbox("Login"):
            create_usertable()
            hashed_pswd = make_hashes(password)

            result = login_user(username,check_hashes(password,hashed_pswd))
            if result:
                st.success("Logged In as {}".format(username))

                task = st.selectbox("Task",["Add Post","Analytics","Profiles"])
                if task == "Add Post":
                    st.subheader("Add Your Post")

                elif task == "Analytics":
                    st.subheader("Analytics")

                elif task == "Profiles":
                    st.subheader("User Profiles")
                    user_result = view_all_users()
                    clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
                    st.dataframe(clean_db)

                #logout_button = st.button("Logout")
                #if logout_button:
                   # st.sidebar.empty()
                    #st.warning("You have been logged out")

            else:
                st.warning("Incorrect Username/Password")
                
    elif choice == "Logout":
            st.subheader("Logout Section")
            logout_button = st.button("Logout")
            if logout_button:
                st.sidebar.empty()
                st.warning("You have been logged out")
    elif choice == "Reset Password":
            st.subheader("Reset Password")
            username = st.text_input("Username")
            old_password = st.text_input("Old Password", type='password')
            new_password = st.text_input("New Password", type='password')

            if st.button("Reset"):
                create_usertable()
                hashed_pswd = make_hashes(old_password)

                result = login_user(username, check_hashes(old_password, hashed_pswd))
                if result:
                    reset_password(username, new_password)

                else:
                    st.warning("Incorrect Username/Password")
    elif choice == "SignUp":
        st.subheader("Create New Account")
        new_user = st.text_input("Username")
        new_password = st.text_input("Password",type='password')

        if st.button("Signup"):
            create_usertable()
            add_userdata(new_user,make_hashes(new_password))
            st.success("You have successfully created a valid Account")
            st.info("Go to Login Menu to login")

if __name__ == '__main__':
    main()
#streamlit run logout_add.py