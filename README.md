# 🚀 SHL AI Assessment Recommendation System

An AI-powered Assessment Recommendation API built using **FastAPI** that recommends the most relevant SHL assessments based on a user's job role, skills, or requirements.

This project was developed as part of the **SHL AI Intern Assignment**.

---

# 📌 Project Overview

The SHL AI Assessment Recommendation System helps recruiters and hiring managers quickly identify the most suitable SHL assessments for different job roles.

The API searches through a catalog of 377+ SHL assessments and returns the most relevant recommendations using a custom scoring algorithm.

---

# ✨ Features

- 🔍 AI-powered assessment recommendation
- ⚡ FastAPI backend
- 📊 Searches 377+ SHL assessments
- 🎯 Relevance-based ranking algorithm
- 🌐 REST API
- 📄 JSON-based assessment catalog
- 🏆 Returns Top 5 matching assessments
- 📈 Clean and scalable project structure

---

# 🛠 Tech Stack

- Python 3.13
- FastAPI
- Uvicorn
- Pydantic
- JSON
- Git & GitHub

---

# 📂 Project Structure

```
SHL_AI_Intern/
│
├── app.py
├── recommender.py
├── catalog.json
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/SHL_AI_Intern.git

cd SHL_AI_Intern
```

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
uvicorn app:app --reload
```

Application will start at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

# 📡 API Endpoints

## Health Check

```
GET /health
```

Response

```json
{
  "status": "ok",
  "items_loaded": 377
}
```

---

## Assessment Recommendation

```
POST /chat
```

Example Request

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Python Developer"
    }
  ]
}
```

Example Response

```json
{
  "reply": "I found 1 matching assessments.",
  "recommendations": [
    {
      "name": "Python (New)",
      "duration": "11 minutes",
      "remote": "yes",
      "adaptive": "no"
    }
  ],
  "end_of_conversation": false
}
```

---

# 🧠 Recommendation Algorithm

The recommendation engine ranks assessments using a custom scoring system.

Matching is performed on:

- Assessment Name
- Description
- Job Levels
- Assessment Keys

Results are sorted by score and the Top 5 assessments are returned.

---

# 📊 Current Dataset

- Total Assessments: **377**
- Data Format: JSON
- Source: SHL Product Catalog

---

# 🔮 Future Improvements

- Natural Language Processing (NLP)
- Semantic Search
- OpenAI LLM Integration
- Assessment Comparison
- Skill Extraction
- Filters (Duration, Remote, Adaptive)
- Deployment on Render

---

# 👨‍💻 Author

**Rajesh Lodhe**

BCA Student | Aspiring Data Analyst & Software Developer

Skills:

- Python
- FastAPI
- SQL
- Power BI
- Data Analysis
- Git & GitHub

---

# 📄 License

This project was developed for educational purposes as part of the SHL AI Internship Assignment.
