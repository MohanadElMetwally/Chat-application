from app.utils.model import llm
from app.utils.vectorstore import retriever
from app.utils.database import get_collection
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda

class ChatService:
    def __init__(self):
        self.chain = self._create_chain()

    def _create_chain(self):
        prompt_template = ChatPromptTemplate.from_template(
            """
        You are an IT expert that helps employees solve any issue they face.

        Use the following piece of context to help you generate a correct answer to the question at the end.
        If the answer requires you to recall something from an earlier conversation, use Session Memory, as it can help you remember important information needed to respond to the question.
        If you don't know, say that you don't know.

        Context:
        {context}

        Session Memory:
        {session_memory}

        Question:
        {question}
        """
        )

        # chain the workflow using LCEL
        chain = (
            {
                'context': retriever, 
                'session_memory': RunnableLambda(lambda _: get_collection().find_one({'session_id': self.session_id})['messages']), 
                'question': RunnablePassthrough()
            } | prompt_template | llm | StrOutputParser()
        )
        return chain

    def generate_response(self, prompt, session_id: int):
        self.session_id = session_id
        return self.chain.invoke(prompt)