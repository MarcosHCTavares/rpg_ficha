# core/personagem.py

from core.atributos import Atributos
from core.habilidades import Habilidades
from core.magias import Magias
from core.inventario import Inventario
from core.combate import Combate

class Personagem:
    """
    Representa um personagem de RPG completo,
    contendo atributos, habilidades, magias, inventário e combate.
    """
    def __init__(
        self,
        nome: str,
        nivel: int = 1,
        atributos: Atributos = None,
        proficiencia: int = 2
    ):
        self.nome = nome
        self.nivel = nivel

        # Atributos do personagem (Força, Destreza, etc)
        self.atributos = atributos if atributos else Atributos()

        # Bônus de proficiência padrão (geralmente baseado no nível)
        self.proficiencia = proficiencia

        # Instâncias dos subsistemas
        self.habilidades = Habilidades(self.atributos, proficiencia=self.proficiencia)
        self.magias = Magias(proficiencia=self.proficiencia)
        self.inventario = Inventario()
        self.combate = Combate(self.atributos, self.inventario, proficiencia=self.proficiencia)

    def atualizar_proficiencia(self, novo_bonus: int):
        """Atualiza o bônus de proficiência em todos os subsistemas."""
        self.proficiencia = novo_bonus
        self.habilidades.proficiencia = novo_bonus
        self.magias.proficiencia = novo_bonus
        self.combate.proficiencia = novo_bonus

    def info_basica(self) -> str:
        """Retorna uma string resumida do personagem."""
        return f"{self.nome} (Nível {self.nivel})"

    def status_vida(self) -> str:
        """Retorna pontos de vida atuais e máximos."""
        return f"HP: {self.combate.pontos_vida_atual}/{self.combate.pontos_vida_max}"

    def adicionar_pericia_treinada(self, pericia_nome: str):
        """Adiciona perícia treinada."""
        self.habilidades.treinar_pericia(pericia_nome)

    def adicionar_salvaguarda_treinada(self, atributo_nome: str):
        """Adiciona salvaguarda treinada."""
        self.habilidades.treinar_salvaguarda(atributo_nome)

    # Aqui você pode adicionar métodos para interagir com magias, inventário e combate,
    # como lançar magia, adicionar/remover itens, atacar, etc.

# Exemplo de uso rápido
if __name__ == "__main__":
    atributos = Atributos(forca=15, destreza=14, constituicao=13,
                         inteligencia=12, sabedoria=10, carisma=8)

    p = Personagem("Thorin", nivel=3, atributos=atributos, proficiencia=2)
    p.adicionar_pericia_treinada("Percepção")
    p.adicionar_salvaguarda_treinada("Sabedoria")

    print(p.info_basica())
    print(p.status_vida())

    print("Perícias treinadas:")
    print(p.habilidades.listar_pericias())

    print("Salvaguardas treinadas:")
    print(p.habilidades.listar_salvaguardas())
