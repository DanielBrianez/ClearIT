import os
import csv
from datetime import datetime

# Define o caminho do arquivo de log na raiz do projeto
LOG_FILE_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "data", "telemetry_logs.csv")

def registrar_log_1a1(perfil_lider, nivel_liderado, tempo_casa, perfil_comportamental, ata_baixada=False):
    """Grava os metadados da reunião no arquivo CSV para o RH (Sem nomes ou dados sensíveis)."""
    
    # Garante que a pasta 'data' existe
    os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True)
    
    arquivo_existe = os.path.isfile(LOG_FILE_PATH)
    
    with open(LOG_FILE_PATH, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")
        
        # Cria o cabeçalho se o arquivo for novo
        if not arquivo_existe:
            writer.writerow([
                "Data_Hora", 
                "Perfil_Lider", 
                "Senioridade_Liderado", 
                "Tempo_Casa", 
                "Perfil_Comportamental", 
                "Ata_Baixada"
            ])
            
        # Adiciona a linha de log
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            perfil_lider,
            nivel_liderado,
            tempo_casa,
            perfil_comportamental,
            "Sim" if ata_baixada else "Não"
        ])