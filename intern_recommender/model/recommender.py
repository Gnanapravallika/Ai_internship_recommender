import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_data():
    students = pd.read_csv("data/student_profiles.csv")
    domains = pd.read_csv("data/internship_domains.csv")
    return students, domains


def recommend_domains(student_name, students, domains, top_k=3):
    # Merge student's data into one text
    students['profile'] = students[['skills', 'interests', 'past_experience']].fillna('').agg(' '.join, axis=1)
    
    # Vectorize both student profile and internship domains
    tfidf = TfidfVectorizer()
    student_vecs = tfidf.fit_transform(students['profile'])
    domain_vecs = tfidf.transform(domains['keywords'])
    
    # Find index of selected student
    idx = students[students['name'] == student_name].index[0]
    student_vector = student_vecs[idx]

    # Compute similarity
    similarities = cosine_similarity(student_vector, domain_vecs).flatten()
    top_matches = similarities.argsort()[::-1][:top_k]
    
    return domains.iloc[top_matches][['domain', 'keywords']]
