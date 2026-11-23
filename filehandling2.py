#import library

from openai import OpenAI
client=OpenAI(API_Key="Auth_Key")

def call_llm(prompt):
    response = client.responses.create(
        model= "gpt-5.4-mini",
        input=user_input
    )
    return response.output_text