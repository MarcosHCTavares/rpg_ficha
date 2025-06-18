# core/config.py

# ======= CONFIGURAÇÕES GERAIS =======

# Nome da pasta onde os dados dos personagens serão salvos
PASTA_DADOS = "dados_personagens"

# Nome padrão do jogo/sistema
SISTEMA = "RPG Ficha Digital"

# Versão do sistema
VERSAO = "1.0.0"

# Definição dos atributos principais
ATRIBUTOS_PADRAO = [
    "Força",
    "Destreza",
    "Constituição",
    "Inteligência",
    "Sabedoria",
    "Carisma"
]

# Lista de perícias disponíveis (baseadas em D&D 5e)
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

# Slots máximos de magias por nível (ajustável por classe)
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

# Cores ou estilos para futura interface (console, web, etc.)
CORES_TEMA = {
    "titulo": "azul",
    "texto": "branco",
    "erro": "vermelho",
    "sucesso": "verde"
}

# ======= CONFIGURAÇÕES FUTURAS (PLACEHOLDER) =======
# Definições de combate, equipamentos, PDF, API, banco de dados, etc.

