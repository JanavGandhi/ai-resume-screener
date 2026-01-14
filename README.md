# 🧠 AI Resume Screener
Full-Stack, Explainable Machine Learning System

An AI-powered resume screening platform that semantically matches resumes to job descriptions using modern NLP techniques.
Built as a full-stack application with a React frontend and FastAPI backend, designed with explainability and production readiness in mind.

## 🚀 Features
### 📄 Resume Upload

Upload resumes in PDF format

### 📝 Job Description Input

Paste job descriptions directly into the UI

### 📊 Relevance Scoring

TF-IDF — lexical similarity baseline

Sentence-BERT — semantic similarity matching

### 🔍 Explainable AI Outputs

Common skill overlap between resume and JD

Top matching resume sentences with relevance scores

### 🌐 Full-Stack Architecture

React (Vite) frontend

FastAPI backend

### 🛡️ Production-Grade API

Multipart file handling

JSON-safe ML outputs

CORS-enabled for browser access

### 🧱 Tech Stack
#### Frontend

React (Vite)

JavaScript

HTML / CSS

#### Backend

FastAPI

Python 3

pdfplumber

scikit-learn

### 🏗️ System Architecture
React Frontend (localhost:5173)
        |
        |  multipart/form-data
        |
FastAPI Backend (localhost:8000)
        |
        |  NLP + ML Pipeline
        |
TF-IDF + Sentence-BERT + Explainability

### 🧠 How It Works

User uploads a resume and provides a job description

Resume text is extracted and cleaned

Resume is split into skills and experience sections

Similarity is computed using:

TF-IDF for keyword overlap

Sentence-BERT for semantic relevance

Explainability layer:

Extracts overlapping skills

Identifies top matching resume sentences

Results are returned via API and rendered in the UI

sentence-transformers

NLTK
