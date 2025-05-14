FROM python:3.13.3-alpine

WORKDIR /app

COPY requirements.txt .

# Required for Cargo
RUN apk add --no-cache rust cargo
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --default-timeout=100 --root-user-action -r requirements.txt

COPY personal_qa_rag .

EXPOSE 8000

CMD ["uvicorn", "personal_qa_rag.api.app:app", "--host", "0.0.0.0", "--port", "8000"]