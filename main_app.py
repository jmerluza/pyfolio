import streamlit as st
import streamlit.components.v1 as components
from streamlit_timeline import timeline
from streamlit_lottie import st_lottie
from contents import (
    git_lottie,
    jira_lottie,
    files_lottie,
    mysql_lottie,
    github_lottie,
    python_lottie,
    gradient_lottie,
    fullname,
    intro_header,
    about_me,
    job_company1,
    job_company2,
    job_desc1,
    job_desc2,
    job_timeline1,
    job_timeline2,
    job_title1,
    job_title2,
    career_timeline,
    linkedin_html,
    linkedin_js,
    sidebar_contents
)

st.set_page_config(page_title=f"{fullname}'s Portfolio", layout="centered", page_icon=":page_with_curl:")

linkedin_badge = f"{linkedin_js} {linkedin_html}"

# with st.sidebar:
    # components.html(html=linkedin_badge, height=310)
#     st.markdown(sidebar_contents)

top_col1, top_col2 = st.columns(spec=[0.4,0.6], vertical_alignment="top")
with top_col1:
    components.html(html=linkedin_badge, height=310)
    # st.header(intro_header)
    
with top_col2:
    st.markdown(sidebar_contents)
    # st_lottie(gradient_lottie, height=400)

st.markdown(about_me)

st.header(":pushpin: Career Highlights")
work_experience_col1, work_experience_col2 = st.columns(2)
with work_experience_col1:
    with st.container(border=True, height=300):
        st.markdown(f"#### *_{job_title1}_*")
        st.markdown(f"**{job_company1}**")
        st.markdown(f"**{job_timeline1}**")
        st.markdown(job_desc1)

with work_experience_col2:
    with st.container(border=True, height=300):
        st.markdown(f"#### *_{job_title2}_*")
        st.markdown(f"**{job_company2}**")
        st.markdown(f"**{job_timeline2}**")
        st.markdown(job_desc2)

with st.container():
    st.subheader("Timeline")
    st.write("*A Streamlit Timeline component by integrating TimelineJS from Knightlab*")
    timeline(career_timeline, height=400)



with st.container():
    st.header(":toolbox: Skills")
    skills_col1, skills_col2, skills_col3, skills_col4 = st.columns(4)
    with skills_col1:
        st_lottie(python_lottie, height=100)
        st_lottie(jira_lottie, height=100)
    with skills_col2:
        st_lottie(git_lottie, height=100)
        st_lottie(mysql_lottie, height=100)

    with skills_col3:
        st_lottie(github_lottie, height=100)

    with skills_col4:
        st_lottie(files_lottie, height=100)