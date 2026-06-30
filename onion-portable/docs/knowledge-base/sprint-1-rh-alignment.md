# KB: Diretrizes de RH e Regras de Negócio - Sprint 1 (ClearIT)

> **Contexto de Negócio:** Consolidação das respostas oficiais do RH da Clear IT (Priscila Bacelar) coletadas na Sprint 1. Este documento serve como fonte de verdade para as regras de conversação do agente de IA, features do sistema e métricas de People Analytics.

---

## 1. Visão Geral
Este documento especifica a distinção metodológica entre os ritos de **1:1** e de **Feedback**, as regras de comunicação não-violenta (comunicação humana/empática) para feedbacks corretivos, as frequências de acompanhamento e o design de telemetria necessário para fornecer insumos estratégicos ao RH sem comprometer a confiança dos líderes e colaboradores.

---

## 2. Conceitos-Chave

### A. Diferença Metodológica de Ritos

#### 1. Reunião 1:1 (One-on-One)
- **Foco:** Relacionamento, bem-estar e desenvolvimento contínuo.
- **Propriedade:** **A agenda pertence ao liderado**. O gestor entra preparado, mas prioriza a pauta trazida pelo colaborador.
- **Estrutura Obrigatória do Roteiro:**
  1. **Check-in Humano (Não-protocolar):** Entender o estado de energia/ânimo do liderado para calibrar o tom da reunião.
  2. **Pauta do Liderado:** Pergunta aberta inicial: *"O que você quer garantir que a gente aborde hoje?"*
  3. **Obstáculos e Entregas (Sem Microgestão):** Identificar impedimentos onde o gestor atua como facilitador e removedor de bloqueios.
  4. **Desenvolvimento e Carreira:** Inserção de competências do Framework de Levels e progresso de PDI (conversa estratégica).
  5. **Acordos e Combinados:** Definição clara de prazos e responsabilidades (verificáveis no próximo encontro).

#### 2. Sessão de Feedback
- **Foco:** Comportamento observado específico e impacto gerado.
- **Propriedade:** Direcionada pelo líder com foco em desenvolvimento (reconhecimento ou melhoria).
- **Estrutura Obrigatória do Roteiro:**
  1. **Contexto e Intenção:** Esclarecer que o objetivo é crescimento, não punição.
  2. **Escuta Ativa (Fase Inegociável):** Perguntar a perspectiva do liderado antes de expor a conclusão (*"Como você enxerga essa situação?"*).
  3. **Modelo SBI (Situação, Comportamento, Impacto):** Específico, baseado em fatos recentes, sem generalizações.
  4. **Co-construção de Solução:** Gestor e liderado definem juntos o plano de ação e a data de revisão.

---

### B. Matriz de Cadências e Frequências

| Rito / Contexto | Frequência Ideal | Objetivo Principal |
|---|---|---|
| **1:1 Geral** | Quinzenal ou Mensal | Alinhamento contínuo e relacionamento |
| **Colaborador Novo** | Primeiros 45 dias, depois 90 dias | Acompanhamento do período de experiência |
| **Risco de Desligamento** | Quinzenal | Ajuste rápido de rota e monitoramento de performance |
| **Feedback Corretivo** | Imediato (máximo 48h) | Correção tempestiva baseada no comportamento observado |
| **Feedback de Carreira** | Bimensal ou Trimestral | Calibração de competências e desenvolvimento |

---

### C. Regras de Tom e Humanização (Feedbacks Corretivos)
Para evitar resistências e atritos, os roteiros de feedbacks corretivos gerados pela IA devem seguir regras de comunicação empática:
- **Separar Pessoa de Comportamento:** Nunca rotular o indivíduo (Ex: *"Você é desorganizado"*). Focar na ação observada (Ex: *"Nos últimos dois sprints, as tarefas chegaram sem documentação"*).
- **Traduzir Emoção em Dados:** Evitar frases subjetivas (Ex: *"Estou desapontado com você"*). Utilizar impactos mensuráveis (Ex: *"A falta de documentação gerou 6 horas extras de retrabalho para o time"*).
- **Vocabulário de Abertura vs. Fechamento:**
  - *Proibido:* "Você sempre...", "É inaceitável", "Eu já te disse antes", "Você é o único que...".
  - *Obrigatório:* "Observei X que gerou o impacto Y", "O que podemos combinar...", "Como posso te apoiar nesta mudança?".

