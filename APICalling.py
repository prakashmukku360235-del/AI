from openai import OpenAI
client=OpenAI(api_key="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")

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