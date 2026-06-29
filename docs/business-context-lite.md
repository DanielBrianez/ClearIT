# Business Context - Smart Leading (ClearIT)

> Este arquivo é a fonte de verdade para Produto. O agente `@product` atualizará este arquivo quando houver novas descobertas.

## 1. Visão Geral (Product Vision)
O **Smart Leading** é um ecossistema ativo de liderança voltado para a ClearIT. A solução opera como uma aplicação web de página única (*Single Page Application*) que permite que líderes realizem reuniões 1:1 assistidas por Inteligência Artificial (copiloto *human-in-the-loop*), acompanha o desenvolvimento de liderados com base no Framework de Levels e mensura a maturidade da liderança através de telemetria de engajamento, fornecendo visibilidade direta para o RH.

A plataforma automatiza a carga cognitiva de planejamento, customiza as abordagens com base em perfis comportamentais e resolve a falta de governança, padronização e engajamento prático nos ritos de gestão de pessoas.

---

## 2. Dores do Cliente (Problemas que resolvemos)
- **Falta de Continuidade:** Líderes e liderados esquecem o que foi combinado em reuniões anteriores, perdendo o histórico de acordos, sentimentos e combinados passados.
- **PDIs Genéricos:** Planos de Desenvolvimento Individual que não se conectam às reais necessidades do nível do colaborador no Framework de Levels.
- **Sobrecarga de Preparação:** Líderes gastam muito tempo (cerca de 30 a 40 minutos) preparando pautas de liderança e antecipando reações antes de cada conversa.
- **Apagão de Dados e Governança no RH:** O departamento de Recursos Humanos não possui visibilidade em tempo real sobre a frequência, qualidade ou adoção das reuniões de 1:1.

---

## 3. Backlog de Épicos e Features (Sprint 2 - MVP)
| ID | Título | Status | Notas |
|---|---|---|---|
| F-01 | Gerar Roteiro Inteligente de 1:1 | Concluído | IA integrada ao prompt da Metodologia CRIA e escuta ativa (Seguro LGPD) |
| F-02 | Exportar Ata da Reunião em PDF | Concluído | Geração de PDF (FPDF) e download com registro na telemetria |
| F-03 | Motor de Maturidade & Liga de Líderes | Em Progresso | Classificação em 4 níveis por drivers operacionais. *Implementada apenas versão básica no código.* |
| F-04 | Dashboard de Métricas do RH | Em Progresso | Tela executiva de RH mostrando adoção e maturidade. *Pendente de implementação no código.* |
| F-05 | Setup de Banco, Autenticação e IA | Concluído | Infraestrutura local com banco CSV (`data/telemetry_logs.csv`) e API do Gemini |

---

## 4. Especificações Ativas (Em Detalhe)

### Feature F-01: Gerar roteiro inteligente de 1:1 (Story 1)
*   **User Story:** Como líder, quero gerar automaticamente um roteiro personalizado para reuniões 1:1 para conduzir conversas relevantes e contextualizadas.
*   **Contexto:** O sistema utiliza IA para gerar um roteiro personalizado considerando o histórico, combinados passados, sentimento registrado e o nível do liderado no Framework de Levels.
*   **Critérios de Aceite:**
    - O roteiro é gerado em até 10 segundos e renderizado na tela (SPA).
    - Considera as competências do nível atual do colaborador (ex: Júnior, Pleno, Sênior, Especialista).
    - O roteiro é adaptado dinamicamente aos três perfis de liderança mapeados (Técnico, Em transição, Engajado).
    - A comunicação com a IA deve ser processada utilizando estritamente contexto comportamental abstrato.
    - É proibida a inserção de dados sensíveis (nomes reais, cpf) no prompt enviado ao LLM (*Privacy by Design*).
    - O líder pode revisar e editar a pauta antes de iniciar formalmente.
    - Tratamento de erro robusto com opção de re-geração amigável em caso de falha de conexão de IA.
*   **Fora do Escopo:** Histórico de versões do roteiro; edição colaborativa em tempo real.

