# core/config.py

# ======= CONFIGURAÇÕES GERAIS =======

# Nome da pasta raiz onde serão salvos dados do sistema (personagens, logs, etc)
PASTA_DADOS = "dados_personagens"

# Pastas para dados específicos, podendo ser usadas no módulo arquivo.py
PASTA_FICHAS = "output/fichas_salvas"
PASTA_PDFS = "output/pdfs_gerados"

# Nome padrão do jogo/sistema
SISTEMA = "RPG Ficha Digital"

# Versão do sistema
VERSAO = "1.0.0"

# ======= ATRIBUTOS E PERÍCIAS =======

# Definição dos atributos principais, padrão D&D 5e
ATRIBUTOS_PADRAO = [
    "Força",
    "Destreza",
    "Constituição",
    "Inteligência",
    "Sabedoria",
    "Carisma"
]

# Lista de perícias baseadas em D&D 5e
PERICIAS_PADRAO = [
    "Acrobacia",
    "Arcanismo",
    "Atletismo",
    "Atuação",
    "Blefar",
    "Furtividade",
    "História",
    "Intuição",
    "Intimidação",
    "Investigação",
    "Lidar com Animais",
    "Medicina",
    "Natureza",
    "Percepção",
    "Persuasão",
    "Prestidigitação",
    "Religião",
    "Sobrevivência"
]

# Mapeamento perícias -> atributo base para facilitar cálculo de bônus
PERICIAS_ATRIBUTOS = {
    "Acrobacia": "Destreza",
    "Arcanismo": "Inteligência",
    "Atletismo": "Força",
    "Atuação": "Carisma",
    "Blefar": "Carisma",
    "Furtividade": "Destreza",
    "História": "Inteligência",
    "Intuição": "Sabedoria",
    "Intimidação": "Carisma",
    "Investigação": "Inteligência",
    "Lidar com Animais": "Sabedoria",
    "Medicina": "Sabedoria",
    "Natureza": "Inteligência",
    "Percepção": "Sabedoria",
    "Persuasão": "Carisma",
    "Prestidigitação": "Destreza",
    "Religião": "Inteligência",
    "Sobrevivência": "Sabedoria"
}

# ======= MAGIAS E SLOTS =======

# Slots máximos de magias por nível (pode ser customizado por classe e nível do personagem)
SLOTS_MAGIA_PADRAO = {
    1: 4,
    2: 3,
    3: 3,
    4: 3,
    5: 2,
    6: 2,
    7: 1,
    8: 1,
    9: 1
}

# ======= ARQUIVOS DE DADOS JSON =======

DATA_PATH = "data"

# Arquivos JSON padrão para carga de dados
JSON_FILES = {
    "racas": f"{DATA_PATH}/racas.json",
    "classes": f"{DATA_PATH}/classes.json",
    "armas": f"{DATA_PATH}/armas.json",
    "itens": f"{DATA_PATH}/itens.json",
    # Magias por classe
    "magias_bardo": f"{DATA_PATH}/magias_bardo.json",
    "magias_bruxo": f"{DATA_PATH}/magias_bruxo.json",
    "magias_clerigo": f"{DATA_PATH}/magias_clerigo.json",
    "magias_druida": f"{DATA_PATH}/magias_druida.json",
    "magias_feiticeiro": f"{DATA_PATH}/magias_feiticeiro.json",
    "magias_mago": f"{DATA_PATH}/magias_mago.json",
    "magias_paladino": f"{DATA_PATH}/magias_paladino.json",
    "magias_ranger": f"{DATA_PATH}/magias_ranger.json",
}

# ======= VISUAL E INTERFACE =======

# Cores ou estilos para interfaces (terminal, web, etc)
CORES_TEMA = {
    "titulo": "azul",
    "texto": "branco",
    "erro": "vermelho",
    "sucesso": "verde"
}

# ======= CONFIGURAÇÕES FUTURAS (PLACEHOLDERS) =======

# Configurações para combate (iniciativa, ataques múltiplos, etc)
COMBATE_CONFIG = {
    "iniciativa_bonus": 0,
    "dano_critico": True,
}

# Configurações para inventário e peso
INVENTARIO_CONFIG = {
    "peso_maximo_padrao": 50.0,  # kg
    "unidade_peso": "kg"
}

# Configurações para geração de PDFs
PDF_CONFIG = {
    "nome_arquivo_padrao": "ficha_personagem.pdf",
    "pagina_tamanho": "A4",
    "margens_cm": 2,
}

# Configurações de salvamento automático
AUTO_SAVE = True
AUTO_SAVE_INTERVAL = 300  # em segundos

# ======= FUNÇÕES UTILITÁRIAS =======

def get_json_path(nome_chave):
    """
    Retorna o caminho do arquivo JSON baseado na chave.
    """
    return JSON_FILES.get(nome_chave, None)
