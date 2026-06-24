import streamlit as st

from src.components.ui_forms import renderizar_formulario_contexto
from src.services.ai_agent import gerar_roteiro_ia
from src.services.pdf_maker import gerar_pdf
from src.utils.logger import registrar_log_1a1

def main():
    st.set_page_config(page_title="Clear IT - Assistente de 1:1", page_icon="🧠", layout="centered")
    
    st.title("🧠 Assistente de Liderança - Clear IT")
    st.markdown("Preencha o contexto comportamental abaixo para gerar um roteiro seguro e customizado.")
    
    # 🛡️ O FORMULÁRIO (Trava a tela de recarregar à toa)
    with st.form("form_contexto"):
        perfil_lider, nivel_liderado, tempo_casa, perfil_comportamental, entregas_recentes, acordos = renderizar_formulario_contexto()
        
        # O botão de gerar agora faz parte do formulário
        gerar_btn = st.form_submit_button("🧠 Gerar Roteiro Personalizado", use_container_width=True)
    
    if gerar_btn:
        if entregas_recentes:
            # DICA: Quando o st.spinner roda, o Streamlit automaticamente mostra um 
            # botão nativo de "STOP" (Parar) no canto superior direito da tela!
            with st.spinner("A IA está analisando os perfis e criando o roteiro..."):
                try:
                    roteiro = gerar_roteiro_ia(perfil_lider, nivel_liderado, tempo_casa, perfil_comportamental, entregas_recentes, acordos)
                    st.session_state.roteiro_gerado = roteiro
                    registrar_log_1a1(perfil_lider, nivel_liderado, tempo_casa, perfil_comportamental)
                except Exception as e:
                    st.error(f"Erro na API do Gemini: {e}")
        else:
            st.warning("⚠️ Preencha pelo menos o resumo das entregas/gaps para a IA ter contexto.")

    # 3. Exibição em Tela 
    if "roteiro_gerado" in st.session_state:
        st.markdown("---")
        st.subheader("💡 Seu Roteiro de Apoio (Confidencial)")
        st.markdown(st.session_state.roteiro_gerado)
        
        st.markdown("---")
        
        # 4. Bloco de Governança e PDF
        st.header("2. Registro Oficial (Ata LGPD)")
        st.info("Insira os nomes reais abaixo. Eles não vão para a IA, apenas para o PDF local.")
        
        col_nome1, col_nome2 = st.columns(2)
        with col_nome1: nome_lider = st.text_input("Nome do Líder:")
        with col_nome2: nome_liderado = st.text_input("Nome do Liderado:")
        
        roteiro_completo = st.session_state.roteiro_gerado
        
        if "--- ATA OFICIAL ---" in roteiro_completo:
            partes = roteiro_completo.split("--- ATA OFICIAL ---")
            texto_para_pdf = partes[1].strip()
        else:
            texto_para_pdf = roteiro_completo 
            
        # 💡 A MÁGICA DO BOTÃO DESATIVADO (Disabled)
        nomes_preenchidos = bool(nome_lider and nome_liderado)
        
        if nomes_preenchidos:
            caminho_pdf = gerar_pdf(nome_lider, nome_liderado, texto_para_pdf)
            with open(caminho_pdf, "rb") as f:
                pdf_bytes = f.read()
        else:
            pdf_bytes = b"" # Arquivo fantasma apenas para o botão existir na tela
            
        st.download_button(
            label="⬇️ Baixar Ata Oficial em PDF",
            data=pdf_bytes,
            file_name=f"Ata_1a1_{nome_liderado.replace(' ', '_')}.pdf" if nomes_preenchidos else "Ata_Pendente.pdf",
            mime="application/pdf",
            use_container_width=True,
            type="primary",
            disabled=not nomes_preenchidos # Se falso, o botão fica cinza e inclicável!
        )
        
        if not nomes_preenchidos:
            st.warning("⚠️ Preencha os nomes acima para habilitar o botão de download.")

if __name__ == "__main__":
    main()