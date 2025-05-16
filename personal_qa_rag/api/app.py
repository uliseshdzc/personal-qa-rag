from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_injector import attach_injector

from personal_qa_rag.api.controllers import questions
from personal_qa_rag.api.dependency_injection import injector
from personal_qa_rag.domain.settings import Settings

settings = Settings()
app = FastAPI(
    title="Personal Question-Answering with RAG",
    version=settings.version,
    description="API conceived to work as a bridge between the Generative AI source and the Front End using RAG.",
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(questions.router)
attach_injector(app, injector)
