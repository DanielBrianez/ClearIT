import streamlit as st
import re
import base64
from src.components.ui_forms import renderizar_formulario_contexto
from src.services.ai_agent import gerar_roteiro_ia
from src.services.pdf_maker import gerar_pdf
from src.utils.logger import registrar_log_1a1

# ==========================================================
# 📊 BANCO DE DADOS LOCAL (Alimenta o Front-end sem ir para a IA)
# ==========================================================
DB_LIDERES = ["Daniel Nascimento", "Bruna Silva", "Rodrigo Costa", "Amanda Souza"]
DB_LIDERADOS = ["Paulo Augusto", "Lucas Silva", "Mariana Santos", "Pedro Alves", "Julia Ribeiro", "Gustavo Lima", "Beatriz Reis"]

def main():
    st.set_page_config(page_title="Smart Leading - ClearIT", page_icon="assets/favicon.ico", layout="centered")

    # --- GERENCIAMENTO DE ESTADO GLOBAIS ---
    if "is_generating" not in st.session_state:
        st.session_state.is_generating = False

    # Inicializa o Ranking com dados fictícios para a tela não nascer vazia
    if "ranking" not in st.session_state:
        st.session_state.ranking = {
            "Daniel Nascimento": 14,
            "Bruna Silva": 9,
            "Rodrigo Costa": 7,
            "Amanda Souza": 4
        }

    # --- 1. CABEÇALHO (LOGO CLICÁVEL E DARK MODE) NO TOPO ABSOLUTO ---
    col_logo, col_tema = st.columns([4, 1])

    def get_base64_image(caminho_imagem):
        with open(caminho_imagem, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
        
    def computar_pontos_lider(nome_lider):
        """Disparada na hora exata do download do PDF: soma +100 XP pro Líder"""
        st.session_state.ranking[nome_lider] = st.session_state.ranking.get(nome_lider, 0) + 1
        st.session_state.lider_ganhou_ponto = True
        
    with col_logo:
        # Aponte para o nome exato da imagem que você salvou na pasta assets!
        img_base64 = get_base64_image("assets/logo.png") 
        
        st.markdown(f"""
            <a href="/" target="_self" style="text-decoration: none;">
                <img src="data:image/png;base64,{img_base64}" width="160" alt="Logo Clear IT" style="margin-top: 5px;">
            </a>
        """, unsafe_allow_html=True)

        
        
    with col_tema:
        st.write("") # Espaço para alinhar verticalmente
        tema_escuro = st.toggle("🌙 Dark Mode")

    # --- 2. INJEÇÃO DE CSS DINÂMICA ---
    with open("assets/style.css", encoding="utf-8") as f:
        css_base = f.read()

    css_dark = ""
    if tema_escuro:
        css_dark = """
        .stApp {
            background-color: #0F172A !important; 
            background-image: radial-gradient(#334155 1px, transparent 1px) !important;
        }
        
        body, body h1, body h2, body h3, body p, body span, body label, body li, body div[data-testid="stMarkdownContainer"] p { 
            color: #F8FAFC !important; 
        }
        
        body div[data-testid="stNotification"] * {
            color: #F8FAFC !important;
        }

        body div[data-testid="stForm"] {
            background-color: #1E293B !important;
            border-color: #334155 !important;
        }
        
        body div.stTextInput input, 
        body div.stTextArea textarea,
        body div.stSelectbox div {
            background-color: #0F172A !important;
            color: #F8FAFC !important;
            border-color: #475569 !important;
            -webkit-text-fill-color: #F8FAFC !important;
        }

        body div[data-testid="stFormSubmitButton"] > button * { color: #2563EB !important; }
        body div[data-testid="stFormSubmitButton"] > button:hover * { color: #FFFFFF !important; }
        body button[kind="primary"] * { color: #FFFFFF !important; }
        body button[disabled] * { color: #94A3B8 !important; }

        body div[data-baseweb="select"] * {
            color: #F8FAFC !important;
        }
        
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

        /* CARDS E FOTOS NO MODO ESCURO */
        body div[data-testid="stVerticalBlockBorderWrapper"] {
            background-color: #1E293B !important;
            border-color: #334155 !important;
            box-shadow: none !important;
        }
        
        body div[data-testid="stImage"] img {
            border-color: #334155 !important;
        }
        """

    st.markdown(f"<style>{css_base}\n{css_dark}</style>", unsafe_allow_html=True)

    # --- 3. GERENCIAMENTO DE ESTADO E TRAVAS ---
    if "is_generating" not in st.session_state:
        st.session_state.is_generating = False

    def travar_tela():
        st.session_state.is_generating = True

    # ==========================================================
    # 4. NAVBAR: ABAS DE NAVEGAÇÃO (Agora grudadinhas no topo!)
    # ==========================================================
    tab_home, tab_ranking, tab_time, tab_sobre = st.tabs(["🏠 Home", "🏆 Ranking de Líderes", "👥 Nosso Time", "ℹ️ Sobre o Projeto"])

    # ----------------------------------------------------------
    # ABA 1: HOME (O aplicativo principal inteiro mora aqui dentro)
    # ----------------------------------------------------------
    with tab_home:
        
        # 👉 Movemos o Título Gigante para DENTRO da aba Home!
        st.title("Smart Leading - ClearIT")
        st.markdown("Preencha o contexto comportamental abaixo para gerar um roteiro seguro e customizado.")
        st.markdown("<br>", unsafe_allow_html=True) # Espaçamento para o form respirar

        # Celebração de pontos do Líder
        if "lider_ganhou_ponto" in st.session_state and st.session_state.lider_ganhou_ponto:
            st.balloons()
            st.toast("🎯 Sensacional! +1 sessão computada no seu Ranking de Líderes!", icon="🔥")
            st.session_state.lider_ganhou_ponto = False

        if "alerta_form" in st.session_state:
            st.warning(st.session_state.alerta_form)
            del st.session_state.alerta_form

        # Exibe alertas na aba Home
        if "alerta_form" in st.session_state:
            st.warning(st.session_state.alerta_form)
            del st.session_state.alerta_form

        # O Formulário
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
        
        # Motor de Geração
        if st.session_state.is_generating:
            if entregas_recentes.strip():
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
                st.session_state.alerta_form = "⚠️ Preencha pelo menos o resumo das entregas/gaps para a IA ter contexto."
                st.session_state.is_generating = False
                st.rerun()

        # Exibição em Tela e Gerador de PDF
        if "roteiro_gerado" in st.session_state:
            st.markdown("---")
            st.subheader("💡 Seu Roteiro de Apoio (Confidencial)")
            st.markdown(st.session_state.roteiro_gerado)
            
            st.markdown("---")
            
            st.header("2. Registro Oficial (Ata LGPD)")
            st.info("Insira os nomes reais abaixo. Eles não vão para a IA, apenas para o PDF local.")
            
            col_nome1, col_nome2 = st.columns(2)
            with col_nome1:nome_lider = st.selectbox("Identifique-se (Líder):", [""] + DB_LIDERES)
            with col_nome2:nome_liderado = st.selectbox("Selecione o Liderado:", [""] + DB_LIDERADOS)
            
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
                if not any(linha.strip().startswith(sujeira) for sujeira in palavras_proibidas):
                    linhas_limpas.append(linha)
                    
            texto_para_pdf = '\n'.join(linhas_limpas)
            texto_para_pdf = re.sub(r'\n{3,}', '\n\n', texto_para_pdf).strip()
                
            nomes_preenchidos = bool(nome_lider and nome_liderado)
            
            if nomes_preenchidos:
                caminho_pdf = gerar_pdf(nome_lider, nome_liderado, texto_para_pdf)
                with open(caminho_pdf, "rb") as f:
                    pdf_bytes = f.read()
            else:
                pdf_bytes = b"" 
                
            # O Botão de Download agora chama o callback de pontos do Líder selecionado!
            st.download_button(
                label="Baixar Ata Oficial em PDF & Computar Pontos",
                data=pdf_bytes,
                file_name=f"Ata_1a1_{nome_liderado.replace(' ', '_')}.pdf" if nomes_preenchidos else "Ata_Pendente.pdf",
                mime="application/pdf",
                use_container_width=True,
                type="primary",
                disabled=not nomes_preenchidos,
                on_click=computar_pontos_lider,
                args=(nome_lider,) # Passa o nome do líder atual como argumento!
            )
            
            if not nomes_preenchidos:
                st.warning("Selecione o seu nome e o do colaborador nos dropdowns acima para liberar o download e pontuar.")

    # ----------------------------------------------------------
    # 🏆 ABA 2: RANKING DE LÍDERES (Nova Seção Gamificada)
    # ----------------------------------------------------------
    with tab_ranking:
        st.header("🏆 Liga de Líderes Clear IT")
        st.markdown("Quem lidera com clareza vai mais longe. Veja os gestores mais engajados nos ritos de 1:1:")
        st.markdown("<br>", unsafe_allow_html=True)

        # Ordena o ranking do maior para o menor
        ranking_ordenado = sorted(st.session_state.ranking.items(), key=lambda x: x[1], reverse=True)

        # Renderiza os cards de colocação com medalhas estilizadas
        for posicao, (lider, sessoes) in enumerate(ranking_ordenado, start=1):
            medalha = "🥇" if posicao == 1 else "🥈" if posicao == 2 else "🥉" if posicao == 3 else "💼"
            
            with st.container(border=True):
                col_pos, col_nome, col_pts = st.columns([1, 4, 2])
                with col_pos:
                    st.subheader(f"{medalha} {posicao}º")
                with col_nome:
                    st.markdown(f"**{lider}**")
                    st.caption("Liderança Estratégica — Clear IT")
                with col_pts:
                    st.markdown(f"🎯 **{sessoes} reuniões**")
                    # Sistema simples de XP fictício baseado nas reuniões (ex: cada reunião vale 100 XP)
                    st.caption(f"{sessoes * 100} total XP")

    # ----------------------------------------------------------
    # ABA 2: NOSSO TIME (Cards com Fotos)
    # ----------------------------------------------------------
    with tab_time:
        st.header("Conheça Nosso Time")
        st.markdown("As mentes por trás do desenvolvimento do Assistente de Liderança Clear IT.")
        st.markdown("<br>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        with col1:
            with st.container(border=True):
                st.image("https://ui-avatars.com/api/?name=Daniel+Nascimento&background=2563EB&color=fff&rounded=true&size=128", width=70)
                st.markdown("**Daniel Nascimento**")
                st.markdown("Tech Lead & Fullstack Dev")
        with col2:
            with st.container(border=True):
                st.image("https://ui-avatars.com/api/?name=Membro+Dois&background=2563EB&color=fff&rounded=true&size=128", width=70)
                st.markdown("**Nome do Membro 2**")
                st.markdown("Product Owner / Negócios")
        with col3:
            with st.container(border=True):
                st.image("https://ui-avatars.com/api/?name=Membro+Tres&background=2563EB&color=fff&rounded=true&size=128", width=70)
                st.markdown("**Nome do Membro 3**")
                st.markdown("Especialista em RH")

        _, col4, col5, _ = st.columns([1, 2, 2, 1])
        with col4:
            with st.container(border=True):
                st.image("https://ui-avatars.com/api/?name=Membro+Quatro&background=2563EB&color=fff&rounded=true&size=128", width=70)
                st.markdown("**Nome do Membro 4**")
                st.markdown("Engenheiro de IA (Prompt)")
        with col5:
            with st.container(border=True):
                st.image("https://ui-avatars.com/api/?name=Membro+Cinco&background=2563EB&color=fff&rounded=true&size=128", width=70)
                st.markdown("**Nome do Membro 5**")
                st.markdown("QA & UX Design")

    # ----------------------------------------------------------
    # ABA 3: SOBRE O PROJETO
    # ----------------------------------------------------------
    with tab_sobre:
        st.header("Sobre o Projeto")
        
        st.markdown("""
        ### 🎯 O Desafio
        Na **Clear IT**, identificamos que ritos fundamentais de gestão, como as reuniões de 1:1, sofriam com a falta de tempo dos líderes para planejamento e com a ausência de uma governança padronizada. Isso resultava em feedbacks burocráticos e desalinhamento de expectativas.

        ### 💡 A Solução
        Desenvolvemos o **Assistente de Liderança Clear IT**, uma plataforma focada no empoderamento do gestor através de Inteligência Artificial. Cruzando o perfil do líder e do liderado, o sistema:
        * Reduz a carga cognitiva na elaboração de pautas.
        * Gera roteiros empáticos e gamificados (com atribuição de XP e Badges).
        * Registra os acordos em uma Ata Oficial em PDF totalmente **adequada à LGPD**, mantendo os dados sensíveis estritamente locais.

        ### 🛠️ Stacks Utilizadas
        * **Front-end / Back-end:** Python 3 & Streamlit
        * **Inteligência Artificial:** Google Gemini (LLM) via `google-generativeai`
        * **Geração de Documentos:** FPDF (Exportação Nativa de PDFs)
        * **Design:** Custom CSS & Componentização UX/UI

        ---
        🔗 **[Acessar o Repositório Oficial no GitHub](https://github.com/SEU_USUARIO/SEU_REPOSITORIO)**
        """)

if __name__ == "__main__":
    main()