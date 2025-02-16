import json
from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)

system_prompt = """
"You are a JSON generator. Respond **ONLY** with valid JSON using this schema: {\"data\": {\"answer\": \"...\", \"key_points\": [], \"references\": []}}"
"""

user_prompt = "Explain photosynthesis in 3 key points"

messages = [{"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}]

response = client.chat.completions.create(
    model="deepseek/deepseek-r1:free",
    messages=messages,
    response_format={
        'type': 'json_object'
    }
)

response_content = response.choices[0].message.content

if not response_content:
    print("The response is empty. Let's check why.")
else:
    print("Raw response:", response_content)
    try:
        data = json.loads(response_content)
        print("Decoded JSON:", data)
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)

