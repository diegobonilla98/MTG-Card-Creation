import openai

# Replace "your_api_key_here" with your actual OpenAI API key
openai.api_key = 'your_api_key_here'


def query_gpt(prompt, model="gpt-3.5-turbo", max_tokens=256):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens,
        temperature=0.7
    )
    return response.choices[0].message['content'].strip()
