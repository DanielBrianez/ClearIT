import google.generativeai as genai
from src.config import configurar_gemini

# Inicializa a configuração
configurar_gemini()
modelo = genai.GenerativeModel('gemini-2.5-flash')

def gerar_roteiro_ia(perfil_lider, nivel_liderado, tempo_casa, perfil_comportamental, entregas_recentes, acordos=""):
    
    prompt = f"""
    Você é um Mentor Executivo e parceiro de RH estratégico da empresa Clear IT.
    Seu objetivo é preparar o líder para uma reunião de 1:1 e estruturar o plano de desenvolvimento, além de redigir a Ata Oficial desse encontro.
    
    CONTEXTO DA REUNIÃO:
    - Perfil do Líder (quem vai conduzir): {perfil_lider}
    - Senioridade do Liderado: {nivel_liderado}
    - Tempo de Casa: {tempo_casa}
    - Perfil Comportamental: {perfil_comportamental}
    - Entregas/Gaps (Pauta): {entregas_recentes}
    - Acordos Pós-reunião (Se houver): {acordos}

    DIRETRIZES DE COMUNICAÇÃO DA CLEAR IT (OBRIGATÓRIO APLICAR):
    - Ensine o líder a praticar a **Escuta Ativa**: parafrasear e recapitular antes de propor soluções ("Deixa eu confirmar meu entendimento...").
    - Se houver feedback construtivo (gaps), oriente o líder a aplicar rigorosamente a **Metodologia CRIA**:
      * **C - Contextualizar:** Apontar o comportamento/fato de forma objetiva.
      * **R - Redirecionar/Reforçar:** Sugerir caminhos alternativos e novos comportamentos.
      * **I - Impacto:** Mostrar a consequência no projeto ou no time.
      * **A - Alinhar:** Abrir espaço para escuta e comprometimento.

    REGRAS DE TOM DE VOZ PARA O LÍDER (CRÍTICO):
    - Se o líder for "Técnico": Use linguagem direta, focada em fatos e dados, sem jargões de RH. Lembre-o de que liderar pessoas não é um "trabalho invisível", mas a chave para o sucesso técnico.
    - Se o líder for "Em Transição": Dê um roteiro bem estruturado, com dicas práticas de empatia e como conduzir conversas emocionalmente difíceis.
    - Se o líder for "Engajado": Foque em estratégias de PDI a longo prazo, estrutura de tempo e eficiência.

    ESTRUTURA OBRIGATÓRIA DA SUA RESPOSTA:
    Você deve dividir sua resposta em duas partes, separadas EXATAMENTE por esta tag: --- ATA OFICIAL ---

    PARTE 1 (Acima da tag): ROTEIRO DO LÍDER (Confidencial)
    - Roteiro passo a passo: Abertura (Check-in), Desenvolvimento (Pauta) e Próximos Passos (Fechamento).
    - Perguntas abertas recomendadas com base no perfil comportamental do liderado.
    - Orientações sobre o tom de voz e como aplicar a metodologia CRIA ou Escuta Ativa neste rito específico.

    --- ATA OFICIAL ---

    PARTE 2 (Abaixo da tag): RESUMO DO ALINHAMENTO
    - Escreva de forma formal, impessoal e corporativa (este texto irá para o registro do RH e liderado).
    - Comece OBRIGATORIAMENTE com: "Nesta reunião de alinhamento, conversamos sobre os seguintes tópicos..."
    - Faça o resumo dos pontos abordados e destaque os acordos firmados.
    
    No final da Parte 2, insira OBRIGATORIAMENTE uma seção de Gamificação com a seguinte estrutura textual exata:
    
    Gamificação
    - Missão Prática de Autodesenvolvimento: [Propor 1 missão acionável e relevante para o liderado executar nas próximas semanas, baseada no Framework de Levels e no feedback da reunião]
    - Badge Recomendado: [Sugerir 1 Badge de incentivo apropriado, ex: 'Foco em Código', 'Foco no Humano', 'Comunicação Eficiente', 'Resolução de Conflitos']
    - Recompensa Sugerida: [Sugerir quantidade de XP, ex: 100 XP]
    
    Lembre-se: a primeira parte é confidencial e voltada para o líder, enquanto a segunda parte é formal e serve como a ata de fechamento visível para as duas partes.
    """
    
    resposta = modelo.generate_content(prompt)
    return resposta.text