from typing import Dict, List, Optional


class SubClasse:
    def __init__(self, nome: str, descricao: str, habilidades: List[str]):
        self.nome = nome
        self.descricao = descricao
        self.habilidades = habilidades

    def __str__(self):
        return f"Subclasse: {self.nome}"


class Classe:
    def __init__(
        self,
        nome: str,
        descricao: str,
        pontos_vida_por_nivel: int,
        pericias_disponiveis: List[str],
        habilidades_classe: List[str],
        sub_classes: Optional[List[SubClasse]] = None,
    ):
        self.nome = nome
        self.descricao = descricao
        self.pontos_vida_por_nivel = pontos_vida_por_nivel
        self.pericias_disponiveis = pericias_disponiveis
        self.habilidades_classe = habilidades_classe
        self.sub_classes = sub_classes or []

    def get_sub_classe(self, nome_sub: str) -> Optional[SubClasse]:
        for sc in self.sub_classes:
            if sc.nome.lower() == nome_sub.lower():
                return sc
        return None

    def __str__(self):
        return f"Classe: {self.nome}"


# Exemplos de classes e subclasses de D&D 5e

GUERREIRO = Classe(
    nome="Guerreiro",
    descricao="Especialista em combate corpo a corpo e armas pesadas.",
    pontos_vida_por_nivel=10,
    pericias_disponiveis=["Atletismo", "Intimidação", "Percepção", "Sobrevivência", "História"],
    habilidades_classe=["Estilo de Luta", "Ação Surpresa", "Segundo Sopro"],
    sub_classes=[
        SubClasse(
            nome="Campeão",
            descricao="Focado em aperfeiçoamento físico e resistência.",
            habilidades=["Aprimoramento de Critico", "Atleta Inato"],
        ),
        SubClasse(
            nome="Mestre de Batalha",
            descricao="Tático e versátil, usa manobras de combate.",
            habilidades=["Manobras de Combate", "Superiores"],
        ),
        SubClasse(
            nome="Cavaleiro Arcano",
            descricao="Combina magia e combate.",
            habilidades=["Magia Arcana", "Defesa Arcana"],
        ),
    ],
)

MAGO = Classe(
    nome="Mago",
    descricao="Usuário de magias arcanas poderosas.",
    pontos_vida_por_nivel=6,
    pericias_disponiveis=["Arcanismo", "História", "Investigação", "Religião"],
    habilidades_classe=["Truques", "Magia de Nível Superior", "Conjuração"],
    sub_classes=[
        SubClasse(
            nome="Escolar da Evocação",
            descricao="Focado em magias de dano direto.",
            habilidades=["Magias Evocativas Potentes"],
        ),
        SubClasse(
            nome="Escolar da Ilusão",
            descricao="Especialista em magias que enganam os sentidos.",
            habilidades=["Magias de Ilusão Aprimoradas"],
        ),
    ],
)

CLERIGO = Classe(
    nome="Clérigo",
    descricao="Canaliza poderes divinos para curar e proteger.",
    pontos_vida_por_nivel=8,
    pericias_disponiveis=["Medicina", "Religião", "Persuasão", "Intuição"],
    habilidades_classe=["Canalizar Divindade", "Magias Divinas", "Domínios Divinos"],
    sub_classes=[
        SubClasse(
            nome="Domínio da Vida",
            descricao="Focado em cura e proteção.",
            habilidades=["Cura Aprimorada", "Resistência Divina"],
        ),
        SubClasse(
            nome="Domínio da Guerra",
            descricao="Focado em combate e força divina.",
            habilidades=["Armaduras e Armas Proficientes", "Poder de Guerra"],
        ),
    ],
)

# Lista geral para busca e uso
TODAS_CLASSES = [
    GUERREIRO,
    MAGO,
    CLERIGO,
    # adicionar outras classes conforme necessário
]


def buscar_classe(nome: str) -> Optional[Classe]:
    nome = nome.lower()
    for classe in TODAS_CLASSES:
        if classe.nome.lower() == nome:
            return classe
    return None


# Teste rápido do módulo
if __name__ == "__main__":
    c = buscar_classe("Guerreiro")
    print(f"Classe: {c.nome} - {c.descricao}")
    print("Pontos de Vida por Nível:", c.pontos_vida_por_nivel)
    print("Perícias disponíveis:", ", ".join(c.pericias_disponiveis))
    print("Habilidades de classe:", ", ".join(c.habilidades_classe))
    print("Subclasses:")
    for sc in c.sub_classes:
        print(f"  {sc.nome} - {sc.descricao}")
        print(f"    Habilidades: {', '.join(sc.habilidades)}")
