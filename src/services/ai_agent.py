import google.generativeai as genai
from src.config import configurar_gemini

# Inicializa a configuração
configurar_gemini()
modelo = genai.GenerativeModel('gemini-3.5-flash')

def gerar_roteiro_ia(perfil_lider, nivel_liderado, tempo_casa, perfil_comportamental, entregas_recentes, acordos=""):
    
    prompt = f"""
    Você é um Mentor Executivo e parceiro de RH estratégico da empresa Clear IT.
    Seu objetivo é preparar o líder para uma reunião de 1:1 e, ao mesmo tempo, redigir a Ata Oficial desse encontro.
    
    CONTEXTO DA REUNIÃO:
    - Perfil do Líder (quem vai conduzir): {perfil_lider}
    - Senioridade do Liderado: {nivel_liderado}
    - Tempo de Casa: {tempo_casa}
    - Perfil Comportamental: {perfil_comportamental}
    - Entregas/Gaps (Pauta): {entregas_recentes}
    - Acordos Pós-reunião: {acordos}

    REGRAS DE TOM DE VOZ PARA O LÍDER (CRÍTICO):
    - Se o líder for "Técnico": Use linguagem ultra-direta, sem jargão de RH, foque em dados.
    - Se o líder for "Em Transição": Dê dicas de empatia e como falar as partes difíceis.
    - Se o líder for "Engajado": Foque em estruturar o tempo e os próximos passos práticos.

    ESTRUTURA OBRIGATÓRIA DA SUA RESPOSTA:
    Você deve dividir sua resposta em duas partes, separadas EXATAMENTE por esta tag: --- ATA OFICIAL ---

    PARTE 1 (Acima da tag): ROTEIRO DO LÍDER (Confidencial)
    - Crie o roteiro da 1:1 dividido em: Abertura, Desenvolvimento da Pauta e Próximos Passos.
    - Dê dicas de postura e correções de tom (ex: como falar de forma menos agressiva).
    - Sugira perguntas focadas no perfil do liderado.

    --- ATA OFICIAL ---

    PARTE 2 (Abaixo da tag): RESUMO DO ALINHAMENTO (Para o PDF)
    - Escreva de forma formal, impessoal e corporativa (este texto irá para o RH).
    - Comece OBRIGATORIAMENTE com: "Nesta reunião de alinhamento, conversamos sobre os seguintes tópicos..."
    - Faça o resumo dos pontos abordados e destaque os acordos firmados.
    - Crie o bloco de GAMIFICAÇÃO contendo:
       1. Um Badge de reconhecimento (ex: 🏆 Badge de Resiliência) baseado nas entregas.
       2. +XP (atribua uma pontuação de 50 a 500 XP justificando o motivo).
       3. Uma Missão clara para a próxima quinzena.
    """
    
    resposta = modelo.generate_content(prompt)
    return resposta.text