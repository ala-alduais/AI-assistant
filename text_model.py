import os
from urllib import response
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key = os.environ.get('GOOGLE_API_KEY'))

model= genai.generativeModel("gemini-1.5",
                             system_instruction="you are helpful assistant",
                             )

response = model.generate_content("How is tea made",
                                  generation_config=genai.types.GenerationConfig(
                                      max_output_tokens=10 ))
print(response.text)

"""
make a code debuing app using gemini api

input == code snippet
output == explanation

use openai API
"""

code = """
dgfhjhkjdghfgh
fjighcjklj
xgfchvjbknl
"""



code = debugger(AI model) = explain