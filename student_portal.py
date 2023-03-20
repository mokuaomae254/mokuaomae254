import streamlit as st
import pandas as pd

# Function to retrieve student data from a database
def get_students():
    # Replace with code to query the database
    return pd.read_csv("students.csv")

# Create a sidebar with form fields for filtering the student data
st.sidebar.header("Filter Students")
name = st.sidebar.text_input("Name")
major = st.sidebar.selectbox("Major", ["Computer Science", "Math", "Physics"])

# Cache the student data to improve performance
@st.cache
def filter_students(name, major):
    students = get_students()
    if name:
        students = students[students["name"].str.contains(name, case=False)]
    if major:
        students = students[students["major"] == major]
    return students

# Display the filtered student data in a table
students = filter_students(name, major)
st.header("Students")
st.table(students)

# Add a button for exporting the student data to a CSV file
if st.button("Export to CSV"):
    csv = students.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # Encode as base64
    href = f'<a href="data:file/csv;base64,{b64}">Download CSV</a>'
    st.markdown(href, unsafe_allow_html=True)

#streamlit run student_portal.py