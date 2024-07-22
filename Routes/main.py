import os
from dotenv import load_dotenv
from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_cohere import ChatCohere
from langserve import add_routes
import uvicorn
from langchain_community.llms import Ollama


load_dotenv()

os.environ["COHERE_API_KEY"] = os.getenv("COHERE_API_KEY")
## Langsmith
os.environ["LANGCHAIN_TRACING_V2"]="True"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

app = FastAPI(
    title='Langchain_server',
    version='1.0',
    description='A simple API Server'
)

add_routes(
    app,
    ChatCohere(),
    path='/Chat_Cohore'
)
model=ChatCohere()
llm = Ollama(model='llama2')
prompt1 = ChatPromptTemplate.from_template("Write me an essay about specific {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("Write me a poem on specific {topic} with 100 words")

add_routes(
    app,
    prompt1|model,
    path='/essay'
)

add_routes(
    app,
    prompt2|llm,
    path='/poem'
)

if __name__ == '__main__':
    uvicorn.run(app,host='localhost',port=8000)