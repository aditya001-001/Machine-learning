import logging
from typing import List, Tuple
from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import PromptTemplate
from langchain.chains import create_retrieval_chain

from utils.embedder import get_embedder
import config

# Configure logging for this module
logger = logging.getLogger(__name__)

def store_chunks(chunks: List[Document], persist_directory: str = None) -> Chroma:
    """
    embeds text chunks and stores them into a ChromaDB vector store.
    
    Args:
        chunks (List[Document]): The chunked documents containing text metadata.
        persist_directory (str, optional): The directory to store ChromaDB files locally. Defaults to config setting.
        
    Returns:
        Chroma: The instantiated and populated Chroma vector store.
        
    Example:
        >>> db = store_chunks(chunks)
    """
    # Use config default if not provided
    if persist_directory is None:
        persist_directory = config.CHROMA_PERSIST_DIR
        
    try:
        # Retrieve the configured embedder
        embedder = get_embedder()
        
        # Initialize and populate the vectorstore from the chunks and embeddings
        db = Chroma.from_documents(
            documents=chunks,
            embedding=embedder,
            persist_directory=persist_directory
        )
        
        # Ensure the vectorstore saves to disk successfully
        db.persist()
        logger.info(f"Stored {len(chunks)} chunks efficiently in Chroma DB at {persist_directory}")
        
        return db
        
    except Exception as e:
        logger.error(f"Error persisting chunks into ChromaDB: {e}")
        raise e

def query_rag(query: str, db: Chroma) -> Tuple[str, List[Document]]:
    """
    Executes a RAG retrieval and generation chain given user question and context DB.
    
    Args:
        query (str): The specific question asked by the user.
        db (Chroma): The primed and populated Chroma vector store.
        
    Returns:
        Tuple[str, List[Document]]: The final string LLM output, and the source chunk documents retrieved.
        
    Example:
        >>> answer, sources = query_rag("What is machine learning?", db)
    """
    try:
        # Load the LLM with settings optimized for factual tasks (0.3 temp limits hallucinations)
        llm = ChatGoogleGenerativeAI(
            model=config.MODEL_NAME,
            google_api_key=config.GOOGLE_API_KEY,
            temperature=0.3
        )
        
        # Design a prompt explicitly instructing the LLM to lean exclusively on returned context chunks
        template = """You are a helpful, professional, and precise research assistant.
        Use only the following pieces of retrieved context to answer the specific question.
        If you don't know the answer or the context doesn't contain the answer, say that you don't know rather than guess. 
        Keep your explanation clear and concise.
        
        Context: {context}
        
        Question: {input}
        
        Answer:"""
        
        prompt = PromptTemplate.from_template(template)
        
        # Creates a Langchain pipeline that "stuffs" all retrieved context documents into the prompt
        combine_docs_chain = create_stuff_documents_chain(llm, prompt)
        
        # Convert vector DB connection surface into an active retriever interface fetching top 3 docs
        retriever = db.as_retriever(search_kwargs={"k": 3})
        
        # Compose final RAG chain (Retrieval + Generation)
        retrieval_chain = create_retrieval_chain(retriever, combine_docs_chain)
        
        # Execute the request
        response = retrieval_chain.invoke({"input": query})
        
        answer = response.get("answer", "")
        source_docs = response.get("context", [])
        
        logger.info(f"Successfully generated a coherent RAG response for query target: {query}")
        
        return answer, source_docs
        
    except Exception as e:
        logger.error(f"Error processing question inside RAG system: {e}")
        raise e
