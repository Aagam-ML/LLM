from langchain_cohere.llms import Cohere
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import streamlit as st
from langchain_cohere import ChatCohere
import os

load_dotenv()
os.environ["COHERE_API_KEY"] = os.getenv("COHERE_API_KEY")
## Langsmith
os.environ["LANGCHAIN_TRACING_V2"]="True"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")


LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_PROJECT="Chatbot"

##Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant please response to the user queries"),
        ("user","Question:{question}")
    ]
)
st.title('Chatbot with Langchain & Cohore')
input_text = st.text_input('Search the topic you want to search')

llm = ChatCohere()
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))