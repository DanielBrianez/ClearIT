import google.generativeai as genai
from src.config import configurar_gemini

# Inicializa a configuração
configurar_gemini()
modelo = genai.GenerativeModel('gemini-3.5-flash')

def gerar_roteiro_ia(perfil_lider, nivel_liderado, tempo_casa, perfil_comportamental, entregas_recentes, acordos=""):
    
    prompt = f"""
    Aja como um Mentor Executivo e de RH da empresa Clear IT.
    
    CONTEXTO DA REUNIÃO:
    - Perfil do Líder (quem vai ler isso): {perfil_lider}
    - Senioridade do Liderado: {nivel_liderado}
    - Tempo de Casa: {tempo_casa}
    - Perfil Comportamental: {perfil_comportamental}
    - Entregas/Gaps (Pauta): {entregas_recentes}
    - Acordos Pós-reunião (se houver): {acordos}

    REGRAS DE TOM DE VOZ (CRÍTICO):
    Se o líder for "Técnico", use linguagem ultra-direta, sem jargão de RH, foque em dados.
    Se o líder for "Em Transição", dê dicas de empatia e como falar as partes difíceis.
    Se o líder for "Engajado", foque em estruturar o tempo e os próximos passos práticos.

    INSTRUÇÕES DE SAÍDA:
    1. Crie um roteiro de 1:1 dividido em: Abertura, Desenvolvimento da Pauta e Próximos Passos.
    2. Crie um bloco de "GAMIFICAÇÃO" contendo:
       - 1 Badge de reconhecimento (ex: 🏆 Badge de Resiliência) baseado nas entregas.
       - +XP (atribua uma pontuação de 50 a 500 XP justificando o motivo).
       - 1 Missão clara para a próxima quinzena.
    """
    
    resposta = modelo.generate_content(prompt)
    return resposta.text