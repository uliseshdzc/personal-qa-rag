import re

from injector import inject, singleton
from langchain.chains.retrieval_qa.base import RetrievalQA

from personal_qa_rag.domain.services.llm_factory import LLMFactory
from personal_qa_rag.domain.services.rag_service import RAGService
from personal_qa_rag.domain.settings import Settings


@singleton
class QAService:
    @inject
    def __init__(
        self, rag_service: RAGService, llm_factory: LLMFactory, settings: Settings
    ):
        vector_store = rag_service.extract_vector_store(settings.source_url)
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=llm_factory.get(),
            retriever=vector_store.as_retriever(),
            return_source_documents=True,
        )

    @staticmethod
    def __parse_from_output(input: str) -> str | None:
        return re.sub(r"(^```html)|(```$)", "", input).strip()

    def ask(self, question: str) -> str | None:
        prompt = f"""
        Imagine you are the person of the vector store you are using. 
        You are going to answer professional questions. The output 
        must be in HTML format. The question is: {question}
        """
        result = self.qa_chain.invoke({"query": prompt})

        return self.__parse_from_output(result["result"])
