from fpdf import FPDF
from datetime import datetime

class AtaPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'Ata Oficial de 1:1 - Clear IT', 0, 1, 'C')
        self.ln(5)

def gerar_pdf(texto_ata, nome_lider, nome_liderado):
    pdf = AtaPDF()
    pdf.add_page()
    
    # Cabeçalho com dados sensíveis (LGPD - Só local)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 8, f"Data: {datetime.now().strftime('%d/%m/%Y')}", 0, 1)
    pdf.cell(0, 8, f"Líder: {nome_lider}", 0, 1)
    pdf.cell(0, 8, f"Liderado: {nome_liderado}", 0, 1)
    pdf.ln(10)
    
    # Corpo da Ata
    pdf.set_font("Arial", '', 11)
    # Tratamento simples para caracteres especiais no FPDF
    texto_limpo = texto_ata.encode('latin-1', 'replace').decode('latin-1')
    pdf.multi_cell(0, 8, texto_limpo)
    
    pdf.ln(20)
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(90, 10, "_"*40, 0, 0, 'C')
    pdf.cell(90, 10, "_"*40, 0, 1, 'C')
    pdf.cell(90, 5, "Assinatura Líder", 0, 0, 'C')
    pdf.cell(90, 5, "Assinatura Liderado", 0, 1, 'C')
    
    return pdf.output(dest='S').encode('latin-1')