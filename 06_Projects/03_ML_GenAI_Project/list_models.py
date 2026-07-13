import config
import google.generativeai as genai

def show_models():
    genai.configure(api_key=config.GOOGLE_API_KEY)
    print("MATCHING MODELS:")
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods and 'gemini' in m.name:
            print(m.name)
            
if __name__ == "__main__":
    show_models()