---

### D. Requisitos de Telemetria para o RH (People Analytics)
O RH necessita de relatórios consolidados agregados. Os logs locais e exportáveis devem conter dados estratégicos para o RH agir preventivamente:
1. **Adesão ao Processo:** `%` de líderes ativos e ranking de cadência de 1:1 por área.
2. **Prevenção de Turnover:** Lista de colaboradores sem 1:1 há mais de 30 dias.
3. **Mapeamento de Riscos:** Sinalizações de risco marcadas diretamente pelos gestores (risco de desligamento ou performance).
4. **Maturidade da Liderança:** Classificação dos líderes baseada na consistência e qualidade dos ritos (Iniciante, Em Desenvolvimento, Consistente, Referência).
5. **Adesão ao Framework:** Identificar quais competências do Framework de Levels são mais discutidas e quais nunca aparecem (sinal de alerta de clareza das competências).

---

## 3. Exemplos Práticos

### A. Estrutura de Prompt do Agente para Reunião 1:1
Abaixo está o mapeamento de como as regras de 1:1 são passadas no prompt do Gemini:

```python
prompt_1a1 = """
Você é um Mentor Executivo e parceiro de RH estratégico da Clear IT.
Escreva um ROTEIRO DE 1:1 focado no relacionamento e no desenvolvimento do liderado.

DADOS DA REUNIÃO:
- Perfil do Líder: {perfil_lider}
- Senioridade: {nivel_liderado}
- Comportamento: {perfil_comportamental}

INSTRUÇÕES DO ROTEIRO (SIGA À RISCA):
1. Comece fornecendo uma orientação de "Check-in Humano" para o líder fazer uma pergunta não protocolar sobre bem-estar.
2. Inclua obrigatoriamente a pergunta inicial de abertura da pauta pelo liderado: "O que você quer garantir que abordemos hoje?".
3. Insira de 1 a 2 perguntas de desenvolvimento pessoal baseadas no nível {nivel_liderado} do Framework de Levels (ex: competências técnicas vs. comunicação).
4. Forneça uma pergunta final para o gestor solicitar feedback sobre si mesmo: "Tem algo que eu poderia fazer diferente para te apoiar melhor?".
5. Enfatize que a reunião deve terminar obrigatoriamente com a definição de acordos claros com prazo definido.
"""
```

### B. Mapeamento de Risco e Telemetria de RH
Exemplo de dados adicionados à telemetria anônima para capturar a eficácia de desenvolvimento e flags de risco:

```json
{
  "timestamp": "2026-06-29 15:52:00",
  "perfil_lider": "Lider em Transicao",
  "senioridade_liderado": "L2",
  "perfil_comportamental": "Analitico",
  "bloco_desenvolvimento_presente": true,
  "sinalizacao_risco_rh": "Baixa Performance / Risco de Desligamento",
  "competencia_framework_discutida": "Comunicação e Alinhamento"
}
```

---

## 4. Armadilhas (Gotchas)

> [!WARNING]
> **Percepção de Vigilância (Autocensura):** Se os líderes sentirem que o RH monitora de forma detalhada o conteúdo textual de cada reunião, eles irão se autocensurar ou boicotar a ferramenta. Os dados que vão para a telemetria do RH devem ser estritamente quantitativos, categóricos e anonimizados. A Ata de PDF é a única via com nomes, e ela é processada exclusivamente no navegador do líder.

> [!IMPORTANT]
> **Omissão da Escuta no Feedback:** Um dos erros mais comuns dos líderes é falar o feedback SBI sem antes perguntar a versão do liderado. O roteiro de feedback gerado pelo agente deve ter uma indicação visual gigante instruindo o líder a ouvir antes de apresentar o impacto.

> [!CAUTION]
> **PDI Sem Suporte do Gestor:** Um PDI unilateral (onde só o liderado tem deveres) é percebido como punição. Os roteiros de PDI sugeridos pelo agente devem obrigatoriamente incluir a pergunta: *"Qual suporte você precisa de mim para viabilizar isso?"*.
