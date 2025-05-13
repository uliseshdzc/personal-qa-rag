from functools import cache

import httpx
import requests
import yaml
from injector import singleton
from langchain.docstore.document import Document
from langchain_community.vectorstores import FAISS
from langchain_openai.embeddings import OpenAIEmbeddings


@singleton
class RAGService:
    def __get_chunks(self, data: str):
        return self.__flatten_json(data)

    def __flatten_json(self, obj):
        chunks = []
        for key, value in obj.items():
            chunks.append(f"{key}: {yaml.dump(value)}")
        return chunks

    @cache
    def extract_vector_store(self, source: str):
        data = requests.get(source).json()
        text_chunks = self.__get_chunks(data)

        documents = [Document(page_content=chunk) for chunk in text_chunks]

        embeddings = OpenAIEmbeddings()
        vector_store = FAISS.from_documents(documents, embeddings)

        return vector_store
