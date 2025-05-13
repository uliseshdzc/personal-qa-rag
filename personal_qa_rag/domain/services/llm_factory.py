from injector import singleton
from langchain_openai import ChatOpenAI


@singleton
class LLMFactory:
    def __init__(self):
        self.llm = ChatOpenAI(name="gpt-4-turbo", temperature=0)

    def get(self):
        return self.llm
