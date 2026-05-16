from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class AnalyzeRequest(BaseModel):
    state: str

@app.post("/analyze")
def analyze(data: AnalyzeRequest):

    prompt = f"""
    User state: {data.state}

    Give:
    - short nervous system analysis
    - calming recommendation
    - stress level

    Respond in JSON style.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You are AI Nervous System Assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return {
        "result": response.choices[0].message.content
    }
