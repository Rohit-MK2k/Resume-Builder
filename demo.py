import os 
from secret import huggingface_key
from langchain_huggingface import HuggingFaceEndpoint

os.environ["HUGGINGFACEHUB_API_TOKEN"] = huggingface_key

llm_repo = "mistralai/Mistral-7B-Instruct-v0.3"

llm = HuggingFaceEndpoint(repo_id=llm_repo, 
                          max_length = 128, 
                          temperature=0.7, 
                          token = huggingface_key)
name = llm.invoke("What is the machine learning?")
print(name)