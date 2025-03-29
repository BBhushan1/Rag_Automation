from datetime import datetime
import logging
import os

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler("logs/session_memory.log")
formatter = logging.Formatter("%(asctime)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

class SessionMemory:
    def __init__(self):
        self.history = []

    def add_interaction(self, prompt, function_name, parameters=None):
        interaction = {
            "prompt": prompt,
            "function": function_name,
            "parameters": parameters,
            "timestamp": datetime.now().isoformat()
        }
        self.history.append(interaction)
        logger.info(f"Interaction: {interaction}")

    def get_context(self, n=3):
        return self.history[-n:]  

    def clear_history(self):
        self.history.clear()