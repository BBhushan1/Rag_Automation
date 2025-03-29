# 🤖 RAG-Based Function Execution API


## 📋 Overview

This project implements a Python-based API service that dynamically retrieves and executes automation functions using LLM (Large Language Model) and RAG. The system processes user prompts, 
maps them to predefined automation functions, and generates executable Python code for function invocation.

The API is built using FastAPI and integrates with FAISS for vector search and Sentence Transformers for embeddings. 
It supports application control, system monitoring, and command execution tasks.

## ✨ Features

- **Function Registry**: Predefined automation functions for common tasks like opening applications, retrieving system stats, and running shell commands
- **RAG Model**: Uses FAISS for vector search and Sentence Transformers to retrieve the best-matching function based on user prompts
- **Dynamic Code Generation**: Generates structured Python scripts for invoking matched functions, including proper imports, error handling, and modularity
- **Session Memory**: Maintains interaction history for context-aware responses
- **API Service**: Exposes a REST API endpoint (`/execute`) for processing user queries and returning executable Python code

## 🚀 Installation and Setup

### Prerequisites

- Python 3.8 or higher
- Required dependencies (install via requirements.txt)

### Steps to Run the Project

1. **Clone the Repository**:

   git clone https://github.com/BBhushan1/Rag_Automation

  

2. **Install Dependencies**:
  
   pip install -r requirements.txt
   

3. **Start the FastAPI Server**:
 
   uvicorn main:app --reload
  

4. **Access the API Documentation**:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 📘 Usage

### API Endpoint

**POST** `/execute`

#### Request:

{
  "prompt": "Open Google Chrome"
}


#### Response:

{
  "function": "open_chrome",
  "code": "from automation_functions import open_chrome\n\ndef main():\n    try:\n        open_chrome()\n        print(\"Chrome opened successfully.\")\n    except Exception as e:\n        print(f\"Error executing function: {e}\")\n\nif __name__ == \"__main__\":\n    main()"
}


### Sample Requests and Responses

| User Prompt | Function Called | Generated Code |
|-------------|----------------|---------------|
| "Open Google Chrome" | `open_chrome` | ```python\nfrom automation_functions import open_chrome\n\ndef main():\n    try:\n        open_chrome()\n        print("Chrome opened successfully.")\n    except Exception as e:\n        print(f"Error executing function: {e}")\n\nif __name__ == "__main__":\n    main()``` |
| "Retrieve CPU usage" | `get_cpu_usage` | ```python\nfrom automation_functions import get_cpu_usage\n\ndef main():\n    try:\n        cpu_usage = get_cpu_usage()\n        print(f"CPU Usage: {cpu_usage}%")\n    except Exception as e:\n        print(f"Error executing function: {e}")\n\nif __name__ == "__main__":\n    main()``` |
| "Run shell command: dir" | `run_shell_command` | ```python\nfrom automation_functions import run_shell_command\n\ndef main():\n    try:\n        result = run_shell_command("dir")\n        print(f"Command executed successfully. Result: {result}")\n    except Exception as e:\n        print(f"Error executing function: {e}")\n\nif __name__ == "__main__":\n    main()``` |
| "xyz" | Error | ```json\n{"detail": "No matching function found for the given prompt."}``` |


## 📝 Logging and Monitoring

The system writes logs to the following files for debugging and monitoring:
- `logs/execution.log` - Function execution logs
- `logs/rag_engine.log` - RAG engine processing logs
- `logs/session_memory.log` - Session and context tracking logs


## 🔮 Future Enhancements

- **Custom User-Defined Functions**: Support for user-uploaded automation functions
- **Enhanced Error Handling**: More detailed error messages and recovery mechanisms
- **Performance Optimization**: Caching common requests and optimizing vector search
- **Authentication and Authorization**: Secure API access with user authentication