### Feature F-02: Exportar ata da reunião em PDF (Story 2)
*   **User Story:** Como líder, quero exportar a ata da reunião em PDF para compartilhar e registrar oficialmente o encontro.
*   **Contexto:** Ao finalizar o rito de 1:1, gera-se um PDF consolidando check-in, pautas, entregas, impedimentos, PDI e plano de ação.
*   **Critérios de Aceite:**
    - O download do PDF é feito em um único clique após a finalização da reunião.
    - A injeção de dados sensíveis de identificação (nome do líder, liderado e área) ocorre exclusivamente no *front-end* no momento da geração do arquivo final.
    - O PDF gerado não é armazenado na nuvem da aplicação ou trafegado para os servidores da IA.
    - O PDF remove marcações brutas da IA (ex: `--- ATA OFICIAL ---`).
    - A ata contém obrigatoriamente a assinatura do rito e o plano de ação (acordos, datas e responsáveis).
    - Cada download realizado dispara um evento de telemetria para computar a "Taxa de Documentação" do líder.
    - **Pendente:** O sistema deve disponibilizar um gatilho rápido no front-end para que o líder envie a Ata de Alinhamento diretamente ao liderado assim que gerada.
*   **Fora do Escopo:** Assinatura digital com certificados ICP-Brasil; versionamento físico de atas anteriores.

### Feature F-03: Motor de Maturidade & Liga de Líderes (Story 3)
*   **User Story:** Como líder, quero acompanhar minha classificação de maturidade e ver meu posicionamento no ranking da minha área para me engajar ativamente nos ritos de liderança.
*   **Contexto:** Classifica o líder em 4 níveis (Iniciante, Em desenvolvimento, Consistente, Referência) com base na telemetria (frequência de ritos, taxa de atas geradas e PDIs ativos), exibindo uma Liga de Líderes.
*   **Critérios de Aceite:**
    - O cálculo de maturidade obedece estritamente aos drivers do PRD (Frequência de Ritos, Taxa de Documentação e Engajamento em PDI).
    - O ranking ("Liga de Líderes") segmenta os dados por líderes da mesma área (ex: Desenvolvimento não visualiza suporte).
    - Exibição de nuggets motivacionais inline ("Você não precisa ter todas as respostas").
    - **Pendente:** Depois da finalização da ata, o usuário é automaticamente direcionado para a dashboard "Meu Perfil" para ver seu progresso.
*   **Fora do Escopo:** Gamificação e badges para liderados/colaboradores.

### Feature F-04: Dashboard de Métricas do RH (Story 4)
*   **User Story:** Como profissional de RH, quero visualizar indicadores das reuniões 1:1 para acompanhar o engajamento dos líderes.
*   **Contexto:** Painel centralizado do RH consolidando a adoção do rito e a evolução da maturidade na ClearIT.
*   **Critérios de Aceite:**
    - Exibe o número de reuniões concluídas na sprint.
    - Exibe a porcentagem de conformidade de ritos quinzenais/mensais.
    - Exibe a distribuição de maturidade (ex: 20% Referência, 40% Consistente).
    - Permite visualização dos dados consolidados sem exposição direta de anotações privadas de 1:1.
*   **Fora do Escopo:** Exportação de planilhas customizadas; criação de gráficos ad-hoc pelo usuário.

### Feature F-05: Setup de Infraestrutura & APIs (Story 5)
*   **Technical Enabler:** Como equipe de desenvolvimento, necessitamos configurar a infraestrutura básica e conexões de API para sustentar as transações do MVP de forma estável.
*   **Critérios de Aceite:**
    - Banco local CSV (`data/telemetry_logs.csv`) configurado e gravando metadados de telemetria.
    - O log deve conter: Data/Hora, Perfil do Líder, Perfil Comportamental, Senioridade e flag se a Ata em PDF foi baixada.
    - Serviço de IA integrado via API do Gemini (`gemini-2.5-flash`) respondendo com formatação de texto estruturado.
    - Variáveis de ambiente configuradas no arquivo `.env.example`.
*   **Fora do Escopo:** Infraestrutura de alta disponibilidade em produção; logs e monitoramento de carga.
