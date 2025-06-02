#  Internship Domain Recommender using AI

##  Project Overview

This project is an "AI-based recommendation system" that suggests the most suitable **internship domains** for students based on their:

- Skills
- Interests
- Past Experience

The system uses "Natural Language Processing (NLP)" and "cosine similarity" to match student profiles with relevant internship fields such as "Data Science, Web Development, AI Research", and more.

---

##  Features

-  Match students with internships using profile data
-  Uses TF-IDF vectorization and cosine similarity
-  Optional web interface with Streamlit
-  Data-driven, customizable, and beginner-friendly

---

## Project Structure

intern_recommender/
├── data/
│ ├── student_profiles.csv # Input student data
│ └── internship_domains.csv # Internship domain keywords
├── model/
│ └── recommender.py # Core recommendation logic
├── app.py # Streamlit web interface (optional)
├── test.py # Test script to try the model
├── requirements.txt # Dependencies list
└── README.md # This file

How It Works

1. Merge the student's `skills`, `interests`, and `experience` into one text block.
2. Convert profile and internship domain text into numerical vectors using `TfidfVectorizer`.
3. Calculate the **cosine similarity** between the student and each domain.
4. Return the top N most similar internship domains.

Install packages:
pip install -r requirements.txt

Run the Test Script:
python test.py

Run the Web App:
streamlit run app.py
