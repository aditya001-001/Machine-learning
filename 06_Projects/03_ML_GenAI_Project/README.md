# Multi-Document RAG Research Assistant

An intelligent research assistant powered by LangChain, Google Gemini, ChromaDB, and Streamlit. It allows users to upload documents (`.pdf`, `.txt`, `.docx`), index them, and ask complex analytical questions based on their content, complete with source citations.

---

## Technical Stack
- **Frontend UI:** Streamlit
- **Agent Orchestration:** LangChain
- **Embeddings Pipeline:** Google Generative AI Embeddings (`models/embedding-001`)
- **LLM Pipeline:** Google Gemini 1.5 Pro (`gemini-1.5-pro-latest`)
- **Vector Database:** ChromaDB (local persistence)
- **Tooling:** Python `dotenv`, `pytest` methodologies, `pypdf`, `python-docx`

---

## Validation Checklist

Prior to final usage, ensure the following constraints pass successfully:

1. `python test_validation.py` → all 5 validation checks execute and PASS.
2. `streamlit run app.py` → interface smoothly opens on `localhost:8501`, rendering without trace errors.
3. `python -c "import config; print(config.check_keys())"` → Prints `True`.
4. Upload sample file → Extraction pipeline successfully computes & writes indices with no crash.
5. Submit empty input (`" "` or empty string) → Catching `st.error()` is displayed preventing crash.
6. Submit valid query target → Generates non-empty semantic answers returning direct citations inside expanders.
7. System handles massive inputs, unsupported files (`.csv`), gracefully preventing memory spikes.

---

## RUN GUIDE / SETUP

**Step 1:** Generate a clean environment  
```bash
python -m venv venv
```

**Step 2:** Activate workspace context  
```bash
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

**Step 3:** Synchronize environment dependencies  
```bash
pip install -r requirements.txt
```
*(Fix: If pip fails, double check python version >= 3.9 and consider appending `--user` flag).*

**Step 4:** Clone environment templates  
```bash
cp .env.example .env
```
*(You must edit `.env` putting your Google Gemini API key inside `GOOGLE_API_KEY`).*

**Step 5:** Execute safety checks  
```bash
python test_validation.py
```
*(Fix: Ensure API keys are matched to `.env` if Test 2 fails, verify pip packages if Test 1 fails).*

**Step 6:** Launch production UI  
```bash
streamlit run app.py
```

**Step 7:** Open `http://localhost:8501` → Upload `.pdf` file → Enter research prompt → Validate semantic response.
