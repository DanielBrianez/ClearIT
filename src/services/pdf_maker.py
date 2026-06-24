from fpdf import FPDF
from datetime import datetime
import re
import os

def limpar_texto(texto):
    """
    Remove marcações de Markdown, títulos internos e emojis, 
    deixando o texto puro e corporativo para o PDF.
    """
    if not texto: return ""
    
    # 1. Apaga tags de estrutura da IA (agora blindado contra variações)
    texto = re.sub(r'(?i).*PARTE 2.*?RESUMO DO ALINHAMENTO.*', '', texto)
    texto = re.sub(r'(?i)--- ATA OFICIAL ---', '', texto)
    
    # 2. Transforma asteriscos que indicam listas em hífens (-)
    texto = re.sub(r'^\s*\*\s+', '- ', texto, flags=re.MULTILINE)
    
    # 3. Aniquila TODOS os asteriscos restantes (negrito e itálico)
    texto = texto.replace('*', '')
    
    # 4. Remove hashtags de títulos Markdown (###)
    texto = re.sub(r'#+\s*', '', texto)
    
    # 5. Remove emojis silenciosamente
    texto = str(texto).encode('latin-1', 'ignore').decode('latin-1')
    
    # 6. Limpa quebras de linha em excesso
    texto = re.sub(r'\n{3,}', '\n\n', texto)
    
    return texto.strip()

def gerar_pdf(nome_lider, nome_liderado, texto_ata):
    pdf = FPDF()
    pdf.add_page()
    
    lider_limpo = limpar_texto(nome_lider)
    liderado_limpo = limpar_texto(nome_liderado)
    texto_limpo = limpar_texto(texto_ata)
    
    # --- NOVO CORTE INTELIGENTE ---
    # Procura por "Gamificação" independente de como a IA tenha escrito
    match = re.search(r'(?i)(bloco de )?gamifica[çc][ãa]o', texto_limpo)
    
    if match:
        texto_resumo = texto_limpo[:match.start()].strip()
        texto_gamificacao = texto_limpo[match.end():].strip()
        # Limpa um eventual hífen que sobrou no começo da gamificação
        texto_gamificacao = re.sub(r'^-\s*', '', texto_gamificacao).strip()
    else:
        texto_resumo = texto_limpo
        texto_gamificacao = ""
    
    # ================= PÁGINA 1: A ATA =================
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Ata Oficial de 1:1 - Clear IT', 0, 1, 'C')
    pdf.ln(5)
    
    pdf.set_font("Arial", 'B', 11)
    pdf.cell(0, 6, f"Data: {datetime.now().strftime('%d/%m/%Y')}", 0, 1)
    pdf.cell(0, 6, f"Lider: {lider_limpo}", 0, 1)
    pdf.cell(0, 6, f"Liderado: {liderado_limpo}", 0, 1)
    
    pdf.ln(3)
    pdf.cell(0, 0, "", "T") # Linha divisória
    pdf.ln(6)
    
    pdf.set_font("Arial", '', 11)
    pdf.multi_cell(0, 7, texto_resumo)
    
    # ================= PÁGINA 2: GAMIFICAÇÃO =================
    if texto_gamificacao:
        pdf.add_page()
        
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, 'Gamificação e Próximos Passos', 0, 1, 'C')
        pdf.ln(5)
        
        pdf.set_font("Arial", '', 11)
        pdf.multi_cell(0, 7, texto_gamificacao)
    
    # --- ASSINATURAS ---
    pdf.ln(25) 
    
    if pdf.get_y() > 250:
        pdf.add_page()
        
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(90, 10, "_"*40, 0, 0, 'C')
    pdf.cell(90, 10, "_"*40, 0, 1, 'C')
    pdf.cell(90, 5, "Assinatura Lider", 0, 0, 'C')
    pdf.cell(90, 5, "Assinatura Liderado", 0, 1, 'C')
    
    os.makedirs("temp", exist_ok=True)
    nome_arquivo = f"temp_ata_{liderado_limpo.replace(' ', '_')}.pdf"
    caminho_arquivo = os.path.join("temp", f"Ata_1a1_{liderado_limpo.replace(' ', '_')}.pdf")
    pdf.output(caminho_arquivo)
    pdf.output(nome_arquivo)
    
    return nome_arquivo
    return caminho_arquivo
    
    
   