import requests
import streamlit as st



import requests

def get_cohore_response(input_text):
    response = requests.post(
        'http://localhost:8000/essay/invoke',
        json={'input': {'topic': input_text}}
    )
    return response.json()['output']['content']

def get_ollama_response(input_text):
    response = requests.post(
        'http://localhost:8000/poem/invoke',
        json={'input': {'topic': input_text}}
    )
    return response.json()['output']


st.title('Routes with Langchain , Cohere , Ollama')
input_text = st.text_input('Write an essay on (requests to cohere LLM)')
input_text1 = st.text_input('Write an poem on (requests to ollama LLM)')

if input_text:
    st.write(get_cohore_response(input_text))

if input_text1:
    st.write(get_ollama_response(input_text1))