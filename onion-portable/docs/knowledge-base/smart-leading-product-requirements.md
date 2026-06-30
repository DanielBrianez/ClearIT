# KB: Requisitos do Produto e Especificação de Features (ClearIT)

> **Contexto de Produto:** Consolidação das especificações de produto, fluxos de telas, novas features e pendências de UI levantadas no resumo pessoal das respostas da Priscila (RH). Este documento atua como o Documento de Requisitos de Produto (PRD) do Smart Leading.

---

## 1. Visão Geral
Este documento especifica os requisitos de software, features do MVP, fluxos de jornada do usuário (líder) e regras de interface para o Smart Leading. Ele visa sanar as dores de falta de continuidade das reuniões, PDIs genéricos e a sobrecarga de preparo das conversas, transformando a ferramenta em um ecossistema ativo de liderança.

---

## 2. Conceitos-Chave e Features Requeridas

### A. Fluxo Pré-Reunião (Preparação Automatizada)
Antes do rito da 1:1 ou Feedback, a aplicação deve disponibilizar ao líder um painel de consolidação contendo:
- **Painel de Contexto do Liderado:**
  - Histórico do rito anterior.
  - Status dos acordos/combinados passados.
  - Sentimentos e momentos pessoais registrados anteriormente.
  - Status das entregas, projetos em andamento e riscos técnicos/operacionais.
  - Comportamentos observados no período (exemplos de fatos e dados).
- **Integração com Levels:** Visualização das competências do nível atual do liderado no Framework de Levels e competências necessárias para a progressão (próximo nível).
- **Assistente de Pauta:** Auxílio na preparação e antecipação de reações do liderado, com estimativa de tempo necessária para o preparo.

---

### B. Feature de Envio Prévio de Pauta (2 dias antes)
- **Requisito:** A pergunta da pauta do liderado (*"O que você quer garantir que a gente aborde hoje?"*) deve ser enviada de forma automatizada ao colaborador com **2 dias de antecedência**.
- **UX:** As respostas do colaborador devem ser consolidadas e aparecer dinamicamente no painel do líder no momento da reunião.

---

### C. Painel "Durante a Conversa" (Registro & Assistência Co-construída)
Durante a reunião, a aplicação operará em tela contínua (SPA) com campos editáveis para anotações e sugestões automáticas por bloco:
1. **Check-in Humano:** Pergunta de empatia sobre o estado atual do colaborador.
2. **Pauta do Liderado:** Exibição das pautas enviadas previamente.
3. **Entregas e Impedimentos:** Campo de remoção de bloqueios.
4. **Desenvolvimento (Levels & PDI):** Acompanhamento de competências.
5. **Acordos (Plano de Ação):** Registro de próximos passos, responsáveis e datas limite.

---

### D. Nova Página: "Guia do Líder"
Deve ser implementada uma seção restrita de treinamento e consulta contendo:
- Metodologia de aplicação de feedbacks.
- Preparação de reuniões de 1:1 e estruturação de PDIs.
- Como aplicar o Modelo SBI (Situação, Comportamento, Impacto).
- Conceituação do papel da IA (*Human-in-the-loop* - apoio à decisão, e não substituição humana).
- Guia linguístico prático (Expressões a Evitar vs. Expressões a Incentivar).

---

### E. Estrutura do PDI Padronizado e Ficha do Liderado
- **Ficha do Liderado:** Perfil individual com habilidades técnicas, comportamentais, progresso do PDI, trilha de carreira e entregáveis por período.
- **Padrão do PDI:** Modelo único corporativo.
  - **Limite:** Máximo de 2 a 3 objetivos simultâneos para evitar sobrecarga.
  - **Elementos:** Competência do framework, ações práticas, prazo, evidências de progresso e suporte explícito do gestor.
  - **Prazos dos Entregáveis:** Marcos definidos obrigatoriamente para **1 mês, 2 meses, 3 meses e 6 meses**.

---

### F. Biblioteca Compartilhada de Temas
- **Requisito:** Campo aberto onde o líder pode cadastrar um tema customizado abordado na 1:1 (além dos sugeridos pelo RH no sistema).
- **Feature de Compartilhamento:** Uma vez inserido, esse tema é enviado automaticamente para a biblioteca compartilhada de líderes da **mesma área**, fomentando a troca de práticas e o alinhamento de problemas sistêmicos do time.

---

