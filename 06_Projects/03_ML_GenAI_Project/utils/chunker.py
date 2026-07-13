import logging
from typing import List
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
import config

# Configure logging for this module
logger = logging.getLogger(__name__)

def chunk_documents(documents: List[Document]) -> List[Document]:
    """
    Splits a list of Document objects into smaller overlapping chunks.
    This helps the RAG system to fit context into the LLM context window limits
    and improves retrieval granularity.
    
    Args:
        documents (List[Document]): The input list of parsed Documents.
        
    Returns:
        List[Document]: A list of chunked Document objects.
        
    Example:
        >>> chunks = chunk_documents(documents)
    """
    try:
        # We use RecursiveCharacterTextSplitter because it tries to split on 
        # logical boundaries (like paragraphs and newlines) before defaulting to arbitrary splits.
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=config.CHUNK_SIZE,
            chunk_overlap=config.CHUNK_OVERLAP,
            separators=["\n\n", "\n", " ", ""]
        )
        
        # Perform the actual splitting logic
        chunks = text_splitter.split_documents(documents)
        logger.info(f"Successfully split {len(documents)} documents into {len(chunks)} distinct chunks.")
        
        return chunks
        
    except Exception as e:
        logger.error(f"Failed to chunk documents due to: {e}")
        raise e
