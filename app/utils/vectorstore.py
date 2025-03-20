from langchain_chroma import Chroma
from app.utils.model import embedding_llm

vectorstore = Chroma(
    collection_name='ITHelp',
    persist_directory='../../Vectorstores',
    embedding_function=embedding_llm
)
retriever = vectorstore.as_retriever(search_type='similarity', search_kwargs={'k': 5})