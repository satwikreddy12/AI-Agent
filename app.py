import streamlit as st
import openai
from openai import OpenAIError

# Set your OpenAI API key
openai.api_key = "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"  # OpenAI API key

# Add context for resume and role understanding
RESUME_CONTEXT = """
Satwik Reddy Ala is a skilled Data Analyst with expertise in AI/ML, data pipelines, and learning engineering.
He has a strong academic background with a Master's in Professional Data Science (GPA: 4.0) from the University of Maryland Baltimore County and a Bachelor's in Computer Science (GPA: 3.46) from JNTUH, Hyderabad, India.

Work Experience:
1. Programmer Analyst, Cognizant Technology Solutions (Sep 2023 - Aug 2024):
   - Refined application development workflows, ensuring accuracy in data lineage and processing.
   - Transformed BTEQ scripts into PySpark using Azure Databricks, enhancing scalability.
   - Delivered end-to-end data pipelines for QA validation, aligning solutions with business objectives.

2. Math Tutor, Baltimore Public Schools (Sept 2024 - Present):
   - Tutored elementary school students in mathematics, focusing on building foundational skills and confidence.
   - Designed personalized learning plans to meet the diverse needs of students.
   - Collaborated with educators to identify and address students' learning gaps.

3. Internship, Cognizant Technology Solutions (March 2022 - Aug 2022):
   - Set up Azure Blob Storage and SQL databases with secure configurations.
   - Developed a Python project to query databases, calculate demographics, and generate insights.
   - Monitored cost-effective Azure virtual machines and performed usage analyses.

4. Machine Learning Intern, Brainovision Solutions (May 2020):
   - Preprocessed and analyzed datasets for ML models.
   - Developed and evaluated ML algorithms for improved accuracy.
   - Documented findings for effective team communication.

Projects:
1. Sentiment Analysis of Electric Vehicle Reviews:
   - Developed a platform for aspect-based sentiment analysis using GPT and BERT to classify and explain sentiments on EV features.
   - Focused on extracting insights about battery life, charging speed, and environmental impact from customer reviews.

2. Driver Drowsiness Detection System:
   - Implemented real-time monitoring to detect driver drowsiness using Python, OpenCV, and dlib.

3. Classification of Parkinson's Disease:
   - Built ensemble ML models to classify Parkinson's disease with optimized accuracy.

4. COVID-19 Case Prediction:
   - Developed and compared ML models to forecast COVID-19 trends, enabling actionable insights.
"""

ROLE_UNDERSTANDING = """
FutureMakers' Readyness platform aims to empower K-5 educators by:
- Helping them plan, prepare, and execute engaging hands-on projects.
- Aligning these projects with educational standards such as NGSS and CASEL.
- Building confidence among educators through AI-driven solutions.
As an AI Development Intern, responsibilities include:
- Refining AI agent interaction models based on educator needs.
- Creating features for data collection, generating preparation materials, and aligning projects with NGSS and CASEL standards.
- Incorporating learning engineering and adult learning strategies to optimize educator confidence.
- Designing intuitive interfaces and conducting user testing to refine features.
"""

HOW_YOU_FIT = """
Satwik Reddy Ala is an ideal fit for FutureMakers' Readyness project because:
1. **AI/ML Expertise**:
   - My experience with sentiment analysis and ML models aligns with the need for AI-driven tools that support educators.
   - Proficiency in Python, PySpark, and OpenAI's GPT models supports the development of scalable, AI-powered solutions.

2. **Educational Understanding**:
   - As a Math Tutor, I can understand the challenges educators face, enabling me to design user-centered features.

3. **Projects**:
   - My work on projects like "Sentiment Analysis of Electric Vehicle Reviews" showcases his ability to extract actionable insights and build intuitive tools.

4. **Problem-Solving**:
   - My professional experience in developing data pipelines and scalable workflows demonstrates his ability to deliver effective solutions for Readyness.
"""

# App Header
st.title("Satwik Reddy Ala - AI Development Intern Application")
st.subheader("Explore my qualifications, experience, and alignment with FutureMakers' goals.")

# Navigation Sidebar
menu = st.sidebar.radio(
    "Navigate to",
    [
        "Introduction",
        "Ask the AI Agent",
        "Education",
        "Technical Skills",
        "Experience",
        "Projects",
        "Role Alignment"
    ]
)

# Static Content Based on Menu Selection
if menu == "Introduction":
    st.write("### Introduction")
    st.write("""
    Hi! I'm **Satwik Reddy Ala**, a dedicated Data Analyst with expertise in AI/ML, data pipelines, and learning engineering.
    """)

elif menu == "Education":
    st.write("### Education")
    st.write("""
    - **Master's in Professional Data Science** (GPA: 4.0) - University of Maryland Baltimore County
    - **Bachelor's in Computer Science** (GPA: 3.46) - JNTUH, Hyderabad, India
    """)

elif menu == "Technical Skills":
    st.write("### Technical Skills")
    st.write("""
    - **Programming Languages:** Python, JavaScript, R, C, CSS
    - **Tools:** MongoDB, Tableau, Power BI, MySQL, Excel
    - **Libraries:** NumPy, Pandas, Hadoop
    - **Specializations:** ETL processes, Data Warehousing, Data Visualization
    """)

elif menu == "Experience":
    st.write("### Experience")
    st.write(RESUME_CONTEXT)

elif menu == "Projects":
    st.write("### Projects")
    st.write("""
    - **Sentiment Analysis of Electric Vehicle Reviews**:
      Developed a platform for aspect-based sentiment analysis using GPT and BERT to classify and explain sentiments on EV features.
    - **Driver Drowsiness Detection System**:
      Implemented real-time monitoring to detect driver drowsiness using Python, OpenCV, and dlib.
    - **Classification of Parkinson's Disease**:
      Built ensemble ML models to classify Parkinson's disease with optimized accuracy.
    - **COVID-19 Case Prediction**:
      Developed and compared ML models to forecast COVID-19 trends, enabling actionable insights.
    """)

elif menu == "Ask the AI Agent":
    st.write("### Ask the AI Agent")
    st.write("You can ask the AI agent questions about my qualifications, projects, understanding of the role, or how I fit the role.")
    
    # User Input
    user_query = st.text_input("Enter your question:")
    if st.button("Submit"):
        if user_query:
            try:
                # Generate AI Response
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are an assistant who answers questions based on the following resume, role understanding, and fit."},
                        {"role": "assistant", "content": RESUME_CONTEXT + ROLE_UNDERSTANDING + HOW_YOU_FIT},
                        {"role": "user", "content": user_query}
                    ],
                    max_tokens=300,
                    temperature=0.7
                )
                ai_response = response['choices'][0]['message']['content']
                st.write("**AI Agent's Response:**")
                st.write(ai_response)
            except OpenAIError as e:
                st.write(f"An error occurred: {e}")
        else:
            st.write("Please enter a question before submitting.")

elif menu == "Role Alignment":
    st.write("### How I Align with FutureMakers' Readyness Goals")
    st.write("Below is how my background, skills, and experience align with FutureMakers' goals for Readyness:")
    st.write("**Role Understanding:**")
    st.write(ROLE_UNDERSTANDING)
    st.write("**How I Fit the Role:**")
    st.write(HOW_YOU_FIT)

# Footer
st.sidebar.markdown("Created by **Satwik Reddy Ala**")
