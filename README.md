# Next-Gen Resume Screening and Automated Interview Preparation System

## Overview

The **Next-Gen Resume Screening and Automated Interview Preparation System** is an AI-powered web application designed to automate the resume screening process and help candidates prepare for interviews.

The system compares uploaded resumes with job descriptions using **Natural Language Processing (NLP)** and **Machine Learning (ML)** techniques. It identifies the most suitable job matches, performs skill gap analysis, and generates technical interview questions using **Google Gemini API**.

This project aims to improve recruitment efficiency and provide candidates with personalized career guidance.

---

## Features

* **Resume Upload (PDF)**

  * Users can upload resumes in PDF format.

* **Resume Text Extraction**

  * Extracts and cleans resume text automatically.

* **Job Matching System**

  * Uses **TF-IDF Vectorization** and **Cosine Similarity** to match resumes with job descriptions.

* **Top 5 Job Recommendations**

  * Displays the most relevant job roles based on similarity scores.

* **Skill Gap Analysis**

  * Identifies missing skills by comparing candidate skills with job requirements.

* **AI Interview Question Generation**

  * Generates technical interview questions based on missing skills using **Google Gemini API**.

---

## Technologies Used

### Frontend

* Streamlit

### Backend

* Python

### Libraries

* Pandas
* Scikit-learn
* PyPDF2
* Regex
* python-dotenv
* Google Generative AI SDK

### AI & NLP

* TF-IDF Vectorization
* Cosine Similarity
* Google Gemini 2.5 Flash

---

## Project Structure

```text
resume_ai_project/
│── app.py                  # Main Streamlit application
│── utils.py                # Helper functions
│── postings_sample.csv     # Sample job dataset
│── requirements.txt        # Required dependencies
│── .gitignore              # Ignored files
│── .env                    # API key (not uploaded)
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/Pracheta070605/nextgen-resume-screening-ai.git
cd nextgen-resume-screening-ai
```

### Create virtual environment (optional)

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## API Key Setup

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

Get your API key from:

https://aistudio.google.com/

---

## Run the Project

```bash
streamlit run app.py
```

---

## Workflow

1. Upload resume in PDF format.
2. System extracts resume text.
3. Text is cleaned and preprocessed.
4. Resume is compared with job descriptions.
5. Top matching jobs are displayed.
6. Missing skills are identified.
7. AI generates interview questions.

---

## Sample Output

* Top Matching Jobs
* Similarity Scores
* Missing Skills
* Generated Interview Questions

---

## Future Improvements

* Resume ranking system
* Better skill extraction using Named Entity Recognition (NER)
* Job recommendation based on career goals
* Multi-language resume support
* Recruiter dashboard
* Resume scoring system

---

## Academic Purpose

This project was developed as part of an academic mini-project for demonstrating the use of:

* Natural Language Processing
* Machine Learning
* Generative AI
* Automated Recruitment Systems

---

## Author

**Pracheta Das**
B.Tech CSE Student
