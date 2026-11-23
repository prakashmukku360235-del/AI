from openai import OpenAI
client=OpenAI(api_key="")

def call_llm(prompt):
    response = client.responses.create(
        model= "gpt-5.4-mini",
        input=user_input
    )
    return response.output_text

user_input= input ("Enter user instruction:")
print("## USER INPUT ##\n")
print(user_input)
result = call_llm(user_input)
print("## AI RESPONSE ##\n")
print(result)