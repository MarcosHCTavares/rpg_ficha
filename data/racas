from typing import Dict, List, Optional


class SubRaca:
    def __init__(self, nome: str, modificadores: Dict[str, int], habilidades: List[str]):
        self.nome = nome
        self.modificadores = modificadores
        self.habilidades = habilidades

    def __str__(self):
        return f"Sub-raça: {self.nome}"


class Raca:
    def __init__(
        self,
        nome: str,
        descricao: str,
        modificadores: Dict[str, int],
        habilidades: List[str],
        sub_racas: Optional[List[SubRaca]] = None,
    ):
        self.nome = nome
        self.descricao = descricao
        self.modificadores = modificadores
        self.habilidades = habilidades
        self.sub_racas = sub_racas or []

    def get_sub_raca(self, nome_sub: str) -> Optional[SubRaca]:
        for sr in self.sub_racas:
            if sr.nome.lower() == nome_sub.lower():
                return sr
        return None

    def __str__(self):
        return f"Raça: {self.nome}"


# Exemplo com algumas raças e sub-raças D&D 5e

HUMANO = Raca(
    nome="Humano",
    descricao="Versátil e adaptável, recebem +1 em todos os atributos.",
    modificadores={
        "forca": 1,
        "destreza": 1,
        "constituicao": 1,
        "inteligencia": 1,
        "sabedoria": 1,
        "carisma": 1,
    },
    habilidades=["Versatilidade: ganha uma perícia extra"],
)

ELFO = Raca(
    nome="Elfo",
    descricao="Ágil, sensível à magia e com visão no escuro.",
    modificadores={
        "destreza": 2,
    },
    habilidades=[
        "Visão no Escuro",
        "Imunidade a Sono",
        "Transe (4 horas de descanso em vez de 8)"
    ],
    sub_racas=[
        SubRaca(
            nome="Alto Elfo",
            modificadores={"inteligencia": 1},
            habilidades=["Truques adicionais com magia"],
        ),
        SubRaca(
            nome="Elfo da Floresta",
            modificadores={"sabedoria": 1},
            habilidades=["Passos silenciosos", "Movimentação rápida na floresta"],
        ),
        SubRaca(
            nome="Elfo Negro (Drow)",
            modificadores={"carisma": 1},
            habilidades=["Visão no Escuro superior", "Resistência a magia", "Magias raciais"],
        ),
    ],
)

ANAO = Raca(
    nome="Anão",
    descricao="Robustos e resistentes, excelentes em trabalhos manuais.",
    modificadores={
        "constituicao": 2,
    },
    habilidades=[
        "Visão no Escuro",
        "Resistência a veneno",
        "Proficiência com ferramentas"
    ],
    sub_racas=[
        SubRaca(
            nome="Anão da Colina",
            modificadores={"sabedoria": 1},
            habilidades=["Pontos de vida extras"],
        ),
        SubRaca(
            nome="Anão das Montanhas",
            modificadores={"forca": 2},
            habilidades=["Proficiência com armaduras pesadas"],
        ),
    ],
)

DRACONATO = Raca(
    nome="Draconato",
    descricao="Descendentes de dragões, fortes e imponentes.",
    modificadores={
        "forca": 2,
        "carisma": 1,
    },
    habilidades=[
        "Sopro de Dragão",
        "Resistência elemental (dependendo do tipo de dragão)"
    ],
)

# Lista completa para facilitar busca e uso
TODAS_RACAS = [
    HUMANO,
    ELFO,
    ANAO,
    DRACONATO,
    # adicionar outras raças conforme necessário
]


def buscar_raca(nome: str) -> Optional[Raca]:
    nome = nome.lower()
    for raca in TODAS_RACAS:
        if raca.nome.lower() == nome:
            return raca
    return None


# Teste rápido do módulo
if __name__ == "__main__":
    r = buscar_raca("Elfo")
    print(f"Raça: {r.nome} - {r.descricao}")
    print("Modificadores:", r.modificadores)
    print("Habilidades:", ", ".join(r.habilidades))
    print("Sub-raças:")
    for sr in r.sub_racas:
        print(f"  {sr.nome} - Modificadores: {sr.modificadores}, Habilidades: {', '.join(sr.habilidades)}")
