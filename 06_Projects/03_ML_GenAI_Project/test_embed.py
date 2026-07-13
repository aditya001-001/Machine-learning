import os
import config
from langchain_google_genai import GoogleGenerativeAIEmbeddings

def test_embed():
    print(f"Config Model: {config.EMBEDDING_MODEL}")
    embedder = GoogleGenerativeAIEmbeddings(
        model=config.EMBEDDING_MODEL,
        google_api_key=config.GOOGLE_API_KEY
    )
    res = embedder.embed_query("Hello world")
    print(f"Success! Vector length: {len(res)}")

if __name__ == "__main__":
    test_embed()
