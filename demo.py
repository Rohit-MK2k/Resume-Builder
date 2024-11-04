import os 
from secret import huggingface_key
from langchain_huggingface import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_core.output_parsers import StrOutputParser

os.environ["HUGGINGFACEHUB_API_TOKEN"] = huggingface_key

llm_repo = "mistralai/Mistral-7B-Instruct-v0.3"

llm = HuggingFaceEndpoint(repo_id=llm_repo, 
                          max_length = 128, 
                          temperature=0.4, 
                          token = huggingface_key)

input = input("Enter any celebrity name...")
# name = llm.invoke(input)


#Prompt templates
input_template = PromptTemplate(
    input_variables = ['name'],
    template = "Tell me about the celebrity {name} "
)

chain = input_template | llm 
# chain = LLMChain(llm = llm, prompt = input_template, verbose = True)
print(chain(input))
