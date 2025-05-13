from pydantic import BaseModel


class InputQuestion(BaseModel):
    question: str

    class Config:
        json_schema_extra = {"example": {"question": "What is your name?"}}
