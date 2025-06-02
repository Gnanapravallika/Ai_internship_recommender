# test.py
from recommender import load_data, recommend_domains

students, domains = load_data()
student_name = "Alice"
recommendations = recommend_domains(student_name, students, domains)

print(f"\nTop internship domain recommendations for {student_name}:\n")
print(recommendations)
