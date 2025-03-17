
import google.generativeai as genai

genai.configure(api_key="")

def list_models():
    models = genai.list_models()
    for model in models:
        print(model.name)

if __name__ == "__main__":
    list_models()
