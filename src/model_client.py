from autogen_ext.models.openai import OpenAIChatCompletionClient
import os

model_client = OpenAIChatCompletionClient(
    model="llama3-8b-8192",  
    base_url="https://api.groq.com/openai/v1", 
    api_key=os.environ["GROQ_API_KEY"],
    model_info={
        "vision": True,
        "function_calling": True,
        "json_output": True,
        "family": "gpt-4",
    },
)

print("Model client initialized:", model_client)

