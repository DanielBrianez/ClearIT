# ✅ Critérios de Aceite (Acceptance Criteria) - MVP Clear IT

Este documento define os requisitos técnicos e de negócio que devem ser atendidos para que a versão inicial (MVP) do Assistente de Liderança seja considerada "Pronta" (*Done*).

## 1. Personalização e Segurança (LGPD)
- [x] O sistema deve gerar um roteiro de 1:1 adaptado dinamicamente aos três perfis de liderança mapeados (Técnico, Em transição, Engajado) e ao contexto comportamental do liderado.
- [x] A comunicação com a IA deve ser processada utilizando estritamente contexto comportamental.
- [x] É terminantemente proibida a inserção de dados sensíveis (nomes reais, CPF, questões de saúde) no *prompt* enviado ao LLM, garantindo *Privacy by Design*.

## 2. Geração da Ata Oficial (Governança)
- [ ] O sistema deve permitir a geração e o download de uma "Ata de Alinhamento" no formato PDF diretamente pelo navegador.
- [ ] A injeção de dados sensíveis de identificação (nome do líder, nome do liderado e área para assinaturas) deve ocorrer exclusivamente no *front-end* no momento da geração do arquivo final.
- [ ] O PDF gerado não deve ser armazenado na nuvem da aplicação ou trafegado para os servidores da IA.

## 3. Motor de Gamificação
- [ ] Ao processar o resumo das entregas e o contexto da reunião, o sistema deve obrigatoriamente gerar um bloco de "Encerramento Gamificado".
- [ ] Este bloco deve conter três elementos de *gamification* visíveis na interface:
  - **Métrica de Progressão:** Pontuação (XP) atrelada ao esforço recente.
  - **Reconhecimento:** Um "Badge" (selo/conquista) focado em uma entrega real relatada na pauta.
  - **Desafio Próximo Ciclo:** Uma "Missão" clara e acionável para a próxima quinzena.

## 4. Jornada em Tela Única (UX e Engajamento)
- [ ] O fluxo completo do usuário (preparação pré-reunião, visualização do roteiro de apoio, preenchimento de dados reais e download da ata) deve acontecer em uma única página contínua (*Single Page Application*).
- [ ] O sistema não deve exigir navegação para telas secundárias ou abertura de abas externas, garantindo que o líder mantenha o foco e reduzindo a carga cognitiva.

## 5. Captura de Telemetria (Logs Ocultos)
- [ ] A cada roteiro gerado com sucesso, a plataforma deve registrar silenciosamente uma nova linha em um arquivo de log local (ex: arquivo CSV isolado) para telemetria.
- [ ] O log deve conter estritamente metadados estratégicos: Data/Hora, Perfil do Líder selecionado, Perfil Comportamental do Liderado, Senioridade e *flag* se a Ata em PDF foi baixada.
- [ ] É terminantemente proibido salvar o conteúdo textual dos resumos ou das conversas geradas, fornecendo insumos para o *People Analytics* do RH sem comprometer a privacidade das 1:1s.