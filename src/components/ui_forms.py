import streamlit as st

def renderizar_formulario_contexto(disabled=False):
    """Renderiza os campos de entrada e retorna as variáveis preenchidas."""
    
    st.header("1. Contexto da Reunião (Variáveis)")
    
    perfil_lider = st.selectbox(
        "Qual o seu perfil de liderança hoje?", 
        ["Técnico (Focado em entregas e dados)", 
         "Em Transição (Novo na liderança, precisa de apoio)", 
         "Engajado (Focado em carreira e desenvolvimento)"],
        disabled=disabled
    )
    
    # Nuggets de encorajamento e dicas de postura baseados no perfil do líder
    if "Técnico" in perfil_lider:
        st.info("💡 **Dica de Postura (Líder Técnico):** Evite jargões excessivos de RH. Foque em dados objetivos, mas lembre-se: a gestão de pessoas não é um 'trabalho invisível' — ela é o que sustenta a performance técnica do time!")
        st.caption("✨ *Nugget:* Você não precisa ter todas as respostas. Seu papel é direcionar e dar suporte para o desenvolvimento.")
    elif "Transição" in perfil_lider:
        st.info("💡 **Dica de Postura (Líder em Transição):** Conversas complexas exigem inteligência emocional. Use empatia, ouça ativamente e encare os conflitos como oportunidades de alinhamento.")
        st.caption("✨ *Nugget:* A consistência nos ritos de 1:1 constrói a segurança psicológica e a confiança na sua liderança.")
    elif "Engajado" in perfil_lider:
        st.info("💡 **Dica de Postura (Líder Engajado):** Mantenha o foco em carreira. Organize a pauta dividindo o tempo entre sentimentos, conquistas recentes, desafios e os acordos práticos de desenvolvimento.")
        st.caption("✨ *Nugget:* Seu comprometimento com as pessoas inspira o time. Mantenha as atas ativas para evitar desalinhamentos!")
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        nivel_liderado = st.selectbox("Senioridade do Liderado:", ["Estagiário", "Júnior", "Pleno", "Sênior", "Especialista"],
        disabled=disabled)
    with col2:
        tempo_casa = st.selectbox("Tempo de Empresa:", ["Menos de 6 meses", "6 meses a 1 ano", "1 a 3 anos", "Mais de 3 anos"], disabled=disabled)
    with col3:
        perfil_comportamental = st.selectbox("Perfil Comportamental:", ["Analítico", "Comunicador", "Executor", "Planejador"], disabled=disabled)
        
    entregas_recentes = st.text_area(
        "Resumo das últimas entregas, gaps ou comportamentos (Pauta):", 
        placeholder="Ex: Entregou o projeto X com atraso, mas ajudou o time novo a se adaptar...", disabled=disabled
    )
    
    acordos = st.text_area(
        "Acordos firmados ou próximos passos (Opcional):", 
        placeholder="Ex: Finalizar a certificação da AWS até o final do trimestre...",
        disabled=disabled
    )
    
    return perfil_lider, nivel_liderado, tempo_casa, perfil_comportamental, entregas_recentes, acordos