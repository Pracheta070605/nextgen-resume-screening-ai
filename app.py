import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
import google.generativeai as genai
from utils import clean_text, extract_resume_text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -------------------------------------
# Load Environment Variables
# -------------------------------------
load_dotenv()

# -------------------------------------
# Gemini API Setup
# -------------------------------------
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(
    api_key=GEMINI_API_KEY
)

model = genai.GenerativeModel(
    "models/gemini-2.5-flash"
)

# -------------------------------------
# Streamlit Page Setup
# -------------------------------------
st.set_page_config(
    page_title="Next-Gen Resume Screening System",
    layout="wide"
)

st.title(
    "Next-Gen Resume Screening and Automated Interview Preparation System"
)

st.write("Upload your resume and get:")
st.write("✔ Top job matches")
st.write("✔ Missing skills")
st.write("✔ AI-generated interview questions")

# -------------------------------------
# Load Job Dataset
# -------------------------------------
jobs = pd.read_csv("postings_sample.csv")

jobs["description"] = jobs["description"].fillna("")
jobs["title"] = jobs["title"].fillna("Unknown Role")

jobs["cleaned_description"] = jobs["description"].apply(
    clean_text
)

# -------------------------------------
# Upload Resume
# -------------------------------------
uploaded_resume = st.file_uploader(
    "Upload Resume (PDF only)",
    type=["pdf"]
)

if uploaded_resume:

    # Extract resume text
    resume_text = extract_resume_text(
        uploaded_resume
    )

    cleaned_resume = clean_text(
        resume_text
    )

    # Success message
    st.success(
        "Resume uploaded and analyzed successfully."
    )

    # -------------------------------------
    # TF-IDF Vectorization
    # -------------------------------------
    vectorizer = TfidfVectorizer()

    job_vectors = vectorizer.fit_transform(
        jobs["cleaned_description"]
    )

    resume_vector = vectorizer.transform(
        [cleaned_resume]
    )

    # -------------------------------------
    # Similarity Calculation
    # -------------------------------------
    similarity_scores = cosine_similarity(
        resume_vector,
        job_vectors
    )[0]

    jobs["similarity_score"] = similarity_scores

    top_matches = jobs.sort_values(
        by="similarity_score",
        ascending=False
    ).head(5)

    # -------------------------------------
    # Top Job Matches
    # -------------------------------------
    st.subheader(
        "Top Matching Jobs"
    )

    st.dataframe(
        top_matches[
            ["title", "similarity_score"]
        ]
    )

    # -------------------------------------
    # Skill Gap Analysis
    # -------------------------------------
    best_match = top_matches.iloc[0]

    resume_skills = set(
        cleaned_resume.split()
    )

    job_skills = set(
        best_match[
            "cleaned_description"
        ].split()
    )

    missing_skills = job_skills - resume_skills

    st.subheader(
        "Missing Skills"
    )

    if missing_skills:
        st.write(
            list(missing_skills)[:10]
        )
    else:
        st.success(
            "No missing skills detected."
        )

    # -------------------------------------
    # Interview Question Generation
    # -------------------------------------
    if missing_skills:

        prompt = f"""
Generate 5 technical interview questions for the role:
{best_match['title']}

Focus on these missing skills:
{', '.join(list(missing_skills)[:5])}

Make them practical and intermediate level.
Only return the questions in numbered format.
"""

        with st.spinner(
            "Generating Interview Questions..."
        ):

            response = model.generate_content(
                prompt
            )

            generated_text = response.text

        st.subheader(
            "Generated Interview Questions"
        )

        st.write(
            generated_text
        )