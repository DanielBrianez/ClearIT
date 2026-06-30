# Decisões Tomadas — Bootstrap e Análise de Gaps

## Decisão 1: Bootstrap Não-Destrutivo
- **Contexto**: O projeto possuía documentações prévias de negócio e engenharia.
- **Opções Consideradas**:
  - Opção A: Substituir tudo pela documentação padrão do Onion.
  - Opção B: Mesclar os arquivos não conflitantes, mantendo a prioridade para as definições de produto do Onion, preservando os arquivos antigos e salvando tudo na nova estrutura `*-lite.md`.
- **Decisão**: Opção B.
- **Justificativa**: Garante que o histórico e as particularidades técnicas (como telemetria detalhada) do desenvolvedor da ClearIT sejam reaproveitados sem comprometer a integridade das features e metas do Onion.
- **Impacto**: O diretório `docs/` agora conta com arquivos consolidados unificados, prontos para a leitura do orquestrador.

## Decisão 2: Congelamento de Código & Relatório de Gaps
- **Contexto**: O desenvolvedor solicitou que o código atual não sofresse alterações, mas que fossem exibidos os desvios técnicos em relação à especificação ideal do Onion.
- **Opções Consideradas**:
  - Opção A: Iniciar refatorações automáticas.
  - Opção B: Criar um documento dedicado de análise de gaps e mapear os trechos exatos de arquivos a serem corrigidos em sprints futuras.
- **Decisão**: Opção B.
- **Justificativa**: Cumpre estritamente a solicitação do usuário de manter o código intocado, gerando valor analítico estruturado direto no workspace de desenvolvimento.
- **Impacto**: Criação do arquivo [onion-gap-analysis.md](file:///c:/Users/Pulse%20Mais/24+1/ClearIT/docs/onion-gap-analysis.md).
