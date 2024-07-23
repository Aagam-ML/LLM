## Data ingestion
import os
from dotenv import load_dotenv
load_dotenv()
os.environ['COHERE_API_KEY'] = os.getenv("COHERE_API_KEY")

## Data Ingestion
from langchain_community.document_loaders import TextLoader
loader=TextLoader("Speech.txt")
text_documents=loader.load()

from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
documents=text_splitter.split_documents(text_documents)
documents[:5]

#vector embedding
from langchain_community.embeddings import OllamaEmbeddings
from langchain_cohere import CohereEmbeddings
from langchain_community.vectorstores import Chroma
db = Chroma.from_documents(documents,CohereEmbeddings())

query = "What are Challenges in Machine learning"
retireved_results=db.similarity_search(query)
print(retireved_results[0].page_content)



##web based loader

# web based loader

#--------------------------------------------------------------------------------------------------------------------------
## load,chunk and index the content of the html page
from langchain_community.document_loaders import WebBaseLoader
import bs4

loader=WebBaseLoader(web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
                     bs_kwargs=dict(parse_only=bs4.SoupStrainer(
                         class_=("post-title","post-content","post-header")

                     )))

text_documents=loader.load()
from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
documents=text_splitter.split_documents(text_documents)
documents[:5]

#vector embedding
from langchain_community.embeddings import OllamaEmbeddings
from langchain_cohere import CohereEmbeddings
from langchain_community.vectorstores import Chroma
db = Chroma.from_documents(documents,CohereEmbeddings())

query = "What are the types of memory in Agent system overview"
retireved_results=db.similarity_search(query)
print(retireved_results[0].page_content)

#-------------------------------------------------------------------------------------------------------------------------
## Pdf reader
from langchain_community.document_loaders import PyPDFLoader
loader=PyPDFLoader('Artificial_Intelligence.pdf')
docs=loader.load()
#converting this texts into chunks

from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
documents=text_splitter.split_documents(docs)
documents[:5]

#vector embedding
from langchain_community.embeddings import OllamaEmbeddings
from langchain_cohere import CohereEmbeddings
from langchain_community.vectorstores import Chroma
db = Chroma.from_documents(documents,CohereEmbeddings())

query = "What is weak AI?"
retireved_results=db.similarity_search(query)
print(retireved_results[0].page_content)

#--------------------------------------------------------------------------------------------------------------------------

