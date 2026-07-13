import logging
from typing import Tuple

# Configure logging for this module
logger = logging.getLogger(__name__)

def validate_file(filename: str, file_size: int) -> Tuple[bool, str]:
    """
    Validates uploaded file against correct extension formats and file size guidelines.
    
    Args:
        filename (str): Name of the file being processed.
        file_size (int): Size footprint of the file in bytes.
        
    Returns:
        Tuple[bool, str]: A validation boolean flag alongside a status/error message string.
        
    Example:
        >>> valid, msg = validate_file("test.pdf", 1024)
    """
    # Hardcoded restrictions mapped according to common application limits and project requirements
    allowed_extensions = ['.pdf', '.txt', '.docx']
    max_size_bytes = 10 * 1024 * 1024 # Exactly 10 MB cap for stability during embedding
    
    try:
        # Limit sizing to protect against Out-Of-Memory/Excessive billing
        if file_size > max_size_bytes:
            return False, "File is too large. Maximum size is 10 MB."
            
        # Limit scope to ensure Langchain loaders don't crash from unsupported types
        if not any(filename.lower().endswith(ext) for ext in allowed_extensions):
            return False, f"Unsupported file type. Allowed: {', '.join(allowed_extensions)}"
            
        return True, "File is fully valid."
        
    except Exception as e:
        logger.error(f"A validation error occurred on file constraints: {e}")
        return False, "An error occurred during file validation mechanisms."

def validate_query(query: str) -> Tuple[bool, str]:
    """
    Validates a researcher prompt before submission to limit malicious or poor quality vector searches.
    
    Args:
        query (str): The raw text sequence from the user input.
        
    Returns:
        Tuple[bool, str]: A validation boolean flag linked with a reason string.
        
    Example:
        >>> valid, msg = validate_query("Summarize this context.")
    """
    # Guard against completely empty submissions causing database match chaos
    if not query or not query.strip():
        return False, "Query cannot be completely empty."
        
    # Guard against single-character/abstract submissions lacking intent context
    if len(query) < 3:
        return False, "Query must be at least 3 characters long to ensure meaningful intent."
        
    return True, "Valid query parameters."
