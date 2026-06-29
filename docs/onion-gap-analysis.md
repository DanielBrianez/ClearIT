# Análise de Gaps: Especificação Ideal (Onion) vs. Implementação Atual (ClearIT) 🔍

Este documento mapeia as diferenças entre a especificação ideal do **Onion Portable** e a implementação real existente no código do **ClearIT** (`src/`). O objetivo é orientar o time de engenharia sobre o que precisa ser construído para alinhar o código com o escopo de produto planejado, sem realizar alterações de código neste momento.

---

## 🗺️ 1. Mapeamento Geral por Feature

### F-01: Gerar Roteiro Inteligente de 1:1
*   **O Ideal (Onion Spec):** O roteiro considera histórico, combinados passados, sentimento e o nível do liderado no Framework de Levels.
*   **O Implementado (Código Atual):** A IA gera o roteiro com base em parâmetros inseridos manualmente pelo líder na hora da reunião. Não há persistência ou leitura automática de históricos passados ou níveis de competência no banco.
*   **Gaps no Código:**
    - Integrar carregamento de dados do colaborador e histórico de ritos anteriores no [ui_forms.py](file:///c:/Users/Pulse%20Mais/24+1/ClearIT/src/components/ui_forms.py) e no [ai_agent.py](file:///c:/Users/Pulse%20Mais/24+1/ClearIT/src/services/ai_agent.py).
    - Mapear as competências de cada nível de senioridade do Framework de Levels diretamente no prompt da IA.

### F-02: Exportar Ata da Reunião em PDF
*   **O Ideal (Onion Spec):** O PDF consolida check-in, pauta, entregas, impedimentos, PDI e plano de ação. Possui gatilho de compartilhamento rápido com o liderado pós-download e envia cópia ao RH.
*   **O Implementado (Código Atual):** O PDF é gerado localmente pelo [pdf_maker.py](file:///c:/Users/Pulse%20Mais/24+1/ClearIT/src/services/pdf_maker.py) e faz o download. A telemetria registra apenas a flag local se o arquivo foi baixado.
*   **Gaps no Código:**
    - Falta implementar o gatilho visual no [app.py](file:///c:/Users/Pulse%20Mais/24+1/ClearIT/src/app.py) para o líder enviar a ata diretamente ao e-mail ou Slack do colaborador.
    - Falta implementar a cópia automática por e-mail para a área de calibração de performance do RH.

### F-03: Motor de Maturidade & Liga de Líderes
*   **O Ideal (Onion Spec):** Avalia e classifica o líder em 4 níveis (Iniciante, Em desenvolvimento, Consistente, Referência) com base em 3 drivers operacionais: Frequência, Taxa de Documentação e Engajamento em PDI.
*   **O Implementado (Código Atual):** O [app.py](file:///c:/Users/Pulse%20Mais/24+1/ClearIT/src/app.py) apenas soma `+1` no dicionário de ranking toda vez que o líder clica em baixar o PDF, sem aplicar nenhuma regra matemática ou lógica de níveis de maturidade.
*   **Gaps no Código:**
    - Implementar a função lógica que lê os registros de telemetria daquele líder e calcula a conformidade das 1:1s, a proporção de atas baixadas e a presença de PDIs ativos.
    - Alterar a exibição da tela de Ranking para exibir a categoria do líder (Ex: "Daniel Nascimento — Nível: Consistente 🏆").

### F-04: Dashboard de Métricas do RH
*   **O Ideal (Onion Spec):** Painel executivo restrito ao RH mostrando adoção aggregate, conformidade e distribuição de maturidade sem expor os conteúdos privados das reuniões.
*   **O Implementado (Código Atual):** Não existe no código. As abas atuais são apenas `Home`, `Ranking`, `Nosso Time` e `Sobre`.
*   **Gaps no Código:**
    - Criar uma nova aba/tela exclusiva no [app.py](file:///c:/Users/Pulse%20Mais/24+1/ClearIT/src/app.py) (ex: `tab_rh = st.tabs(...)` protegida por senha simples ou perfil de acesso).
    - Desenvolver gráficos agregados lendo o arquivo [telemetry_logs.csv](file:///c:/Users/Pulse%20Mais/24+1/ClearIT/data/telemetry_logs.csv).

---

## 🔎 2. Gaps por Arquivo de Código

### 1. [src/app.py](file:///c:/Users/Pulse%20Mais/24+1/ClearIT/src/app.py)
*   **Falta de Abas Requeridas:** Ausência da aba de **Dashboard de RH** (Feature F-04) e da aba de treinamento **Guia do Líder** (Requisito D).
*   **Mockups/Placeholders de Time:** A aba "Nosso Time" (`tab_time`) está com nomes de membros fictícios e imagens geradas genericamente de avatares.
*   **Ordenação Simples do Ranking:** Falta de segmentação por área e lógica de maturidade.

### 2. [src/components/ui_forms.py](file:///c:/Users/Pulse%20Mais/24+1/ClearIT/src/components/ui_forms.py)
*   **Inputs Genéricos:** Os acordos e planos de desenvolvimento são coletados em uma caixa de texto livre. Não há o formulário estruturado para PDI (limite de 2 a 3 objetivos, suporte do gestor e marcos de 1, 2, 3 e 6 meses).

### 3. [src/services/ai_agent.py](file:///c:/Users/Pulse%20Mais/24+1/ClearIT/src/services/ai_agent.py)
*   **Instruções de Levels no Prompt:** O prompt atual do Gemini não possui conhecimento sobre a matriz de habilidades do **Framework de Levels** da ClearIT. Ele gera um roteiro comportamental geral, mas não técnico por competência.

### 4. [src/services/pdf_maker.py](file:///c:/Users/Pulse%20Mais/24+1/ClearIT/src/services/pdf_maker.py)
*   **Tratamento de String:** O script realiza limpeza de marcas brutas da IA, mas pode falhar se a estrutura de retorno do Gemini mudar a tag de divisão `--- ATA OFICIAL ---`. Precisa de um parser estruturado ou JSON Output.

### 5. [src/utils/logger.py](file:///c:/Users/Pulse%20Mais/24+1/ClearIT/src/utils/logger.py)
*   **Limitação de Metadados:** O logger registra apenas se a ata foi gerada e baixada localmente. Ele não captura eventos de compartilhamento ou se o PDI foi ativado, impedindo a computação correta dos drivers de maturidade.
