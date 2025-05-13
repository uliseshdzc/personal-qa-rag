from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi_injector import Injected

from personal_qa_rag.domain.models.input_question import InputQuestion
from personal_qa_rag.domain.services.qa_service import QAService

router = APIRouter(tags=["Questions"])


@router.post(
    # "/source/{source}/question",
    "/question",
    response_class=HTMLResponse,
    responses={200: {"content": {"text/html": {"example": "<p>My response</p>"}}}},
    summary="Retrieves the personal information using RAG",
    description="Retrieves the personal information that corresponds to the input question using RAG.",
)
def retrieve_information(
    input_question: InputQuestion,
    # source: Annotated[
    #     str,
    #     Path(
    #         title="The embedding source",
    #         description="The embedding source to utilize. If a null source is transmitted, a new embedding source will be created for every query.",
    #     ),
    # ] = None,
    qa_service=Injected(QAService),
):
    return qa_service.ask(input_question.question)
