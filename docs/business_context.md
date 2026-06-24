# 📄 Contexto de Negócio (Business Context) — Assistente de Liderança Clear IT

## 1. Visão Executiva
O **Assistente de Liderança Clear IT** é uma solução estratégica desenvolvida sob o modelo de MVP (Minimum Viable Product) corporativo. Trata-se de uma aplicação web de página única (*Single Page Application*) operada por Inteligência Artificial (LLM - Google Gemini) voltada para o empoderamento e suporte de líderes na preparação, condução e documentação de reuniões de 1:1 (*one-on-ones*) e alinhamentos de feedback.

A plataforma automatiza a carga cognitiva de planejamento, customiza as abordagens com base em perfis comportamentais e resolve uma dor histórica do setor de Recursos Humanos: a falta de governança, padronização e engajamento prático nos ritos de gestão de pessoas.

---

## 2. O Problema (As Dores do Negócio)
Atualmente, a gestão de talentos e o acompanhamento de performance na Clear IT esbarram em três gargalos operacionais e estratégicos:

* **Silos de Liderança e Sobrecarga Cognitiva:** Líderes técnicos (Tech Leads) ou gestores recém-promovidos (em transição) carecem de tempo ou framework metodológico para estruturar conversas difíceis, planos de desenvolvimento individual (PDI) ou feedbacks construtivos, resultando em reuniões superficiais.
* **Feedbacks Burocráticos e Desengajamento:** O processo tradicional de feedback é frequentemente percebido pelos liderados como um rito puramente burocrático e retrospectivo, sem conexão com o futuro, desafios práticos ou incentivos gamificados.
* **Apagão de Dados e Governança no RH:** O departamento de Recursos Humanos não possui visibilidade em tempo real sobre a frequência, qualidade ou adoção das reuniões de 1:1. A ausência de atas padronizadas impede o cruzamento de dados para identificar gargalos de turnover, desalinhamento de escopo ou insatisfação cultural nas equipes.

---

## 3. A Solução Proposta
A plataforma atua como um copiloto de liderança focado em dados e comportamento. O fluxo de valor é dividido em três etapas automatizadas dentro de uma interface unificada:

1. **Pré-Reunião (Mapeamento Contextual):** O líder insere variáveis objetivas (Senioridade do colaborador, tempo de casa, perfil comportamental da metodologia Clear IT e resumo de entregas ou gaps recentes).
2. **Durante a Reunião (Roteiro Hiper-Personalizado):** A IA processa as variáveis cruzando o perfil do próprio líder com o perfil do liderado, devolvendo instantaneamente um roteiro estruturado (Abertura, Pauta Principal e Alinhamento).
3. **Pós-Reunião (Gamificação e Registro):** O sistema traduz os acordos firmados em um fechamento gamificado (atribuição automática de XP, indicação de Badge de reconhecimento e uma Missão prática para o próximo ciclo) e disponibiliza o download imediato de uma Ata Oficial em PDF.

---

## 4. Proposta de Valor e Impacto de Negócio (ROI)
* **Eficiência Operacional:** Redução estimada em até 70% no tempo gasto pelos gestores na preparação de pautas de liderança.
* **Retenção de Talentos (Redução de Turnover):** Liderados recebem feedbacks mais empáticos, previsíveis e direcionados, aumentando o sentimento de pertencimento e clareza de carreira.
* **Cultura de Alta Performance Gamificada:** A introdução de metas quinzenais tangíveis (Missões) e recompensas simbólicas (Badges/XP) aumenta o engajamento prático do colaborador com seus próprios gaps.
* **Telemetria Estratégica (People Analytics):** Através de um sistema interno e silencioso de logs, a plataforma coleta metadados operacionais (frequência, perfis mais acessados, geração de atas) permitindo que o RH monitore a saúde da liderança da empresa sem violar a privacidade.

---

## 5. Segurança, Confidencialidade e Conformidade (LGPD)
Desenhado sob o princípio rigoroso de **Privacy by Design**, o projeto mitiga riscos jurídicos associados ao vazamento ou processamento indevido de dados pessoais na nuvem:

* **Isolamento de Dados Sensíveis:** A comunicação direta com a API da inteligência artificial utiliza estritamente o contexto corporativo e comportamental abstrato.
* **Injeção Local de Identificadores:** Nomes de líderes, nomes de liderados e assinaturas eletrônicas são inseridos pelo usuário exclusivamente na camada de *front-end* no momento final de geração do PDF. 
* **IA Cega para Identidades:** Como os dados sensíveis nunca trafegam pela rede e não são enviados para os servidores da IA, o projeto garante conformidade irrestrita com as diretrizes da Lei Geral de Proteção de Dados (LGPD).