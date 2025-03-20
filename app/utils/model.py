from langchain_ollama.chat_models import ChatOllama
from langchain_ollama.embeddings import OllamaEmbeddings

embedding_llm = OllamaEmbeddings(model='nomic-embed-text')
llm = ChatOllama(model='deepseek-r1:1.5b')