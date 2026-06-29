import streamlit as st
import re
import base64
import pandas as pd
import uuid
import os
from src.components.ui_forms import renderizar_formulario_contexto
from src.services.ai_agent import gerar_roteiro_ia
from src.services.pdf_maker import gerar_pdf
from src.utils.logger import registrar_log_1a1, marcar_ata_baixada

# ==========================================================
# 📊 BANCO DE DADOS LOCAL (Alimenta o Front-end sem ir para a IA)
# ==========================================================
DB_LIDERES_METADATA = {
    "Daniel Nascimento": {"area": "Tecnologia", "perfil": "Técnico (Focado em entregas e dados)"},
    "Bruna Silva": {"area": "Tecnologia", "perfil": "Em Transição (Novo na liderança, precisa de apoio)"},
    "Rodrigo Costa": {"area": "Negócios & Vendas", "perfil": "Engajado (Focado em carreira e desenvolvimento)"},
    "Amanda Souza": {"area": "RH & Operações", "perfil": "Engajado (Focado em carreira e desenvolvimento)"}
}
DB_LIDERES = list(DB_LIDERES_METADATA.keys())
DB_LIDERADOS = ["Paulo Augusto", "Lucas Silva", "Mariana Santos", "Pedro Alves", "Julia Ribeiro", "Gustavo Lima", "Beatriz Reis"]

