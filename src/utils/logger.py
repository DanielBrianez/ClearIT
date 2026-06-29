import os
import csv
from datetime import datetime

# Define o caminho do arquivo de log na raiz do projeto
LOG_FILE_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "data", "telemetry_logs.csv")

def registrar_log_1a1(id_rito, nome_lider, area_lider, perfil_lider, nivel_liderado, tempo_casa, perfil_comportamental, contem_pdi=False, ata_baixada=False):
    """Grava os metadados da reunião no arquivo CSV para o RH (Sem nomes dos liderados ou dados sensíveis do time)."""
    
    # Garante que a pasta 'data' existe
    os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True)
    
    arquivo_existe = os.path.isfile(LOG_FILE_PATH)
    
    with open(LOG_FILE_PATH, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")
        
        # Cria o cabeçalho se o arquivo for novo
        if not arquivo_existe:
            writer.writerow([
                "ID_Rito",
                "Data_Hora", 
                "Nome_Lider",
                "Area_Lider",
                "Perfil_Lider", 
                "Senioridade_Liderado", 
                "Tempo_Casa", 
                "Perfil_Comportamental", 
                "Contem_PDI",
                "Ata_Baixada"
            ])
            
        # Adiciona a linha de log
        writer.writerow([
            id_rito,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            nome_lider,
            area_lider,
            perfil_lider,
            nivel_liderado,
            tempo_casa,
            perfil_comportamental,
            "Sim" if contem_pdi else "Não",
            "Sim" if ata_baixada else "Não"
        ])

def marcar_ata_baixada(id_rito):
    """Lê o arquivo telemetry_logs.csv, encontra o rito pelo id_rito e marca como baixado (Ata_Baixada = Sim)."""
    if not os.path.isfile(LOG_FILE_PATH):
        return False
        
    linhas = []
    atualizado = False
    
    with open(LOG_FILE_PATH, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        linhas = list(reader)
        
    if not linhas:
        return False
        
    # Identifica o índice da coluna ID_Rito e Ata_Baixada no cabeçalho
    cabecalho = linhas[0]
    try:
        idx_id = cabecalho.index("ID_Rito")
        idx_ata = cabecalho.index("Ata_Baixada")
    except ValueError:
        return False
        
    for i in range(1, len(linhas)):
        if linhas[i][idx_id] == str(id_rito):
            linhas[i][idx_ata] = "Sim"
            atualizado = True
            break
            
    if atualizado:
        with open(LOG_FILE_PATH, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerows(linhas)
        return True
        
    return False