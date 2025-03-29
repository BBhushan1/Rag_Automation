**RAG-Based Function Execution API**

#Overview#
This project implements a Python-based API service that dynamically retrieves and executes automation functions using RAG. The system processes user prompts, maps them to 
predefined automation functions, and generates executable Python code for function invocation.

The API is built using FastAPI and integrates with FAISS for vector search and Sentence Transformers for embeddings. 
It supports application control, system monitoring, and command execution tasks.

Features
Function Registry : Predefined automation functions for common tasks like opening applications, retrieving system stats, and running shell commands.
RAG Model : Uses FAISS for vector search and Sentence Transformers to retrieve the best-matching function based on user prompts.
Dynamic Code Generation : Generates structured Python scripts for invoking matched functions, including proper imports, error handling, and modularity.
Session Memory : Maintains interaction history for context-aware responses.
API Service : Exposes a REST API endpoint (/execute) for processing user queries and returning executable Python code.

Installation and Setup
Prerequisites
Python 3.8 or higher
Install required dependencies:
bash
Copy
1
pip install -r requirements.txt
Steps to Run the Project
Clone the Repository :
bash
Copy
1
2
git clone <your-repo-url>
cd <project-directory>
Install Dependencies :
bash
Copy
1
pip install -r requirements.txt
Start the FastAPI Server :
bash
Copy
1
uvicorn main:app --reload
Access the API Documentation :
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
Usage
API Endpoint
POST /execute
Request :
json
Copy
1
2
3
⌄
{
  "prompt": "Open Google Chrome"
}
Response :
json
Copy
1
2
3
4
⌄
{
  "function": "open_chrome",
  "code": "from automation_functions import open_chrome\n\ndef main():\n    try:\n        open_chrome()\n        print(\"Chrome opened successfully.\")\n    except Exception as e:\n        print(f\"Error executing function: {e}\")\n\nif __name__ == \"__main__\":\n    main()"
}
Sample Requests and Responses
"Open Google Chrome"
open_chrome
python from automation_functions import open_chrome def main(): try: open_chrome() print("Chrome opened successfully.") except Exception as e: print(f"Error executing function: {e}") if __name__ == "__main__": main()
"Retrieve CPU usage"
get_cpu_usage
python from automation_functions import get_cpu_usage def main(): try: cpu_usage = get_cpu_usage() print(f"CPU Usage: {cpu_usage}%") except Exception as e: print(f"Error executing function: {e}") if __name__ == "__main__": main()
"Run shell command: dir"
run_shell_command
python from automation_functions import run_shell_command def main(): try: result = run_shell_command("dir") print(f"Command executed successfully. Result: {result}") except Exception as e: print(f"Error executing function: {e}") if __name__ == "__main__": main()
"xyz"
Error
json {"detail": "No matching function found for the given prompt."}



Optional Enhancements
Logging and Monitoring : Logs are written to logs/execution.log, logs/rag_engine.log, and logs/session_memory.log for debugging and monitoring.
Custom User-Defined Functions : Extend the system to support user-uploaded functions (future enhancement).
