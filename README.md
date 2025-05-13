# Personal Question-Answering with RAG

This project is a back-end API conceived to work as a bridge between the Generative AI source and the front-end using RAG.

## Setup

### Prerequisites

- Python 3.13
- Virtual environment tool (e.g., `venv`)

### Installation

1. Installing Python 3.13

   **Windows:**

   - Download the installer from the official [Python website](https://www.python.org/downloads/).
   - Run the installer and follow the instructions. Make sure to check the box that says "Add Python to PATH".

     **macOS:**

   - You can use Homebrew to install Python 3.13:

     ```sh
     brew install python@3.13
     ```

     **Linux:**

   - Use your package manager to install Python 3.13. For example, on Ubuntu:
     ```sh
     sudo apt update
     sudo apt install python3.13
     ```

2. **Create a virtual environment:**

   ```
   python3.13 -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
   ```
   .\venv\Scripts\activate
   ```
   - On macOS and Linux:
   ```
   source venv/bin/activate
   ```
4. **Install the required packages:**

   ```
   pip install -r requirements.txt
   ```

## Usage
1. **Set the environment variables**: It is necessary to set the following environment variables:

    | Variable       | Description                                                                       |
    |----------------|-----------------------------------------------------------------------------------|
    | OPENAI_API_KEY | API key to access the OpenAI project                                              |
    | SOURCE_URL     | URL with the resume using the [JSON Resume](https://jsonresume.org/schema) format |

   This can
3. **Run the application:**

   ```
   python -m personal_qa_rag
   ```

   This will launch the API. It is then possible to look at the OpenAPI site at http://localhost:8000/docs.