### G. Regra para Cálculo de Maturidade da Liderança
A classificação automática de maturidade do líder (**Iniciante, Em desenvolvimento, Consistente, Referência**) é calculada a partir de três drivers operacionais capturados pela telemetria:
1. **Frequência de Ritos:** Volume e regularidade de reuniões de 1:1 realizadas dentro da cadência quinzenal/mensal estipulada para a equipe.
2. **Taxa de Documentação:** Proporção de reuniões que resultaram na emissão e download de atas oficiais em PDF para governança.
3. **Engajamento em PDI:** Quantidade de PDIs gerados e mantidos ativos para os liderados de sua equipe direta.

*Algoritmo Conceitual de Classificação:*
- **Iniciante:** Frequência de 1:1 irregular, baixa taxa de documentação, sem PDIs ativos.
- **Em desenvolvimento:** 1:1 na cadência regular, mas baixa documentação ou PDIs pendentes.
- **Consistente:** 1:1 na cadência regular, atas em PDF geradas sistematicamente, com PDIs ativos para a maioria dos liderados.
- **Referência:** Cumpre 100% dos ritos e documentação, possui PDIs ativos para todos os liderados e contribui ativamente adicionando temas novos à biblioteca compartilhada da área.

---

### H. UX Micro-Interações (Nuggets e Dicas)
- **Nuggets de Encorajamento:** Inserção de mensagens sutis de apoio à liderança na UI durante o uso (Ex: *"Você não precisa ter todas as respostas"*).
- **Campos de Sugestão Ativa:** Dicas visuais inline com perguntas recomendadas com base no perfil comportamental selecionado.

---

## 3. Exemplos Práticos

### A. Fluxo de Estado das Abas (SPA) no Streamlit
Mapeamento conceitual do novo painel em tela única:

```python
# Conceito de Navegação SPA para o app.py
aba_home, aba_guia_lider, aba_ranking, aba_sobre = st.tabs([
    "🏠 Copiloto 1:1", 
    "📖 Guia do Líder", 
    "🏆 Liga de Líderes", 
    "ℹ️ Sobre"
])

with aba_guia_lider:
    st.header("📖 Guia do Líder da Clear IT")
    st.info("Human-in-the-Loop: A IA atua como copiloto. A responsabilidade de decisão é sua.")
    
    # Renderização do Guia Linguístico
    col_evitar, col_incentivar = st.columns(2)
    with col_evitar:
        st.subheader("❌ Evite usar:")
        st.markdown("- *'Você sempre faz isso.'*\n- *'Estou decepcionado com você.'*\n- *'Você precisa melhorar.'*")
    with col_incentivar:
        st.subheader("✅ Procure usar:")
        st.markdown("- *'Observei X, o impacto foi Y. O que acha?'*\n- *'Como posso te apoiar nessa mudança?'*\n- *'O que você precisa para virar esse jogo?'*")
```

### B. Estruturação do PDI Padronizado (JSON Schema)
Representação estruturada do PDI corporativo contendo as janelas de entregáveis:

```json
{
  "liderado_id": "liderado_01",
  "objetivos": [
    {
      "competencia_levels": "Comunicação Eficiente",
      "acao_concreta": "Apresentar a arquitetura do projeto no rito técnico de Agosto",
      "prazo": "2026-08-15",
      "suporte_gestor": "Disponibilizar 2h semanais de mentoria de arquitetura",
      "entregaveis": {
        "1_mes": "Esboço dos slides da apresentação",
        "2_meses": "Revisão geral da arquitetura com o Tech Lead",
        "3_meses": "Execução da palestra para a área",
        "6_meses": "Consolidar melhorias com base no feedback recebido"
      }
    }
  ]
}
```

---

## 4. Armadilhas (Gotchas)

> [!WARNING]
> **Sobrecarga de PDIs:** Não permitir que a IA ou o líder criem mais de 3 objetivos simultâneos no formulário de PDI. Focar no desenvolvimento focado e realizável.

> [!IMPORTANT]
> **Tag de Compartilhamento de Temas:** A biblioteca de temas compartilhados deve agrupar apenas líderes da **mesma área** (Ex: Desenvolvimento, QA, Infraestrutura). Compartilhar temas de forma global pode poluir a lista com problemas não relacionados (Ex: Líder de Suporte visualizando temas de DevOps).

> [!CAUTION]
> **Pauta Preenchida sem Notificação:** O envio da pauta ao colaborador com 2 dias de antecedência deve ter um mecanismo de fallback (ex: copiar texto/link rápido) caso o Streamlit não possua servidores de e-mail integrados no ambiente local do MVP.
