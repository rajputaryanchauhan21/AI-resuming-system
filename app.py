import streamlit as st
import pandas as pd
from src.text_extraction import extract_text
from src.preprocessing import clean_text
from src.skill_extraction import extract_skills
from src.ranking import rank_resumes
from src.matching import calculate_match

# Page configuration
st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)

# Header
st.title("📄 AI Resume Screening System")
st.markdown("Smart Resume Analysis & Candidate Matching")
st.caption("dveloped by ARYAN CHAUHAN")
# Sidebar
st.sidebar.header("Settings")

job_role = st.sidebar.selectbox(
    "Select Job Role",
    ["Software Developer", "Data Scientist", "Web Developer", "Custom"]
)

match_threshold = st.sidebar.slider(
    "Match Threshold (%)",
    min_value=0,
    max_value=100,
    value=50
)

st.sidebar.markdown("---")
st.sidebar.info("Upload resumes and compare with job description.")

# Main Layout
col1, col2 = st.columns(2)

# Left Column → Resume Upload
with col1:
    st.subheader("📑 Upload Resumes")

    uploaded_resumes = st.file_uploader(
        "Upload Resume Files",
        type=["pdf", "docx"],
        accept_multiple_files=True
    )

    if uploaded_resumes:
        st.success(f"{len(uploaded_resumes)} resume(s) uploaded ✅")

# Right Column → Job Description
with col2:
    st.subheader("📝 Job Description")

    job_description = st.text_area(
        "Paste Job Description Here",
        height=200,
        placeholder="Enter job requirements, skills, experience..."
    )

# Divider
st.markdown("---")

# Action Buttons
col3, col4, col5 = st.columns([1, 1, 2])

with col3:
    analyze_btn = st.button("🔍 Analyze Resumes")

with col4:
    clear_btn = st.button("🗑 Clear")

# Placeholder Results Section
st.subheader("📊 Results")

if analyze_btn:
    if not uploaded_resumes:
        st.warning("Please upload at least one resume.")
    elif not job_description.strip():
        st.warning("Please enter a job description.")
    else:
        st.success("Analysis Started ✅")

        jd_clean = clean_text(job_description)
        jd_skills = extract_skills(jd_clean, job_role)

        results = []

        for resume in uploaded_resumes:
            resume_text = extract_text(resume, resume.name)
            resume_clean = clean_text(resume_text)
            resume_skills = extract_skills(resume_clean, job_role)

            matched_skills, missing_skills, score = calculate_match(resume_skills, jd_skills)

            results.append({
                "name": resume.name,
                "matched": matched_skills,
                "missing": missing_skills,
                "score": score
            })

        ranked_results = rank_resumes(results)

        table_data = []

        for r in ranked_results:
            table_data.append({
                  "Rank": r["rank"],  # ✅ FIRST COLUMN
                 "Candidate Name": r["name"],  # ✅ SECOND COLUMN
                 "Matched Skills": ", ".join(r["matched"]),
                 "Missing Skills": ", ".join(r["missing"]),
                 "Match Score (%)": r["score"],
                 "Status": "Good Match" if r["score"] >= match_threshold else "Low Match"
             })

        df = pd.DataFrame(table_data)

        st.dataframe(df, use_container_width=True)

        excel_file = "screening_results.xlsx"
        df.to_excel(excel_file, index=False)

        with open(excel_file, "rb") as f:
            st.download_button(
                label="📥 Download Results in Excel",
                data=f,
                file_name=excel_file,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
   

if clear_btn:
    st.experimental_rerun()

st.markdown("---")

st.markdown(
    """
    <div style='text-align: center; font-size: 16px;'>
        🚀 <b>AI Resume Screening Tool</b><br>
        Developed by <b>चौहान साहब</b>
    </div>
    """,
    unsafe_allow_html=True
)



