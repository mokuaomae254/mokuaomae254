import streamlit as st

# CV section title
st.title("Computer Science Developer CV")

# Personal information
st.subheader("Personal Information")
name = st.text_input("Full Name")
email = st.text_input("Email Address")
phone = st.text_input("Phone Number")
location = st.text_input("Location")
linkedin = st.text_input("LinkedIn Profile Link")
github = st.text_input("Github Profile Link")

# Education
st.subheader("Education")
degree = st.text_input("Degree")
major = st.text_input("Major")
school = st.text_input("School")
graduation_year = st.text_input("Graduation Year")
gpa = st.text_input("GPA")

# Work Experience
st.subheader("Work Experience")
job_title = st.text_input("Job Title")
company = st.text_input("Company")
start_date = st.text_input("Start Date")
end_date = st.text_input("End Date")
job_description = st.text_area("Job Description")

# Skills
st.subheader("Skills")
skills = st.text_area("Enter your skills, separated by commas")

# Certifications
st.subheader("Certifications")
certifications = st.text_area("Enter your certifications, separated by commas")

# Projects
st.subheader("Projects")
project_name = st.text_input("Project Name")
project_description = st.text_area("Project Description")
project_link = st.text_input("Project Link")

# Awards
st.subheader("Awards")
award_name = st.text_input("Award Name")
award_description = st.text_area("Award Description")

# Submit button
if st.button("Submit"):
    result = f"Name: {name} \nEmail: {email} \nPhone: {phone} \nLocation: {location} \nLinkedIn: {linkedin} \nGithub: {github} \n\nEducation: \nDegree: {degree} \nMajor: {major} \nSchool: {school} \nGraduation Year: {graduation_year} \nGPA: {gpa} \n\nWork Experience: \nJob Title: {job_title} \nCompany: {company} \nStart Date: {start_date} \nEnd Date: {end_date} \nJob Description: {job_description} \n\nSkills: {skills} \n\nCertifications: {certifications} \n\nProjects: \nName: {project_name} \nDescription: {project_description} \nLink: {project_link} \n\nAwards: \nName: {award_name} \nDescription: {award_description}"
    st.success(result)

import streamlit as st

# CV section title
st.title("Computer Science Developer CV")

# Personal information
st.subheader("Personal Information")
name = st.text_input("Full Name")
email = st.text_input("Email Address")
phone = st.text_input("Phone Number")
location = st.text_input("Location")

# Education
st.subheader("Education")
degree = st.text_input("Degree")
school = st.text_input("School")
graduation_year = st.text_input("Graduation Year")

# Work Experience
st.subheader("Work Experience")
job_title = st.text_input("Job Title")
company = st.text_input("Company")
start_date = st.text_input("Start Date")
end_date = st.text_input("End Date")
job_description = st.text_area("Job Description")

# Skills
st.subheader("Skills")
skills = st.text_area("Enter your skills, separated by commas")

# Submit button
if st.button("Submit"):
    result = f"Name: {name} \nEmail: {email} \nPhone: {phone} \nLocation: {location} \n\nEducation: \nDegree: {degree} \nSchool: {school} \nGraduation Year: {graduation_year} \n\nWork Experience: \nJob Title: {job_title} \nCompany: {company} \nStart Date: {start_date} \nEnd Date: {end_date} \nJob Description: {job_description} \n\nSkills: {skills}"
    st.success(result)


#streamlit run cvs.py