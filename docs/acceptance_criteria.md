# ✅ Critérios de Aceite (Acceptance Criteria) - MVP Clear IT

Este documento define os requisitos técnicos e de negócio que devem ser atendidos para que a versão inicial (MVP) do Assistente de Liderança seja considerada "Pronta" (*Done*).

## 1. Personalização e Segurança (LGPD)
- [x] O sistema deve gerar um roteiro de 1:1 adaptado dinamicamente aos três perfis de liderança mapeados (Técnico, Em transição, Engajado) e ao contexto comportamental do liderado.
- [x] A comunicação com a IA deve ser processada utilizando estritamente contexto comportamental abstrato.
- [x] É terminantemente proibida a inserção de dados sensíveis (nomes reais, CPF, questões de saúde) no *prompt* enviado ao LLM, garantindo *Privacy by Design*.

## 2. Geração da Ata Oficial e Governança
- [x] O sistema deve permitir a geração e o download de uma "Ata de Alinhamento" no formato PDF diretamente pelo navegador.
- [x] A seleção de identidades (líder e liderado) deve ser feita via banco de dados local (Dropdowns restritos) no *front-end*, sem envio para a nuvem.
- [x] O PDF gerado não deve ser armazenado na nuvem da aplicação ou trafegado para os servidores da IA.

## 3. Gamificação de Liderança (Engajamento)
- [x] O sistema deve incentivar o engajamento dos gestores através de um Ranking de Líderes em tempo real.
- [x] A cada Ata em PDF gerada e baixada, o líder selecionado deve receber pontuação (+1 Sessão) automaticamente no placar da empresa.
- [x] A interface deve celebrar o engajamento visualmente (toasts e balões) para reforçar o hábito da governança.

## 4. Jornada em Tela Única (UX)
- [x] O fluxo completo do usuário (preparação, visualização do roteiro de apoio, identificação e download da ata) deve acontecer em uma interface contínua (SPA organizada por Abas).
- [x] O sistema não deve exigir navegação para telas secundárias ou abertura de abas externas, garantindo que o líder mantenha o foco e reduzindo a carga cognitiva.

## 5. Captura de Telemetria (Logs Ocultos)
- [x] A cada roteiro gerado com sucesso, a plataforma deve registrar silenciosamente uma nova linha em um arquivo de log local para telemetria.
- [x] O log deve conter estritamente metadados estratégicos: Data/Hora, Perfil do Líder selecionado, Perfil Comportamental do Liderado e Senioridade.
- [x] É terminantemente proibido salvar o conteúdo textual das conversas geradas, fornecendo insumos para o *People Analytics* do RH sem comprometer a privacidade das 1:1s.