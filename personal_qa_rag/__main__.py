import uvicorn


def main():
    uvicorn.run("personal_qa_rag.api.app:app")


if __name__ == "__main__":
    main()
