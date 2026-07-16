from utils.groq_client import generate_response

prompt = """
Write a professional summary for a B.Tech Artificial Intelligence and Data Science student
who knows Python, Java, SQL, Machine Learning and is looking for internships.
"""

response = generate_response(prompt)

print(response)