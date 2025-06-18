from typing import List, Optional


class Classe:
    def __init__(
        self,
        nome: str,
        descricao: str,
        pontos_vida_por_nivel: int,
        atributos_principais: List[str],
        pericias_disponiveis: List[str],
        habilidades_classe: List[str],
    ):
        self.nome = nome
        self.descricao = descricao
        self.pontos_vida_por_nivel = pontos_vida_por_nivel
        self.atributos_principais = atributos_principais
        self.pericias_disponiveis = pericias_disponiveis
        self.habilidades_classe = habilidades_classe

    def __str__(self):
        return f"Classe: {self.nome}"


# Classes Oficiais D&D 5e (sem subclasses)

BARBARO = Classe(
    nome="Barbaro",
    descricao="Guerreiro feroz que utiliza a fúria em combate.",
    pontos_vida_por_nivel=12,
    atributos_principais=["Força", "Constituição"],
    pericias_disponiveis=["Atletismo", "Intimidação", "Sobrevivência", "Furtividade"],
    habilidades_classe=[
        "Fúria",
        "Defesa sem Armadura",
        "Ataque Selvagem",
        "Sentidos Aguçados",
        "Camuflagem na Natureza",
    ],
)

BARD = Classe(
    nome="Bardo",
    descricao="Artista e inspirador, mestre em magia e música.",
    pontos_vida_por_nivel=8,
    atributos_principais=["Carisma", "Destreza"],
    pericias_disponiveis=[
        "Acrobacia",
        "Arcanismo",
        "Atuação",
        "Enganação",
        "História",
        "Intimidação",
        "Intuição",
        "Investigação",
        "Lidar com Animais",
        "Medicina",
        "Natureza",
        "Percepção",
        "Persuasão",
        "Prestidigitação",
        "Religião",
        "Sobrevivência",
    ],
    habilidades_classe=[
        "Inspirar Coragem",
        "Magia de Bardo",
        "Conhecimento Enciclopédico",
        "Magias de Curandeiro",
    ],
)

CLERIGO = Classe(
    nome="Clérigo",
    descricao="Servidor divino que conjura magias para proteger e curar.",
    pontos_vida_por_nivel=8,
    atributos_principais=["Sabedoria", "Carisma"],
    pericias_disponiveis=[
        "História",
        "Intuição",
        "Medicina",
        "Persuasão",
        "Religião",
    ],
    habilidades_classe=[
        "Magia Divina",
        "Canalizar Divindade",
        "Domínio Divino",
        "Intercessão Divina",
    ],
)

DRUIDA = Classe(
    nome="Druida",
    descricao="Guardião da natureza, capaz de se transformar em animais.",
    pontos_vida_por_nivel=8,
    atributos_principais=["Sabedoria", "Constituição"],
    pericias_disponiveis=[
        "Arcanismo",
        "Intuição",
        "Medicina",
        "Natureza",
        "Percepção",
        "Religião",
        "Sobrevivência",
    ],
    habilidades_classe=[
        "Magia de Druida",
        "Forma Selvagem",
        "Conexão com a Natureza",
    ],
)

GUE = Classe(
    nome="Guerreiro",
    descricao="Especialista em combate corpo a corpo e armas pesadas.",
    pontos_vida_por_nivel=10,
    atributos_principais=["Força", "Destreza"],
    pericias_disponiveis=[
        "Acrobacia",
        "Atletismo",
        "Intimidação",
        "Percepção",
        "Sobrevivência",
    ],
    habilidades_classe=[
        "Estilo de Luta",
        "Segundo Sopro",
        "Ação Surpresa",
        "Ataque Extra",
        "Indomável",
    ],
)

LADINO = Classe(
    nome="Ladino",
    descricao="Especialista em furtividade, ataques rápidos e habilidades furtivas.",
    pontos_vida_por_nivel=8,
    atributos_principais=["Destreza", "Carisma"],
    pericias_disponiveis=[
        "Acrobacia",
        "Furtividade",
        "Atuação",
        "Enganação",
        "Intuição",
        "Investigação",
        "Percepção",
        "Prestidigitação",
    ],
    habilidades_classe=[
        "Ataque Furtivo",
        "Evasão",
        "Ação Bônus",
        "Especialização",
    ],
)

