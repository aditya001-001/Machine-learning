import importlib
import streamlit as st
import config
from utils.document_loader import load_document
from utils.chunker import chunk_documents
from utils.retriever import store_chunks, query_rag
from utils.validator import validate_file, validate_query

def main():
    """
    Main Streamlit application entry point handling UI layout and logic flow.
    Orchestrates the UI elements connecting Document ingestion, storage, retrieval, and conversation.
    """
    # Initialize basic Streamlit layout preferences before rendering
    st.set_page_config(page_title="Multi-Document RAG Research Assistant", layout="wide")
    st.title("📚 Multi-Document RAG Research Assistant")
    
    # Pre-flight readiness check for critical API keys
    try:
        importlib.reload(config)
    except Exception:
        pass
        
    if not config.check_keys():
        st.error("Critical environment variables are missing. Please configure your .env file or deployment secrets.")
        st.stop()
        
    # Isolate ingestion elements into a clean sidebar navigation interface
    with st.sidebar:
        st.header("Document Upload")
        uploaded_file = st.file_uploader("Upload a PDF, TXT, or DOCX", type=["pdf", "txt", "docx"])
        
        # We enforce a deliberate action button to avoid processing partially loaded files
        if st.button("Process Document"):
            if uploaded_file is None:
                st.error("Please upload a file first to initialize.")
            else:
                # Intercept invalid files quickly before wasting computation power
                valid, msg = validate_file(uploaded_file.name, uploaded_file.size)
                if not valid:
                    st.error(msg)
                else:
                    try:
                        # Staged visual feedback guides the user through the pipeline progress
                        with st.spinner("Extracting text from loaded document..."):
                            docs = load_document(uploaded_file.getvalue(), uploaded_file.name)
                            
                        with st.spinner("Splitting large text sections into localized chunks..."):
                            chunks = chunk_documents(docs)
                            
                        with st.spinner("Generating vector embeddings and synchronizing database..."):
                            # The vectorstore requires persistence across interactions in Session State
                            st.session_state['vector_db'] = store_chunks(chunks)
                            
                        st.success(f"Processing sequence complete! Embedded {len(chunks)} contextual chunks successfully.")
                    except Exception as e:
                        # Graceful failure on extraction elements rather than raw exceptions
                        st.error(f"A pipeline error occurred during document processing: {e}")
                        
    # Setup primary Chat input layout for researcher interaction
    st.header("Ask Research Questions")
    user_query = st.text_input("Enter your analytical or research question below:")
    
    # We restrict query firing until explict button press to prevent half-written query execution
    if st.button("Submit Query"):
        valid_q, query_msg = validate_query(user_query)
        
        # Halt execution on poor quality questions
        if not valid_q:
            st.error(query_msg)
        # Verify the database exists in state
        elif 'vector_db' not in st.session_state:
            st.error("Please securely upload and process a valid research document first.")
        else:
            with st.spinner("Searching knowledge base and generating grounded response..."):
                try:
                    db = st.session_state['vector_db']
                    # Dispatch to modular business logic
                    answer, sources = query_rag(user_query, db)
                    
                    st.markdown("### Synthesized Answer")
                    st.write(answer)
                    
                    st.markdown("### Document Citations")
                    # We render sources strictly to verify zero hallucination
                    for i, doc in enumerate(sources):
                        with st.expander(f"Reference Location {i+1} : {doc.metadata.get('source', 'Unknown')}"):
                            st.write(doc.page_content)
                            
                    # Implement local export logic for sharing outputs
                    result_text = f"Research Question: {user_query}\n\nSynthesized Answer: {answer}\n\nReference Extracts:\n"
                    for d in sources:
                        result_text += f"- {d.page_content}\n"
                    
                    # Direct binary download bypassing normal routing latency
                    st.download_button(
                        label="Download Full Output Report",
                        data=result_text,
                        file_name="research_output.txt",
                        mime="text/plain"
                    )
                except Exception as e:
                    # Generic fallback handling system errors avoiding app crashes
                    st.error(f"An unexpected inference error occurred during generation: {e}")

if __name__ == "__main__":
    main()
