# Chat-application
 
# LLM Chat API

A FastAPI-based application that lets you interact with a Large Language Model (LLM) via HTTP requests. Send your prompt to the `/generate` endpoint and receive responses powered by our integrated LLM.

## Overview

This project provides a simple and efficient API interface to chat with an LLM. It leverages FastAPI to handle HTTP requests and communicate with the model. The application is designed to work seamlessly with the required libraries, which are listed in `requirements.txt`.

## Features

- **Simple API Endpoint:** Send prompts to `/generate` for LLM responses.
- **FastAPI Integration:** Built using FastAPI for high-performance asynchronous handling.
- **LLM and Embedding Support:** Supports the `deepseek-r1:1.5b` model for generating text and `nomic-embed-text` for embeddings.

## Prerequisites

Before you can run the application, make sure you have the following installed on your system:

1. **Python 3.8+**  
   Ensure Python is installed and available in your system's PATH.

2. **Ollama:**  
   The application requires [Ollama](https://ollama.com) to manage and run the LLM models. Follow the instructions on the Ollama website for installation.

3. **Model Pulls:**  
   - Pull the `deepseek-r1:1.5b` model:  
     ```bash
     ollama pull deepseek-r1:1.5b
     ```
   - Pull the embedding model `nomic-embed-text`:  
     ```bash
     ollama pull nomic-embed-text
     ```

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/MohanadElMetwally/Chat-application.git
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Required Dependencies** 
Run the following command to install the necessary Python libraries:  
```bash
pip install -r requirements.txt
```

4. **4. Pull the Required Models with Ollama**
Before running the application, you need to download the required models using Ollama. Run the following commands:  

- **Download the main LLM model:**  
  ```bash
  ollama pull deepseek-r1:1.5b
  ```

- **Download the embedding model:**  
  ```bash
  ollama pull nomic-embed-text
  ```

5. **Running the Application**
Once all dependencies and models are installed, start the FastAPI server:  

```bash
fastapi dev main.py
```

6. **Testing the `/generate` Endpoint** 

After starting the FastAPI server, you can test the `/generate` endpoint using various methods.

#### Using cURL:  
Run the following command in your terminal to send a request:  
```bash
curl -X POST "http://localhost:8000/generate" -H "Content-Type: application/json" -d '{"prompt": "Hello, how are you?"}'
```
