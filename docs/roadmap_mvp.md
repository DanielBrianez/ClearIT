# 🗺️ Roadmap do Produto - Assistente de Liderança Clear IT

Este documento traça a visão de evolução do produto, desde a fundação (MVP) até à sua integração total no ecossistema corporativo da empresa.

## 🚀 Fase 1: MVP (Fundação e Validação) - *Concluído*
O objetivo desta fase foi validar o conceito principal, garantindo a geração de valor imediato com o menor esforço de desenvolvimento possível.
- [x] Estruturação da arquitetura de ficheiros (*Clean Code*).
- [x] Integração com a API do Google Gemini (Motor de Inteligência Artificial).
- [x] Criação do Mega-Prompt com foco na adaptação comportamental do líder e liderado.
- [x] Geração de Ata Oficial em PDF (*fpdf*) com injeção local de dados.
- [x] Conformidade total com a LGPD (*Privacy by Design*).

## 🎨 Fase 2: UI/UX e Telemetria (Ajustes Finos) - *Em Progresso*
Foco na melhoria da experiência do utilizador (líderes) e na recolha de métricas silenciosas para o departamento de Recursos Humanos.
- [ ] Melhoria visual do ecrã no Streamlit (Injeção de CSS personalizado, cores da marca e logótipo).
- [ ] Implementação de sistema de *Logs Ocultos* num ficheiro `.csv` para telemetria (rastreio de perfis mais utilizados, seniores vs. juniores, e volume de atas geradas).
- [ ] Refinamento das regras de negócio do motor de Gamificação (Missões mais robustas e sistema de XP balanceado).

## 📊 Fase 3: Portal de *People Analytics* (Painel de RH) - *Em Planeamento*
Expansão do produto para atender também aos gestores de Recursos Humanos, dando visibilidade aos dados recolhidos.
- [ ] Criação de um segundo ecrã (Dashboard restrito para RH).
- [ ] Leitura e formatação visual dos *logs* guardados na Fase 2.
- [ ] Geração de gráficos (ex.: percentagem de uso por perfil de liderança, frequência de reuniões 1:1 na empresa).

## 🔌 Fase 4: Integrações Corporativas (Escala) - *Futuro*
Integrar o Assistente de Liderança diretamente nas ferramentas de comunicação que a equipa já utiliza diariamente.
- [ ] Integração de notificações de Missões/XP através de *Webhooks* para o Slack ou Microsoft Teams.
- [ ] Integração com a API do Google Calendar / Outlook para leitura automática da agenda de 1:1s e preparação prévia.
- [ ] Envio automático (e opcional) da Ata de PDF encriptada para a base de dados central do RH.