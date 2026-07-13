import os
import logging
import tempfile
from typing import List
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader, TextLoader, Docx2txtLoader

# Configure logging for this module
logger = logging.getLogger(__name__)

def load_document(file_bytes: bytes, filename: str) -> List[Document]:
    """
    Loads a document from bytes into LangChain Document objects based on extension.
    
    Args:
        file_bytes (bytes): The raw bytes content of the uploaded file.
        filename (str): The original filename, used to determine the file type.
        
    Returns:
        List[Document]: A list of LangChain Document objects ready for chunking.
        
    Example:
        >>> docs = load_document(my_bytes, "sample.pdf")
    """
    docs = []
    
    try:
        # LangChain loaders typically require a file path. We use a NamedTemporaryFile
        # to write the bytes to disk temporarily, allowing the loaders to read it.
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(filename)[1]) as temp_file:
            temp_file.write(file_bytes)
            temp_file_path = temp_file.name

        # Determine which loader to use based on the file extension
        if filename.lower().endswith(".pdf"):
            loader = PyPDFLoader(temp_file_path)
            docs = loader.load()
        elif filename.lower().endswith(".txt"):
            loader = TextLoader(temp_file_path)
            docs = loader.load()
        elif filename.lower().endswith(".docx"):
            loader = Docx2txtLoader(temp_file_path)
            docs = loader.load()
        else:
            raise ValueError(f"Unsupported file format provided: {filename}")
            
        logger.info(f"Successfully loaded {filename} into {len(docs)} document pages/sections.")
        
    except Exception as e:
        logger.error(f"Error occurred while loading document {filename}: {e}")
        raise e
        
    finally:
        # We must clean up the temporary file from the disk to prevent space leaks
        if 'temp_file_path' in locals() and os.path.exists(temp_file_path):
            os.remove(temp_file_path)
            
    return docs