MAGO = Classe(
    nome="Mago",
    descricao="Usuário de magias arcanas poderosas e versáteis.",
    pontos_vida_por_nivel=6,
    atributos_principais=["Inteligência", "Sabedoria"],
    pericias_disponiveis=[
        "Arcanismo",
        "História",
        "Investigação",
        "Religião",
    ],
    habilidades_classe=[
        "Magia Arcana",
        "Truques",
        "Conjuração de Magia",
        "Conhecimento Arcano",
    ],
)

MONGE = Classe(
    nome="Monge",
    descricao="Artista marcial disciplinado com habilidades místicas.",
    pontos_vida_por_nivel=8,
    atributos_principais=["Destreza", "Sabedoria"],
    pericias_disponiveis=[
        "Acrobacia",
        "Atletismo",
        "Furtividade",
        "Religião",
    ],
    habilidades_classe=[
        "Artes Marciais",
        "Defesa sem Armadura",
        "Ki",
        "Movimento Acelerado",
        "Ataques Desarmados",
    ],
)

PALADINO = Classe(
    nome="Paladino",
    descricao="Guerreiro sagrado que combina força e fé.",
    pontos_vida_por_nivel=10,
    atributos_principais=["Força", "Carisma"],
    pericias_disponiveis=[
        "Intimidação",
        "Medicina",
        "Persuasão",
        "Religião",
    ],
    habilidades_classe=[
        "Aura de Proteção",
        "Imposição das Mãos",
        "Magia Divina",
        "Sentido Divino",
    ],
)

RANGER = Classe(
    nome="Ranger",
    descricao="Caçador e explorador mestre em combate à distância e rastreamento.",
    pontos_vida_por_nivel=10,
    atributos_principais=["Destreza", "Sabedoria"],
    pericias_disponiveis=[
        "Atletismo",
        "Furtividade",
        "Intuição",
        "Investigação",
        "Natureza",
        "Percepção",
        "Sobrevivência",
    ],
    habilidades_classe=[
        "Inimigo Predileto",
        "Exploração Natural",
        "Ataque Extra",
        "Magia de Ranger",
    ],
)

SORCERER = Classe(
    nome="Feiticeiro",
    descricao="Usuário de magia inata e poderosa.",
    pontos_vida_por_nivel=6,
    atributos_principais=["Carisma", "Constituição"],
    pericias_disponiveis=[
        "Atuação",
        "Enganação",
        "Intuição",
        "Religião",
    ],
    habilidades_classe=[
        "Origem Mágica",
        "Magia Inata",
        "Metamagia",
        "Reservas de Feitiços",
    ],
)

WARLOCK = Classe(
    nome="Bruxo",
    descricao="Usuário de magia concedida por pacto com entidades sobrenaturais.",
    pontos_vida_por_nivel=8,
    atributos_principais=["Carisma", "Constituição"],
    pericias_disponiveis=[
        "Arcano",
        "Enganação",
        "História",
        "Intimidação",
        "Religião",
    ],
    habilidades_classe=[
        "Pacto Sobrenatural",
        "Magia de Bruxo",
        "Invocações",
    ],
)

TODAS_CLASSES = [
    BARBARO,
    BARD,
    CLERIGO,
    DRUIDA,
    GUE,
    LADINO,
    MAGO,
    MONGE,
    PALADINO,
    RANGER,
    SORCERER,
    WARLOCK,
]


def buscar_classe(nome: str) -> Optional[Classe]:
    nome = nome.lower()
    for classe in TODAS_CLASSES:
        if classe.nome.lower() == nome:
            return classe
    return None


if __name__ == "__main__":
    c = buscar_classe("Mago")
    if c:
        print(f"Classe: {c.nome}")
        print(f"Descrição: {c.descricao}")
        print(f"Pontos de vida por nível: {c.pontos_vida_por_nivel}")
        print(f"Atributos principais: {', '.join(c.atributos_principais)}")
        print(f"Perícias disponíveis: {', '.join(c.pericias_disponiveis)}")
        print(f"Habilidades de classe: {', '.join(c.habilidades_classe)}")
    else:
        print("Classe não encontrada.")
