import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


class AIResumeGenerator:

    def __init__(self):

        self.model = "llama-3.3-70b-versatile"

    def generate(self, prompt):

        response = client.chat.completions.create(

            model=self.model,

            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an expert ATS Resume Writer. "
                        "Generate professional resumes using clear headings, "
                        "bullet points, and concise language."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.3,
            max_tokens=2048

        )

        return response.choices[0].message.content