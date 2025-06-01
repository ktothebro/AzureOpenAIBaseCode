from openai import OpenAI
from config import API_KEY, ENDPOINT

# Create a client using your Azure OpenAI endpoint
client = OpenAI(
    api_key=API_KEY,
    base_url=ENDPOINT
)

def classify_ticket(text):
    response = client.chat.completions.create(
        model="gpt-4o",  # 👈 Replace with your Azure *deployment name*, not model name
        messages=[
            {"role": "system", "content": "Classify the IT support issue."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content.strip()
