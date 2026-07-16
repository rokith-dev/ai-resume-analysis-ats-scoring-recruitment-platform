import os

from dotenv import load_dotenv
from groq import Groq

# Load .env file
load_dotenv()

# Create Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_response(prompt):
    """
    Generate response using Groq Llama model.
    """

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "system",
                "content": "You are an expert Resume Writer and Career Coach."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.4,
        max_tokens=1024

    )

    return response.choices[0].message.content