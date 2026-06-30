# Business Context - Smart Leading (ClearIT)

> Este arquivo é a fonte de verdade para Produto. O agente `@product` atualizará este arquivo quando houver novas descobertas.

## 1. Visão do Produto
O **Smart Leading** é um ecossistema ativo de liderança voltado para a ClearIT. A solução permite que líderes realizem reuniões 1:1 assistidas por Inteligência Artificial (copiloto human-in-the-loop), acompanha o desenvolvimento de liderados com base no Framework de Levels e mensura a maturidade da liderança através de telemetria de engajamento, fornecendo visibilidade direta para o RH.

## 2. Dores do Cliente (Problemas que resolvemos)
- **Falta de Continuidade:** Líderes e liderados esquecem o que foi combinado em reuniões anteriores, perdendo o histórico de acordos e sentimentos.
- **PDIs Genéricos:** Planos de Desenvolvimento Individual que não se conectam às reais necessidades do nível do colaborador no Framework de Levels.
- **Sobrecarga de Preparação:** Líderes gastam muito tempo preparando pautas e antecipando reações antes de cada conversa.

## 3. Backlog de Épicos e Features (Sprint 2 - MVP)
| ID | Título | Status | Notas |
|---|---|---|---|
| F-01 | Gerar Roteiro Inteligente de 1:1 | Concluído | IA integrada ao prompt da Metodologia CRIA e escuta ativa |
| F-02 | Exportar Ata da Reunião em PDF | Concluído | Geração de PDF (FPDF) e download com registro na telemetria |
| F-03 | Motor de Maturidade & Liga de Líderes | Concluído | Maturidade em 4 níveis por drivers reais no ranking por área |
| F-04 | Dashboard de Métricas do RH | Concluído | Tela executiva de RH mostrando adoção e simulação de eNPS |
| F-05 | [Enabler] Setup de Banco, Autenticação e IA | Concluído | Infraestrutura local com banco CSV e conexão com a API do Gemini |

---

## 4. Especificações Ativas (Em Detalhe)

### Feature F-01: Gerar roteiro inteligente de 1:1 (Story 1)
*   **User Story:** Como líder, quero gerar automaticamente um roteiro personalizado para reuniões 1:1 para conduzir conversas relevantes e contextualizadas.
*   **Contexto:** O sistema utiliza IA para gerar um roteiro personalizado considerando o histórico, combinados passados, sentimento registrado e o nível do liderado no Framework de Levels.
*   **Critérios de Aceite:**
    - O roteiro é gerado em até 30 segundos.
    - Considera as competências do nível atual do colaborador (ex: Júnior, Pleno, Sênior, Especialista).
    - O líder pode revisar e editar a pauta antes de iniciar formalmente.
    - Tratamento de erro robusto com opção de re-geração amigável em caso de falha de conexão de IA.
*   **Fora do Escopo:** Histórico de versões do roteiro; edição colaborativa em tempo real.

### Feature F-02: Exportar ata da reunião em PDF (Story 2)
*   **User Story:** Como líder, quero exportar a ata da reunião em PDF para compartilhar e registrar oficialmente o encontro.
*   **Contexto:** Ao finalizar o rito de 1:1, gera-se um PDF consolidando check-in, pautas, entregas, impedimentos, PDI e plano de ação.
*   **Critérios de Aceite:**
    - O download do PDF é feito em um único clique após a finalização da reunião.
    - A ata contém obrigatoriamente a assinatura do rito e o plano de ação (acordos, datas e responsáveis).
    - Cada download realizado dispara um evento de telemetria para computar a "Taxa de Documentação" do líder.
*   **Fora do Escopo:** Assinatura digital com certificados ICP-Brasil; versionamento físico de atas anteriores.

### Feature F-03: Motor de Maturidade & Liga de Líderes (Story 3)
*   **User Story:** Como líder, quero acompanhar minha classificação de maturidade e ver meu posicionamento no ranking da minha área para me engajar ativamente nos ritos de liderança.
*   **Contexto:** Classifica o líder em 4 níveis (Iniciante, Em desenvolvimento, Consistente, Referência) com base na telemetria (frequência de ritos, taxa de atas geradas e PDIs ativos), exibindo uma Liga de Líderes.
*   **Critérios de Aceite:**
    - O cálculo de maturidade obedece estritamente ao algoritmo definido no PRD.
    - O ranking ("Liga de Líderes") segmenta os dados apenas por líderes da mesma área (ex: Desenvolvimento não visualiza suporte).
    - Exibição de nuggets motivacionais inline ("Você não precisa ter todas as respostas").
*   **Fora do Escopo:** Gamificação e badges para liderados/colaboradores (movido para Backlog Futuro).

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
    - Banco de dados relacional configurado e tabelas iniciais criadas (Usuários, Ritos, Logs e PDIs).
    - Serviço de IA integrado via API respondendo com JSON formatado.
    - Variáveis de ambiente configuradas no arquivo `.env.example`.
*   **Fora do Escopo:** Infraestrutura de alta disponibilidade em produção; logs e monitoramento de carga.
