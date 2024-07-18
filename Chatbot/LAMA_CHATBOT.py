from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import streamlit as st
from langchain_community.llms import Ollama
import os

load_dotenv()


## Langsmith
os.environ["LANGCHAIN_TRACING_V2"]="True"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant please response to the user queries"),
        ("user","Question:{question}")
    ]
)
st.title('Langchain demo with LAMA')
input_text = st.text_input('Search the topic you want to search')

llm = Ollama(model="llama2")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))