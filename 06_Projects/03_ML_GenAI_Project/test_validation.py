import os
import sys

def run_tests():
    """
    Executes a suite of 5 modular validation tests establishing 
    correct baseline project integration prior to stream launch.
    """
    tests_passed = 0
    print("Starting Validation Suite for RAG System...\n")
    
    # Test 1: Critical Dependency Setup Check
    try:
        import streamlit
        import langchain
        import chromadb
        import google.generativeai
        print("[v] Test 1: Core imports loaded correctly... PASS")
        tests_passed += 1
    except ImportError as e:
        print(f"[x] Test 1: Environment dependency failure... FAIL -> {e}")

    # Test 2: Environment Variable Ingestion 
    try:
        # Mocking environment overrides config fallbacks
        os.environ["GOOGLE_API_KEY"] = "fake_key_for_test"
        import config
        import importlib
        importlib.reload(config)
        
        assert config.check_keys() is True, "Config failed to accept synthetic inputs"
        print("[v] Test 2: Environment configuration ingestion... PASS")
        tests_passed += 1
    except Exception as e:
        print(f"[x] Test 2: Configuration mapping mechanism failure... FAIL -> {e}")

    # Test 3: Safe Recursive Chunking Behavior
    try:
        from utils.chunker import chunk_documents
        from langchain_core.documents import Document
        
        # Test basic chunk boundaries avoiding API hit
        doc = Document(page_content="Word " * 500, metadata={"source": "test.txt"})
        chunks = chunk_documents([doc])
        
        assert len(chunks) > 1, "Documents failed to recursively subdivide"
        print("[v] Test 3: Structural chunking boundary allocation... PASS")
        tests_passed += 1
    except Exception as e:
        print(f"[x] Test 3: Langchain splitter algorithm crashed... FAIL -> {e}")

    # Test 4: Embedding Interface Loading Logic 
    try:
        from utils.embedder import get_embedder
        import utils.embedder
        import importlib
        importlib.reload(utils.embedder)
        
        embedder = get_embedder()
        assert embedder is not None, "Failed to instantiate Embedding Object"
        
        print("[v] Test 4: Provider embedder wrapper instantiation... PASS")
        tests_passed += 1
    except Exception as e:
        print(f"[x] Test 4: Embedder configuration failure under mocking... FAIL -> {e}")
        
    # Test 5: Custom Guardrail Input Logic Validation
    try:
        from utils.validator import validate_file, validate_query
        
        # Validate correct boundary conditions on file handler filters
        v_res, _ = validate_file("academic_doc.pdf", 1024)
        vq_res, _ = validate_query("") # Try simulating bad input
        
        assert v_res is True, "Healthy documents arbitrarily failing format check"
        assert vq_res is False, "Empty strings bypassing text filters"
        
        print("[v] Test 5: Dual parameter boundary validations... PASS")
        tests_passed += 1
    except Exception as e:
        print(f"[x] Test 5: Input validators bypassed/damaged... FAIL -> {e}")

    # Execution summary
    if tests_passed == 5:
        print("\nAll 5 Validation Checks PASS! Application is greenlit for deployment.")
        sys.exit(0)
    else:
        print(f"\nSystem Degraded! {tests_passed}/5 Checks Completed. Review logs.")
        sys.exit(1)

if __name__ == "__main__":
    run_tests()
