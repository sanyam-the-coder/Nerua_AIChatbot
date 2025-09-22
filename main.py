import os
from openai import OpenAI

client = OpenAI(api_key="Insert your API key")

def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Exiting the chat. Goodbye!")
            break

        response = chat_with_gpt(user_input)

        print("NERUA:", response)
