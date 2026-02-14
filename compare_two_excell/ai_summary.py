from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_summary(added, deleted, modified):

    prompt = f"""
    You are a data audit assistant.

    Added records: {len(added)}
    Deleted records: {len(deleted)}
    Modified record groups: {len(modified)}

    Provide a professional audit summary in simple business language.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content
