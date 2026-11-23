#add library 
from urllib import response

import ollama

#establish connection to the local LLM
def call_llm(input):
 response = ollama.chat(
                       model="llama3.2:1b",
                       messages=[
                        {
                         "role":"user",
                        "content":"input"
                        }

                       ]
    )
 return response["message"]["content"]
user_input= input ("Enter user instruction:")
print("## USER INPUT ##\n")
print(user_input)
result = call_llm(user_input)
print("## AI RESPONSE ##\n")
print(result)
 ##coment 