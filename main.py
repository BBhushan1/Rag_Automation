from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from rag_engine import RAGEngine
from code_generator import generate_code
from memory import SessionMemory
import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/execution.log"),
        logging.StreamHandler()  
    ]
)

app = FastAPI()
rag = RAGEngine()
memory = SessionMemory()

class PromptRequest(BaseModel):
    prompt: str
    parameters: dict = None 

@app.post("/execute", summary="Execute Automation Function")
async def execute_prompt(request: PromptRequest):
    try:
        logging.info(f"Received request: {request}")

        function_name, parameters = rag.retrieve_function(request.prompt)
        
        valid_functions = ["open_chrome", "open_calculator", "open_notepad", 
                           "get_cpu_usage", "get_ram_usage", "run_shell_command"]
        if function_name not in valid_functions:
            logging.error(f"Invalid function retrieved: {function_name}")
            raise HTTPException(status_code=400, detail="Invalid function retrieved.")
        
        generated_code = generate_code(function_name, parameters=request.parameters)
        
        logging.info(f"Prompt: {request.prompt}, Function: {function_name}, Parameters: {request.parameters}")
        
        memory.add_interaction(
            prompt=request.prompt,
            function_name=function_name,
            parameters=request.parameters
        )
        
        logging.info(f"Generated code: {generated_code}")
        return {"function": function_name, "code": generated_code}
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))