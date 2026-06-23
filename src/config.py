import os
import google.generativeai as genai

def carregar_env_nativo():
    """Lê o arquivo .env na raiz do projeto e injeta nas variáveis de ambiente"""
    # Descobre onde o config.py está e aponta para o .env que está uma pasta acima (raiz)
    caminho_env = os.path.join(os.path.dirname(__file__), "..", ".env")
    
    if os.path.exists(caminho_env):
        with open(caminho_env, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                # Ignora linhas vazias ou comentários
                if linha and not linha.startswith("#") and "=" in linha:
                    chave, valor = linha.split("=", 1)
                    # Limpa espaços e aspas extras se houver
                    os.environ[chave.strip()] = valor.strip().strip('"').strip("'")

def configurar_gemini():
    # Carrega o arquivo .env antes de buscar a chave
    carregar_env_nativo()
    
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError(
            "🛑 Erro: GEMINI_API_KEY não encontrada no arquivo .env.\n"
            "Verifique se o arquivo .env está na raiz do projeto com o formato: GEMINI_API_KEY=sua_chave"
        )
    
    genai.configure(api_key=api_key)