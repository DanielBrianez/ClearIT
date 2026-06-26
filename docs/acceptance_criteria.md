# ✅ Critérios de Aceite (Acceptance Criteria) - MVP Clear IT

Este documento define os requisitos técnicos e de negócio que devem ser atendidos para que a versão inicial (MVP) do Assistente de Liderança seja considerada "Pronta" (*Done*).

## 1. Personalização e Segurança (LGPD)
- [x] O sistema deve gerar um roteiro de 1:1 adaptado dinamicamente aos três perfis de liderança mapeados (Técnico, Em transição, Engajado) e ao contexto comportamental do liderado.
- [x] A comunicação com a IA deve ser processada utilizando estritamente contexto comportamental.
- [x] É terminantemente proibida a inserção de dados sensíveis (nomes reais, CPF, questões de saúde) no *prompt* enviado ao LLM, garantindo *Privacy by Design*.
- [x] Alimentar um *front-end* com banco de dados com o nome do liderado pra facilitar o preenchimento da Ata e envio.
- [ ] Modificação da ata para enviar exclusivamente para o RH com dados para os ciclos de calibração de performance.

## 2. Geração da Ata Oficial (Governança)
- [x] O sistema deve permitir a geração e o download de uma "Ata de Alinhamento" no formato PDF diretamente pelo navegador.
- [x] A injeção de dados sensíveis de identificação (nome do líder, nome do liderado e área para assinaturas) deve ocorrer exclusivamente no *front-end* no momento da geração do arquivo final.
- [x] O PDF gerado não deve ser armazenado na nuvem da aplicação ou trafegado para os servidores da IA.
- [ ] O sistema deve disponibilizar um gatilho rápido no *front-end* (ex: integração com cliente de e-mail local ou botão de copiar link/texto) para que o líder envie a Ata de Alinhamento diretamente ao liderado assim que gerada. 
- [ ] O bloco de telemetria deve registrar um evento anônimo quando a ação de "Compartilhar Ata com Liderado" for acionada, permitindo calcular a Taxa de Documentação (Total de Atas Compartilhadas / Total de Roteiros Gerados). 

## 3. Jornada em Tela Única (UX e Engajamento)
- [x] O fluxo completo do usuário (preparação pré-reunião, visualização do roteiro de apoio, preenchimento de dados reais e download da ata) deve acontecer em uma única página contínua (*Single Page Application*).
- [x] O sistema não deve exigir navegação para telas secundárias ou abertura de abas externas, garantindo que o líder mantenha o foco e reduzindo a carga cognitiva.
- [ ] Depois da finalização da ata, o usuário é automaticamente direcionado para a *dashboard* “Meu perfil”, para ver seu progresso.

## 4. Captura de Telemetria (Logs Ocultos)
- [x] A cada roteiro gerado com sucesso, a plataforma deve registrar silenciosamente uma nova linha em um arquivo de log local (ex: arquivo CSV isolado) para telemetria.
- [x] O log deve conter estritamente metadados estratégicos: Data/Hora, Perfil do Líder selecionado, Perfil Comportamental do Liderado, Senioridade e *flag* se a Ata em PDF foi baixada.
- [x] É terminantemente proibido salvar o conteúdo textual dos resumos ou das conversas geradas, fornecendo insumos para o *People Analytics* do RH sem comprometer a privacidade das 1:1s.
- [ ] Colocar o RH em cópia nos e-mails. 
- [ ] O sistema deve disponibilizar uma ação explícita e imediata pós-geração do PDF (ex: botão "Compartilhar Ata" ou cópia automática de sumário formatado para a área de transferência) que permita ao líder enviar o documento ou o resumo do alinhamento diretamente ao liderado.
- [ ] A execução da ação de compartilhamento descrita acima deve disparar um evento anônimo para o arquivo de telemetria local (ex: `flag_compartilhado = true`), garantindo que o RH consiga auditar a Taxa de Documentação e Transparência sem expor o conteúdo da conversa.
- [ ] Telemetria (Logs Ocultos) captura se o líder engajou, aceitou ou concluiu essas missões. 
- [ ] **Para o liderado:** Para medir a Relevância Percebida o liderado recebe uma pergunta de avaliação sobre a relevância percebida como: *"Essa reunião foi útil?"* depois de cada reunião.