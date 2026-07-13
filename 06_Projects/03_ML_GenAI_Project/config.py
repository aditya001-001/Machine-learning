import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging to display time, level, and message
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Constants retrieved from environment variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
CHROMA_PERSIST_DIR = os.getenv("CHROMA_PERSIST_DIR", "./chroma_db")
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 1000))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 200))

# Fixed Model Configurations
MODEL_NAME = "gemini-2.5-flash"
EMBEDDING_MODEL = "models/gemini-embedding-001"

def check_keys() -> bool:
    """
    Checks if all required environment variables are set.

    Returns:
        bool: True if all required keys are present, False otherwise.
        
    Example:
        >>> check_keys()
        True
    """
    if not GOOGLE_API_KEY:
        logger.error("GOOGLE_API_KEY is not set in environment.")
        return False
    # Additional keys can be checked here if needed
    return True
