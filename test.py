import google.generativeai as genai

genai.configure(api_key="AIzaSyDEjwjM2qcc5zxuZt_r4tDkENCNrWYT5lM")

models = genai.list_models()
print("Available models:")
for model in models:
    print(model.name, "supports", model.supported_generation_methods)
