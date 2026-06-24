import google.generativeai as genai
from src.config import configurar_gemini

# Configura a chave
configurar_gemini()

print("Buscando modelos disponíveis para a sua chave...")
print("-" * 40)

# Lista todos os modelos disponíveis
for m in genai.list_models():
    # Filtra apenas os modelos que suportam geração de texto
    if 'generateContent' in m.supported_generation_methods:
        print(f"✅ Modelo suportado encontrado: {m.name}")