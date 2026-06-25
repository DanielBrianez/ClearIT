import streamlit as st
import re
from src.components.ui_forms import renderizar_formulario_contexto
from src.services.ai_agent import gerar_roteiro_ia
from src.services.pdf_maker import gerar_pdf
from src.utils.logger import registrar_log_1a1

def main():
    st.set_page_config(page_title="Smart Leading - ClearIT", page_icon="assets/favicon.ico", layout="centered")

    # --- CABEÇALHO COM TOGGLE DE DARK MODE ---
    col_titulo, col_tema = st.columns([4, 1])
    with col_titulo:
         st.title("Smart Leading - ClearIT")
         st.markdown("Preencha o contexto comportamental abaixo para gerar um roteiro seguro e customizado.")
        
    with col_tema:
        st.write("") # Espaço para alinhar verticalmente
        tema_escuro = st.toggle("🌙 Dark Mode")

    # --- INJEÇÃO DE CSS DINÂMICA ---
    with open("assets/style.css", encoding="utf-8") as f:
        css_base = f.read()

    # Se o botão de Dark Mode for ativado, injetamos as variáveis escuras por cima
    css_dark = ""
    if tema_escuro:
        css_dark = """
        .stApp {
            background-color: #0F172A !important; 
            background-image: radial-gradient(#334155 1px, transparent 1px) !important;
        }
        
        /* 1. FORÇA TEXTOS GLOBAIS (Patente Alta com 'body') */
        body, body h1, body h2, body h3, body p, body span, body label, body li, body div[data-testid="stMarkdownContainer"] p { 
            color: #F8FAFC !important; 
        }
        
        /* 2. CORREÇÃO DA CAIXA DE ALERTA (st.info) NO MODO ESCURO */
        body div[data-testid="stNotification"] * {
            color: #F8FAFC !important;
        }

        /* 3. FUNDO DO FORMULÁRIO */
        body div[data-testid="stForm"] {
            background-color: #1E293B !important;
            border-color: #334155 !important;
        }
        
        /* 4. SEÇÃO DA ATA: CORREÇÃO DOS INPUTS DE TEXTO (Dentro e fora do Form) */
        body div.stTextInput input, 
        body div.stTextArea textarea,
        body div.stSelectbox div {
            background-color: #0F172A !important;
            color: #F8FAFC !important;
            border-color: #475569 !important;
            -webkit-text-fill-color: #F8FAFC !important; /* Força cor clara até no Chrome/Edge */
        }

        /* 5. PROTEÇÃO DE CORES DOS BOTÕES (Garante legibilidade dos textos internos) */
        body div[data-testid="stFormSubmitButton"] > button * { color: #2563EB !important; }
        body div[data-testid="stFormSubmitButton"] > button:hover * { color: #FFFFFF !important; }
        body button[kind="primary"] * { color: #FFFFFF !important; }
        body button[disabled] * { color: #94A3B8 !important; }

        /* 6. BALÕES DOS DROPDOWNS E SETINHAS NO MODO ESCURO */
        body div[data-baseweb="select"] * {
            color: #F8FAFC !important;
        }
        
        /* Pinta a setinha de branco no Modo Escuro */
        body div[data-baseweb="select"] svg {
            fill: #F8FAFC !important;
            color: #F8FAFC !important;
        }
        
        body div[data-baseweb="popover"] * {
            color: #F8FAFC !important;
        }
        
        body div[data-baseweb="popover"] > div,
        body div[data-baseweb="popover"] ul {
            background-color: #1E293B !important;
            border-color: #334155 !important;
        }
        
        body li[role="option"] {
            background-color: #1E293B !important;
        }
        
        body li[role="option"]:hover,
        body li[role="option"]:hover *,
        body li[role="option"][aria-selected="true"],
        body li[role="option"][aria-selected="true"] * {
            background-color: #334155 !important;
            color: #60A5FA !important;
        }
        """

    st.markdown(f"<style>{css_base}\n{css_dark}</style>", unsafe_allow_html=True)
 
 # --- FUNÇÃO DE TRAVA DO BOTÃO ---

    def travar_tela():

        st.session_state.is_generating = True



    # Garante que as variáveis existam quando o app iniciar

    if "is_generating" not in st.session_state:

        st.session_state.is_generating = False



    # --- FUNÇÃO DE TRAVA DO BOTÃO ---

    def travar_tela():

        st.session_state.is_generating = True



    # 📩 CAIXA DE CORREIO: Exibe alertas salvos se o usuário clicou com a pauta vazia

    if "alerta_form" in st.session_state:

        st.warning(st.session_state.alerta_form)

        del st.session_state.alerta_form # Apaga a mensagem logo após mostrar



    # 🛡️ O FORMULÁRIO (Trava a tela de recarregar à toa)

    with st.form("form_contexto"):

        perfil_lider, nivel_liderado, tempo_casa, perfil_comportamental, entregas_recentes, acordos = renderizar_formulario_contexto(

            disabled=st.session_state.is_generating

        )

       

        gerar_btn = st.form_submit_button(

            "Gerando Roteiro... Aguarde ⏳" if st.session_state.is_generating else "Gerar Roteiro Personalizado",

            use_container_width=True,

            disabled=st.session_state.is_generating,

            on_click=travar_tela

        )

   

    # --- MOTOR DE GERAÇÃO COM DESTRAVAMENTO AUTOMÁTICO ---

    if st.session_state.is_generating:

        if entregas_recentes.strip(): # Verifica se não está vazio (ignora espaços em branco)

            with st.spinner("A IA está analisando os perfis e criando o roteiro..."):

                try:

                    roteiro = gerar_roteiro_ia(perfil_lider, nivel_liderado, tempo_casa, perfil_comportamental, entregas_recentes, acordos)

                    st.session_state.roteiro_gerado = roteiro

                    registrar_log_1a1(perfil_lider, nivel_liderado, tempo_casa, perfil_comportamental)

                except Exception as e:

                    st.error(f"Erro na API do Gemini: {e}")

                finally:

                    st.session_state.is_generating = False

                    st.rerun()

        else:

            # SALVA A MENSAGEM, DESTRAVA E RECARREGA A TELA

            st.session_state.alerta_form = "⚠️ Preencha pelo menos o resumo das entregas/gaps para a IA ter contexto."

            st.session_state.is_generating = False

            st.rerun()

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

        palavras_proibidas = [
            "ATA OFICIAL DE", "Empresa: Clear", "Data: [", "Horário: [", 
            "Líder: [", "Liderado(a):", "Cargo do", "Participantes:"
        ]
        linhas_limpas = []
        for linha in texto_para_pdf.split('\n'):
            # Se a linha NÃO começa com as palavras proibidas, a gente guarda
            if not any(linha.strip().startswith(sujeira) for sujeira in palavras_proibidas):
                linhas_limpas.append(linha)
                
        texto_para_pdf = '\n'.join(linhas_limpas)

        texto_para_pdf = re.sub(r'\n{3,}', '\n\n', texto_para_pdf).strip()
            
        # 💡 A MÁGICA DO BOTÃO DESATIVADO (Disabled)
        nomes_preenchidos = bool(nome_lider and nome_liderado)
        
        if nomes_preenchidos:
            caminho_pdf = gerar_pdf(nome_lider, nome_liderado, texto_para_pdf)
            with open(caminho_pdf, "rb") as f:
                pdf_bytes = f.read()
        else:
            pdf_bytes = b"" # Arquivo fantasma apenas para o botão existir na tela
            
        st.download_button(
            label="Baixar Ata Oficial em PDF",
            data=pdf_bytes,
            file_name=f"Ata_1a1_{nome_liderado.replace(' ', '_')}.pdf" if nomes_preenchidos else "Ata_Pendente.pdf",
            mime="application/pdf",
            use_container_width=True,
            type="primary",
            disabled=not nomes_preenchidos 
        )
        
        if not nomes_preenchidos:
            st.warning("Preencha os nomes acima para habilitar o botão de download.")

if __name__ == "__main__":
    main()