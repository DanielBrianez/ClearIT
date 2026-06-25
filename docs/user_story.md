# 📌 História de Usuário (User Story)

**Feature:** Geração Segura e Personalizada de Roteiros de 1:1 e Atas (MVP)  
**Status:** Pronto para Dev  

---

## 📖 Narrativa

> **Como** gestor ou líder técnico na Clear IT,  
> **Eu quero** inserir rapidamente o contexto comportamental e de projeto da minha equipe,  
> **Para que** a IA me forneça um roteiro de condução empático e gamificado, gerando uma ata em PDF segura (LGPD) sem que eu precise gastar horas planejando.

---

## ✅ Critérios de Aceite (Acceptance Criteria)

### 1. Desempenho de Geração (Eficiência)
* **Critério:** O sistema deve gerar e renderizar o roteiro completo na tela em até 10 segundos após o clique.
* **Método:** Teste de performance via interface (*Network Tab*).
* **Baseline:** Atualmente o líder leva cerca de 30 a 40 minutos para redigir um roteiro manual.

### 2. Conformidade LGPD (Segurança de Dados)
* **Critério:** Os nomes reais preenchidos na seção de "Ata Oficial" não devem ser enviados no payload da API do Gemini sob nenhuma hipótese.
* **Método:** *Code review* e inspeção de tráfego de rede (*Network Monitor*).
* **Baseline:** Risco zero de vazamento de identificadores diretos.

### 3. Estabilidade de Interface (UX e Prevenção de Erros)
* **Critério:** Durante o tempo de processamento da IA (*spinner* ativo), a interface de inputs deve ser "congelada" para impedir perda de dados ou sobrecarga de cliques.
* **Método:** Teste manual e automatizado de UI.
* **Baseline:** Zero erros de *Rate Limit* causados por duplo clique do usuário.

### 4. Completude da Ata (Validação de Negócio)
* **Critério:** O PDF gerado para download deve obrigatoriamente formatar e incluir a seção de Gamificação (+XP e Badges) e remover marcações brutas da IA (ex: `--- ATA OFICIAL ---`).
* **Método:** Download e validação visual de QA do arquivo `.pdf`.
* **Baseline:** O PDF gerado deve estar pronto para assinatura digital/física sem necessidade de edição textual pós-download.