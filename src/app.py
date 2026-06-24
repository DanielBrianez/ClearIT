import streamlit as st
import os
from src.services.ai_agent import gerar_roteiro_ia
from src.services.pdf_maker import gerar_pdf
from src.utils.logger import registrar_log_1a1

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
                    registrar_log_1a1(perfil_lider, nivel_liderado, tempo_casa, perfil_comportamental)
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

# Bloco 2: Governança / Geração de PDF
    st.header("2. Registro Oficial (Ata LGPD)")
    st.info("Insira os nomes reais apenas para gerar o PDF local.")
    
    col_nome1, col_nome2 = st.columns(2)
    with col_nome1: nome_lider = st.text_input("Nome do Líder:")
    with col_nome2: nome_liderado = st.text_input("Nome do Liderado:")
    
    # Se o roteiro já foi gerado e está na memória
    if "roteiro_gerado" in st.session_state:
        roteiro_completo = st.session_state.roteiro_gerado
        
        # ✂️ O Corte Mágico: Separa o texto na tag
        if "--- ATA OFICIAL ---" in roteiro_completo:
            partes = roteiro_completo.split("--- ATA OFICIAL ---")
            texto_para_pdf = partes[1].strip() # Pega só a parte 2 (Resumo + Gamificação)
        else:
            # Caso a IA falhe e não coloque a tag, manda tudo por segurança
            texto_para_pdf = roteiro_completo 
            
        if st.button("📄 Baixar Ata em PDF"):
            if nome_lider and nome_liderado:
                with st.spinner("Gerando PDF seguro..."):
                    # Passamos apenas o texto_para_pdf (sem as dicas do líder)
                    caminho_pdf = gerar_pdf(nome_lider, nome_liderado, texto_para_pdf)
                    
                    with open(caminho_pdf, "rb") as f:
                        st.download_button(
                            label="⬇️ Clique aqui para salvar o PDF",
                            data=f,
                            file_name=f"Ata_1a1_{nome_liderado.replace(' ', '_')}.pdf",
                            mime="application/pdf"
                        )
            else:
                st.warning("⚠️ Preencha os nomes reais do líder e liderado para gerar o documento.")
                
if __name__ == "__main__":
    main()