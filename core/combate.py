# core/combate.py

from typing import Optional
from core.rolagem import Rolagem
from core.atributos import Atributos
from core.inventario import Inventario


class Combate:
    """
    Classe para gerenciar combate entre personagens.
    """

    def __init__(self, atributos: Atributos, inventario: Optional[Inventario] = None, proficiencia: int = 2):
        self.atributos = atributos
        self.inventario = inventario or Inventario()
        self.pontos_vida_max = 10 + atributos.modificador("Constituição")  # Exemplo base; ajustar conforme classe
        self.pontos_vida_atual = self.pontos_vida_max
        self.proficiencia = proficiencia
        self.condicoes = set()  # ex: 'envenenado', 'paralisado', etc.

    def iniciativa(self) -> dict:
        """
        Rola iniciativa (d20 + modificador de Destreza).
        """
        bonus = self.atributos.modificador("Destreza")
        resultado = Rolagem.rolar_ataque(bonus)
        return resultado

    def atacar(self, bonus_ataque: int = 0, vantagem: Optional[bool] = None) -> dict:
        """
        Rola um ataque com bônus e possibilidade de vantagem/desvantagem.
        Considera modificador de Força ou Destreza dependendo da arma (simplificado aqui como Força).
        """
        mod_forca = self.atributos.modificador("Força")
        total_bonus = mod_forca + bonus_ataque + self.proficiencia
        resultado = Rolagem.rolar_ataque(total_bonus, vantagem)
        return resultado

    def receber_dano(self, dano: int) -> None:
        """
        Aplica dano ao personagem.
        """
        self.pontos_vida_atual -= dano
        if self.pontos_vida_atual < 0:
            self.pontos_vida_atual = 0

    def curar(self, cura: int) -> None:
        """
        Aplica cura ao personagem, sem ultrapassar o máximo.
        """
        self.pontos_vida_atual += cura
        if self.pontos_vida_atual > self.pontos_vida_max:
            self.pontos_vida_atual = self.pontos_vida_max

    def esta_vivo(self) -> bool:
        """
        Retorna True se o personagem estiver com vida acima de 0.
        """
        return self.pontos_vida_atual > 0

    def aplicar_condicao(self, condicao: str) -> None:
        """
        Aplica uma condição negativa ao personagem.
        """
        self.condicoes.add(condicao)

    def remover_condicao(self, condicao: str) -> None:
        """
        Remove uma condição.
        """
        self.condicoes.discard(condicao)

    def listar_condicoes(self) -> list:
        """
        Retorna uma lista das condições atuais.
        """
        return list(self.condicoes)


# Teste rápido do módulo
if __name__ == "__main__":
    from core.atributos import Atributos
    from core.inventario import Inventario

    atributos = Atributos(forca=16, destreza=14, constituicao=12,
                          inteligencia=10, sabedoria=8, carisma=13)
    inventario = Inventario()

    combate = Combate(atributos, inventario)

    print("Iniciativa:", combate.iniciativa())
    print("Ataque:", combate.atacar(bonus_ataque=1, vantagem=True))

    combate.receber_dano(5)
    print(f"Pontos de vida após dano: {combate.pontos_vida_atual}")

    combate.curar(3)
    print(f"Pontos de vida após cura: {combate.pontos_vida_atual}")

    combate.aplicar_condicao("envenenado")
    combate.aplicar_condicao("atordoado")
    print("Condições atuais:", combate.listar_condicoes())

    combate.remover_condicao("envenenado")
    print("Condições após remover envenenado:", combate.listar_condicoes())
