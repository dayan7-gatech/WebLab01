import streamlit as st
import info
import pandas as pd

#About me
def about_me():
    st.header("About Me")
    st.image(info.profile_picture, width= 200)
    st.write(info.about_me)
    st.write("---")

about_me()

#Links
def links_section():
    st.sidebar.header("Links")
    
    st.sidebar.text("Check out my GitHub")
    github_link = f' <a href="{info.my_github_url}"><img src="{info.github_image_url}" alt="GitHub" width="75" height="75"></a>'
    st.sidebar.markdown(github_link, unsafe_allow_html=True)
    
    st.sidebar.text("Connect with me on LinkedIn")
    linkedin_link = f'<a href="{info.my_linkedin_url}"><img src="{info.linkedin_image_url}" alt="LinkedIn" width="75" height="75"></a>'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)
    
    st.sidebar.text("Send me an email")
    email_link = f'<a href="mailto:{info.my_email_address}"><img src="{info.email_image_url}" alt="Email" width="75" height="75"></a>'
    st.sidebar.markdown(email_link, unsafe_allow_html=True)
    
links_section()

#Education
def education_section(education_data, course_data):
    st.header("Education")
    
    st.subheader(info.education_data["Institution"])
    st.write("Degree:", info.education_data["Degree"])
    st.write("Graduation Date:", info.education_data["Graduation Date"])
    st.write("GPA:", info.education_data["GPA"])
    
    st.subheader("Coursework")
    coursework = pd.DataFrame(course_data)
    st.dataframe(coursework, hide_index=True)
    
    st.write("---")
    
education_section(info.education_data, info.course_data)

# Professional Experience
def experience_section(experience_data):
    st.header("Professional Experience")
    
    for job_title, (job_description, image) in experience_data.items():
        expander = st.expander(job_title)
        expander.image(image, width=250)
        
        for bullet in job_description:
            expander.write(bullet)
            
experience_section(info.experience_data)

#Projects
def projects_section(projects_data):
    st.header("Projects")
    
    for project_name, project_description in projects_data.items():
        expander = st.expander(project_name)
        expander.write(project_description)
        
    st.subheader("Interactive Algebra Quiz")
    st.write("I created an interactive algebra quiz using Streamlit! Test your algebra knowledge!")
    
    st.link_button(
        "Take My Algebra Quiz",
        "https://cs1301algebraquiz-vh7rjanckrzuy7mtvcjggu.streamlit.app"
    )
        
projects_section(info.projects_data)

#Skills
def skills_section(programming_data, spoken_data):
    st.header("Skills")
    
    st.subheader("Programming Languages")
    
    for skill, percentage in programming_data.items():
        st.write(skill)
        st.progress(percentage)
        
    st.subheader("Spoken Languages")
    
    for language, fluency in spoken_data.items():
        st.write(language, ":", fluency)
        
skills_section(info.programming_data, info.spoken_data)

#Activities
def activities_section(leadership_data, activity_data):
    st.header("Activities")
    
    tab1, tab2 = st.tabs(["Leadership", "Community Service"])
    
    with tab1:
        for title, (details,image) in leadership_data.items():
            expander =st.expander(title)
            expander.image(image, width=250)
            
            for bullet in details:
                expander.write(bullet)
                
    with tab2:
        for title, details in activity_data.items():
            expander = st.expander(title)
            
            for bullet in details:
                expander.write(bullet)
                
activities_section(info.leadership_data, info.activity_data)



