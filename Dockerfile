FROM python:3.13.3-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --default-timeout=100 -r requirements.txt

COPY personal_qa_rag ./personal_qa_rag

EXPOSE 8000

CMD ["uvicorn", "personal_qa_rag.api.app:app", "--host", "0.0.0.0", "--port", "8000"]