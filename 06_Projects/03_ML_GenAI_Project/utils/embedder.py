import logging
from typing import Any
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import config

# Configure logging for this module
logger = logging.getLogger(__name__)

def get_embedder() -> Any:
    """
    Initializes and returns the Google Gemini embedding model.
    The embedder is responsible for converting text chunks into vector representations.
    
    Returns:
        GoogleGenerativeAIEmbeddings: The initialized embedding model object or compatible interface.
        
    Example:
        >>> embedder = get_embedder()
    """
    try:
        # We specifically initialize the Google Generative AI Embeddings 
        # using the config parameters to avoid hardcoding secrets.
        embedder = GoogleGenerativeAIEmbeddings(
            model=config.EMBEDDING_MODEL,
            google_api_key=config.GOOGLE_API_KEY
        )
        logger.info("Successfully initialized the Gemini Generative AI Embedder.")
        
        return embedder
        
    except Exception as e:
        logger.error(f"Failed to initialize the Gemini embedder. Error: {e}")
        raise e
