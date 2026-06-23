import streamlit as st
import os
from src.services.ai_agent import gerar_roteiro_ia
from src.services.pdf_maker import gerar_pdf

st.set_page_config(page_title="Clear IT - Assistente de Liderança", page_icon="🤝", layout="centered")

# Variáveis de Estado para não perder os dados quando a tela atualizar
if "roteiro_gerado" not in st.session_state:
    st.session_state.roteiro_gerado = ""

def main():
    st.title("🤝 Assistente de 1:1 e Feedback")
    st.markdown("Prepare suas reuniões de forma rápida, estruturada e 100% alinhada à LGPD.")
    
    # Aviso de Chave de API
    if not os.getenv("GEMINI_API_KEY"):
        st.error("⚠️ Atenção: A variável GEMINI_API_KEY não foi encontrada no ambiente.")
    
    st.divider()

    # Bloco 1: Preparação
    st.header("1. O Contexto da Reunião")
    perfil_lider = st.selectbox("Seu Perfil (Líder)", ["Líder Técnico", "Líder em Transição", "Líder Engajado"])
    
    col1, col2, col3 = st.columns(3)
    with col1: nivel_liderado = st.selectbox("Senioridade", ["Estagiário", "Júnior", "Pleno", "Sênior"])
    with col2: tempo_casa = st.selectbox("Tempo de Casa", ["< 6 meses", "6 a 12 meses", "> 1 ano"])
    with col3: perfil_comportamental = st.selectbox("Perfil (Clear IT)", ["Analítico", "Comunicador", "Executor", "Planejador"])

    entregas_recentes = st.text_area("Resumo para a Pauta (Entregas ou Gaps):", placeholder="Ex: Entregou no prazo, mas...")

    if st.button("🧠 Gerar Roteiro Personalizado", use_container_width=True):
        if entregas_recentes:
            with st.spinner("A IA está analisando os perfis e criando o roteiro..."):
                try:
                    roteiro = gerar_roteiro_ia(perfil_lider, nivel_liderado, tempo_casa, perfil_comportamental, entregas_recentes)
                    st.session_state.roteiro_gerado = roteiro
                except Exception as e:
                    st.error(f"Erro na API do Gemini: {e}")
        else:
            st.warning("⚠️ Preencha o resumo da pauta para a IA ter contexto.")

    # Exibe o roteiro se ele existir na sessão
    if st.session_state.roteiro_gerado:
        st.success("Roteiro Gerado com Sucesso!")
        with st.expander("Visualizar Roteiro e Gamificação", expanded=True):
            st.markdown(st.session_state.roteiro_gerado)

    st.divider()

    # Bloco 2: Governança / Geração de PDF (Dados Reais entram apenas aqui)
    st.header("2. Registro Oficial (Ata LGPD)")
    st.info("Insira os nomes reais apenas para gerar o PDF local. Estes dados não são enviados para a IA.")
    
    col_nome1, col_nome2 = st.columns(2)
    with col_nome1: nome_lider = st.text_input("Nome do Líder:")
    with col_nome2: nome_liderado = st.text_input("Nome do Liderado:")

    if st.session_state.roteiro_gerado and nome_lider and nome_liderado:
        pdf_bytes = gerar_pdf(st.session_state.roteiro_gerado, nome_lider, nome_liderado)
        
        st.download_button(
            label="📄 Baixar Ata Oficial (PDF)",
            data=pdf_bytes,
            file_name=f"Ata_1a1_{nome_liderado.replace(' ', '_')}.pdf",
            mime="application/pdf",
            type="primary",
            use_container_width=True
        )
    elif not st.session_state.roteiro_gerado:
        st.warning("Gere um roteiro primeiro para liberar a Ata em PDF.")

if __name__ == "__main__":
    main()