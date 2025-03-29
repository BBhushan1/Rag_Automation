import json
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss
import logging
import os

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler("logs/rag_engine.log")
formatter = logging.Formatter("%(asctime)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

class RAGEngine:
    def __init__(self, metadata_file="data/function_metadata.json"):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = faiss.IndexFlatL2(384)  
        self.functions = []
        self.function_metadata = []
        self.load_metadata(metadata_file)

    def load_metadata(self, metadata_file):
        try:
            with open(metadata_file, 'r') as f:
                self.function_metadata = json.load(f)
            descriptions = [func["description"] for func in self.function_metadata]
            embeddings = self.model.encode(descriptions)
            self.index.add(np.array(embeddings, dtype=np.float32))
            self.functions = [func["name"] for func in self.function_metadata]
            logger.info(f"Loaded metadata for {len(self.functions)} functions.")
        except FileNotFoundError:
            logger.error(f"Metadata file not found: {metadata_file}")
            raise FileNotFoundError(f"Metadata file not found: {metadata_file}")
        except json.JSONDecodeError:
            logger.error("Invalid JSON format in metadata file.")
            raise ValueError("Invalid JSON format in metadata file.")

    def reload_metadata(self, metadata_file=None):
        if metadata_file:
            self.load_metadata(metadata_file)
        else:
            self.load_metadata("data/function_metadata.json")  

    def retrieve_function(self, query, threshold=0.5):
        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(np.array(query_embedding, dtype=np.float32), 1)
        
        normalized_distance = distances[0][0] / np.linalg.norm(query_embedding)
        
        if normalized_distance > threshold:
            logger.warning(f"Poor match for query: {query}")
            return None, None
        
        matched_index = indices[0][0]
        return (
            self.function_metadata[matched_index]["name"],
            self.function_metadata[matched_index].get("parameters", [])
        )