def popular_dados_demonstracao():
    """Gera logs de telemetria históricos fictícios para a demonstração inicial e cálculo de maturidade."""
    caminho_csv = os.path.join(os.path.dirname(__file__), "..", "data", "telemetry_logs.csv")
    if not os.path.exists(caminho_csv):
        os.makedirs(os.path.dirname(caminho_csv), exist_ok=True)
        dados = [
            ["ID_Rito", "Data_Hora", "Nome_Lider", "Area_Lider", "Perfil_Lider", "Senioridade_Liderado", "Tempo_Casa", "Perfil_Comportamental", "Contem_PDI", "Ata_Baixada"],
            [str(uuid.uuid4()), "2026-06-15 10:00:00", "Daniel Nascimento", "Tecnologia", "Técnico (Focado em entregas e dados)", "Júnior", "Menos de 6 meses", "Analítico", "Sim", "Sim"],
            [str(uuid.uuid4()), "2026-06-15 14:30:00", "Daniel Nascimento", "Tecnologia", "Técnico (Focado em entregas e dados)", "Pleno", "1 a 3 anos", "Executor", "Sim", "Sim"],
            [str(uuid.uuid4()), "2026-06-16 09:00:00", "Bruna Silva", "Tecnologia", "Em Transição (Novo na liderança, precisa de apoio)", "Estagiário", "Menos de 6 meses", "Comunicador", "Sim", "Não"],
            [str(uuid.uuid4()), "2026-06-16 16:00:00", "Rodrigo Costa", "Negócios & Vendas", "Engajado (Focado em carreira e desenvolvimento)", "Sênior", "Mais de 3 anos", "Planejador", "Sim", "Sim"],
            [str(uuid.uuid4()), "2026-06-17 11:00:00", "Amanda Souza", "RH & Operações", "Engajado (Focado em carreira e desenvolvimento)", "Pleno", "6 meses a 1 ano", "Comunicador", "Não", "Sim"],
            [str(uuid.uuid4()), "2026-06-18 10:30:00", "Daniel Nascimento", "Tecnologia", "Técnico (Focado em entregas e dados)", "Sênior", "Mais de 3 anos", "Analítico", "Sim", "Sim"],
            [str(uuid.uuid4()), "2026-06-18 15:00:00", "Bruna Silva", "Tecnologia", "Em Transição (Novo na liderança, precisa de apoio)", "Júnior", "6 meses a 1 ano", "Executor", "Não", "Sim"],
            [str(uuid.uuid4()), "2026-06-19 14:00:00", "Rodrigo Costa", "Negócios & Vendas", "Engajado (Focado em carreira e desenvolvimento)", "Pleno", "1 a 3 anos", "Comunicador", "Sim", "Sim"],
            [str(uuid.uuid4()), "2026-06-22 09:30:00", "Daniel Nascimento", "Tecnologia", "Técnico (Focado em entregas e dados)", "Estagiário", "Menos de 6 meses", "Planejador", "Sim", "Não"],
            [str(uuid.uuid4()), "2026-06-23 10:00:00", "Rodrigo Costa", "Negócios & Vendas", "Engajado (Focado em carreira e desenvolvimento)", "Júnior", "6 meses a 1 ano", "Analítico", "Não", "Sim"],
            [str(uuid.uuid4()), "2026-06-23 15:30:00", "Bruna Silva", "Tecnologia", "Em Transição (Novo na liderança, precisa de apoio)", "Pleno", "1 a 3 anos", "Planejador", "Sim", "Não"],
            [str(uuid.uuid4()), "2026-06-24 11:30:00", "Daniel Nascimento", "Tecnologia", "Técnico (Focado em entregas e dados)", "Pleno", "6 meses a 1 ano", "Executor", "Sim", "Sim"],
            [str(uuid.uuid4()), "2026-06-24 16:00:00", "Amanda Souza", "RH & Operações", "Engajado (Focado em carreira e desenvolvimento)", "Sênior", "Mais de 3 anos", "Analítico", "Sim", "Sim"],
            [str(uuid.uuid4()), "2026-06-25 10:00:00", "Rodrigo Costa", "Negócios & Vendas", "Engajado (Focado em carreira e desenvolvimento)", "Estagiário", "Menos de 6 meses", "Executor", "Sim", "Sim"],
            [str(uuid.uuid4()), "2026-06-25 14:30:00", "Daniel Nascimento", "Tecnologia", "Técnico (Focado em entregas e dados)", "Sênior", "Mais de 3 anos", "Comunicador", "Não", "Sim"],
            [str(uuid.uuid4()), "2026-06-26 09:00:00", "Bruna Silva", "Tecnologia", "Em Transição (Novo na liderança, precisa de apoio)", "Júnior", "6 meses a 1 ano", "Analítico", "Sim", "Sim"],
            [str(uuid.uuid4()), "2026-06-26 13:30:00", "Rodrigo Costa", "Negócios & Vendas", "Engajado (Focado em carreira e desenvolvimento)", "Pleno", "1 a 3 anos", "Planejador", "Sim", "Sim"],
            [str(uuid.uuid4()), "2026-06-26 15:00:00", "Daniel Nascimento", "Tecnologia", "Técnico (Focado em entregas e dados)", "Júnior", "Menos de 6 meses", "Comunicador", "Sim", "Sim"]
        ]
        with open(caminho_csv, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerows(dados)

def carregar_dados_telemetria():
    caminho_csv = os.path.join(os.path.dirname(__file__), "..", "data", "telemetry_logs.csv")
    if os.path.exists(caminho_csv):
        try:
            return pd.read_csv(caminho_csv, sep=";")
        except Exception:
            return pd.DataFrame()
    return pd.DataFrame()

def calcular_estatisticas_lideres(df):
    estatisticas = {}
    
    # Inicializa todos do banco com 0
    for lider, meta in DB_LIDERES_METADATA.items():
        estatisticas[lider] = {
            "ritos": 0,
            "atas_baixadas": 0,
            "pdis": 0,
            "taxa_doc": 0.0,
            "taxa_pdi": 0.0,
            "maturidade": "Iniciante",
            "icone_maturidade": "🔴",
            "area": meta["area"],
            "perfil": meta["perfil"]
        }
        
    if df.empty:
        return estatisticas
        
    for lider in DB_LIDERES:
        df_lider = df[df["Nome_Lider"] == lider]
        if not df_lider.empty:
            ritos = len(df_lider)
            atas_baixadas = len(df_lider[df_lider["Ata_Baixada"] == "Sim"])
            pdis = len(df_lider[df_lider["Contem_PDI"] == "Sim"])
            
            taxa_doc = atas_baixadas / ritos if ritos > 0 else 0
            taxa_pdi = pdis / ritos if ritos > 0 else 0
            
            # Motor de maturidade baseado nos drivers
            if ritos >= 8 and taxa_doc >= 0.85 and taxa_pdi >= 0.7:
                maturidade = "Referência"
                icone = "🔵"
            elif ritos >= 5 and taxa_doc >= 0.7 and taxa_pdi >= 0.5:
                maturidade = "Consistente"
                icone = "🟢"
            elif ritos >= 3 and (taxa_doc >= 0.5 or taxa_pdi >= 0.4):
                maturidade = "Em Desenvolvimento"
                icone = "🟡"
            else:
                maturidade = "Iniciante"
                icone = "🔴"
                
            estatisticas[lider].update({
                "ritos": ritos,
                "atas_baixadas": atas_baixadas,
                "pdis": pdis,
                "taxa_doc": taxa_doc,
                "taxa_pdi": taxa_pdi,
                "maturidade": maturidade,
                "icone_maturidade": icone
            })
            
    return estatisticas

def main():
    st.set_page_config(page_title="Smart Leading - ClearIT", page_icon="assets/favicon.ico", layout="centered")

    # Garante dados de demonstração coerentes no primeiro carregamento
    popular_dados_demonstracao()

    # --- GERENCIAMENTO DE ESTADO GLOBAIS ---
    if "is_generating" not in st.session_state:
        st.session_state.is_generating = False

    # --- 1. CABEÇALHO (LOGO CLICÁVEL E DARK MODE) NO TOPO ABSOLUTO ---
    col_logo, col_tema = st.columns([4, 1])

    def get_base64_image(caminho_imagem):
        with open(caminho_imagem, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
        
    def computar_pontos_lider():
        st.session_state.lider_ganhou_ponto = True
        
    with col_logo:
        img_base64 = get_base64_image("assets/logo.png") 
        st.markdown(f"""
            <a href="/" target="_self" style="text-decoration: none;">
                <img src="data:image/png;base64,{img_base64}" width="160" alt="Logo Clear IT" style="margin-top: 5px;">
            </a>
        """, unsafe_allow_html=True)
        
    with col_tema:
        st.write("") 
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

    def travar_tela():
        st.session_state.is_generating = True

    # ==========================================================
    # 4. NAVBAR: ABAS DE NAVEGAÇÃO
    # ==========================================================
    tab_home, tab_ranking, tab_rh, tab_time, tab_sobre = st.tabs([
        "🏠 Home", 
        "🏆 Liga de Líderes", 
        "📊 Painel do RH (People Analytics)",
        "👥 Nosso Time", 
        "ℹ️ Sobre o Projeto"
    ])

    # ----------------------------------------------------------
    # ABA 1: HOME
    # ----------------------------------------------------------
    with tab_home:
        st.title("Smart Leading - ClearIT")
        st.markdown("Identifique os participantes e preencha as variáveis para gerar o roteiro e a ata oficial de 1:1.")
        st.markdown("<br>", unsafe_allow_html=True) 

        # Celebração de pontos do Líder
        if "lider_ganhou_ponto" in st.session_state and st.session_state.lider_ganhou_ponto:
            st.balloons()
            st.toast("🎯 Sensacional! Rito documentado e pontuação computada na Liga de Líderes!", icon="🔥")
            st.session_state.lider_ganhou_ponto = False

        if "alerta_form" in st.session_state:
            st.warning(st.session_state.alerta_form)
            del st.session_state.alerta_form

        # Identificação dos nomes
        st.header("Identificação do Encontro")
        st.info("Insira os nomes reais. Eles não são enviados para a IA (Conformidade com a LGPD), apenas injetados localmente na Ata em PDF.")
        col_nome1, col_nome2 = st.columns(2)
        with col_nome1:
            nome_lider = st.selectbox("Identifique-se (Líder):", [""] + DB_LIDERES)
        with col_nome2:
            nome_liderado = st.selectbox("Selecione o Liderado:", [""] + DB_LIDERADOS)
            
        st.markdown("---")

        # Formulário
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
        
        # Validação do formulário disparada no submit
        if gerar_btn:
            if not nome_lider or not nome_liderado:
                st.session_state.alerta_form = "⚠️ Você precisa selecionar o Líder e o Liderado nos dropdowns de Identificação no topo antes de gerar."
                st.session_state.is_generating = False
                st.rerun()
            elif not entregas_recentes.strip():
                st.session_state.alerta_form = "⚠️ Preencha o resumo das entregas/gaps recentes para contextualizar a Inteligência Artificial."
                st.session_state.is_generating = False
                st.rerun()

        # Motor de Geração
        if st.session_state.is_generating:
            if nome_lider and nome_liderado and entregas_recentes.strip():
                with st.spinner("A IA está analisando os perfis e criando o roteiro baseado na Metodologia CRIA..."):
                    try:
                        roteiro = gerar_roteiro_ia(perfil_lider, nivel_liderado, tempo_casa, perfil_comportamental, entregas_recentes, acordos)
                        st.session_state.roteiro_gerado = roteiro
                        
                        # Cria ID de rito e registra log inicial
                        st.session_state.id_rito = str(uuid.uuid4())
                        area_lider = DB_LIDERES_METADATA[nome_lider]["area"]
                        contem_pdi = bool(acordos.strip())
                        
                        registrar_log_1a1(
                            st.session_state.id_rito,
                            nome_lider,
                            area_lider,
                            perfil_lider,
                            nivel_liderado,
                            tempo_casa,
                            perfil_comportamental,
                            contem_pdi=contem_pdi,
                            ata_baixada=False
                        )
                    except Exception as e:
                        st.error(f"Erro na API do Gemini: {e}")
                    finally:
                        st.session_state.is_generating = False
                        st.rerun()

        # Exibição do Roteiro e Geração de PDF
        if "roteiro_gerado" in st.session_state and nome_lider and nome_liderado:
            st.markdown("---")
            st.subheader("💡 Seu Roteiro de Apoio (Confidencial)")
            st.markdown(st.session_state.roteiro_gerado)
            
            st.markdown("---")
            st.header("2. Registro Oficial (Ata LGPD)")
            st.info("A ata de resumo abaixo está pronta para download e assinatura física ou digital local.")
            
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
            
            caminho_pdf = gerar_pdf(nome_lider, nome_liderado, texto_para_pdf)
            with open(caminho_pdf, "rb") as f:
                pdf_bytes = f.read()
                
            def ao_baixar_pdf():
                marcar_ata_baixada(st.session_state.id_rito)
                computar_pontos_lider()
                
            st.download_button(
                label="Baixar Ata Oficial em PDF & Computar Pontos",
                data=pdf_bytes,
                file_name=f"Ata_1a1_{nome_liderado.replace(' ', '_')}.pdf",
                mime="application/pdf",
                use_container_width=True,
                type="primary",
                on_click=ao_baixar_pdf
            )

    # ----------------------------------------------------------
    # 🏆 ABA 2: LIGA DE LÍDERES (Ranking Dinâmico por Drivers)
    # ----------------------------------------------------------
    with tab_ranking:
        st.header("🏆 Liga de Líderes Clear IT")
        st.markdown("Quem lidera com clareza vai mais longe. Acompanhe a maturidade e a consistência do time de gestores:")
        st.markdown("<br>", unsafe_allow_html=True)

        # Filtro de áreas
        area_selecionada = st.selectbox("Filtrar ranking por área:", ["Todas", "Tecnologia", "Negócios & Vendas", "RH & Operações"])
        st.markdown("<br>", unsafe_allow_html=True)

        df_telemetria = carregar_dados_telemetria()
        estats = calcular_estatisticas_lideres(df_telemetria)

        # Filtra e formata a lista de ranking
        lista_ranking = []
        for lider, dados in estats.items():
            if area_selecionada == "Todas" or dados["area"] == area_selecionada:
                lista_ranking.append((lider, dados))

        # Ordenação por: 1º Ritos totais (Frequência), 2º Taxa de Doc (Critério de desempate)
        lista_ranking.sort(key=lambda x: (x[1]["ritos"], x[1]["taxa_doc"]), reverse=True)

        # Renderização dos cards do Ranking
        for posicao, (lider, dados) in enumerate(lista_ranking, start=1):
            medalha = "🥇" if posicao == 1 else "🥈" if posicao == 2 else "🥉" if posicao == 3 else "💼"
            
            with st.container(border=True):
                col_pos, col_nome, col_pts = st.columns([1.2, 4, 2])
                with col_pos:
                    st.subheader(f"{medalha} {posicao}º")
                with col_nome:
                    st.markdown(f"**{lider}** ({dados['area']})")
                    st.caption(f"Maturidade: {dados['icone_maturidade']} **{dados['maturidade']}** | Perfil de Gestão: *{dados['perfil'].split('(')[0].strip()}*")
                with col_pts:
                    st.markdown(f"🎯 **{dados['ritos']} ritos**")
                    st.caption(f"📄 Doc: {dados['taxa_doc']*100:.0f}% | 💼 PDI: {dados['taxa_pdi']*100:.0f}%")

    # ----------------------------------------------------------
    # 📊 ABA 3: PAINEL ANALÍTICO DO RH (People Analytics)
    # ----------------------------------------------------------
    with tab_rh:
        st.header("📊 Painel de Governança de RH — People Analytics")
        st.markdown("Consolidação dos principais indicadores de adoção, ritos e feedbacks da Clear IT em tempo real.")
        st.markdown("---")

        df_telemetria = carregar_dados_telemetria()

        if df_telemetria.empty:
            st.info("Nenhum dado de telemetria registrado no sistema ainda.")
        else:
            total_ritos = len(df_telemetria)
            total_baixadas = len(df_telemetria[df_telemetria["Ata_Baixada"] == "Sim"])
            taxa_documentacao = (total_baixadas / total_ritos * 100) if total_ritos > 0 else 0
            total_pdis = len(df_telemetria[df_telemetria["Contem_PDI"] == "Sim"])
            taxa_pdi = (total_pdis / total_ritos * 100) if total_ritos > 0 else 0
            
            # eNPS Liderança Estimado: Queda de 2026 foi para 45%. Projeção 2027 a partir da taxa de atas (Doc)
            enps_projetado = 45 + int(taxa_documentacao * 0.35)
            
            # Linha de Indicadores Executivos (KPIs Dores 1, 2 e 3)
            col_m1, col_m2, col_m3, col_m4 = st.columns(4)
            with col_m1:
                st.metric("Total de 1:1s / Feedbacks", f"{total_ritos}", help="Frequência total de ritos na plataforma (KPI Dor 1)")
            with col_m2:
                st.metric("Taxa de Documentação", f"{taxa_documentacao:.1f}%", help="Porcentagem de atas oficiais baixadas (KPI Dor 2 - Combate à Caixa-Preta)")
            with col_m3:
                st.metric("Engajamento PDI / Missões", f"{taxa_pdi:.0f}%", help="Porcentagem de conversas que resultaram em planos de PDI/Missões (KPI Dor 3)")
            with col_m4:
                st.metric("Estimativa eNPS 2027", f"{enps_projetado}", delta=f"+{enps_projetado - 45}" if enps_projetado > 45 else None, help="Projeção da evolução de Liderança e Confiança (KPI Dor 2)")

            st.markdown("<br>", unsafe_allow_html=True)

            # Gráficos da Telemetria
            col_g1, col_g2 = st.columns(2)
            with col_g1:
                st.subheader("Adoção por Perfil de Liderança")
                perfil_counts = df_telemetria["Perfil_Lider"].value_counts()
                st.bar_chart(perfil_counts)
                st.caption("Acompanhamento do engajamento de líderes Técnicos, em Transição e de Gestão (KPI Dor 1).")
                
            with col_g2:
                st.subheader("Senioridade dos Liderados")
                sen_counts = df_telemetria["Senioridade_Liderado"].value_counts()
                st.bar_chart(sen_counts)
                st.caption("Distribuição das conversas de 1:1 por nível de senioridade técnica.")

            st.markdown("---")
            st.subheader("Histórico Recente de Telemetria (Anonimizado - Conformidade LGPD)")
            st.dataframe(
                df_telemetria[["Data_Hora", "Area_Lider", "Perfil_Lider", "Senioridade_Liderado", "Contem_PDI", "Ata_Baixada"]].tail(10),
                use_container_width=True
            )

    # ----------------------------------------------------------
    # ABA 4: NOSSO TIME
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
    # ABA 5: SOBRE O PROJETO
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