# core/pericias.py

from core.config import PERICIAS_PADRAO


class Habilidades:
    """
    Gerencia as perícias (skills) do personagem.
    """

    def __init__(self):
        # Lista das perícias treinadas
        self.pericias_treinadas = []

    def adicionar(self, pericia):
        """
        Adiciona uma perícia treinada ao personagem,
        desde que ela seja válida e não esteja duplicada.
        """
        if pericia not in PERICIAS_PADRAO:
            raise ValueError(f"Perícia '{pericia}' não existe.")
        if pericia not in self.pericias_treinadas:
            self.pericias_treinadas.append(pericia)

    def remover(self, pericia):
        """
        Remove uma perícia treinada, se existir.
        """
        if pericia in self.pericias_treinadas:
            self.pericias_treinadas.remove(pericia)

    def listar(self):
        """
        Retorna a lista de perícias treinadas.
        """
        return self.pericias_treinadas.copy()

    def possui(self, pericia):
        """
        Verifica se o personagem tem determinada perícia treinada.
        """
        return pericia in self.pericias_treinadas

    def __str__(self):
        if not self.pericias_treinadas:
            return "Nenhuma perícia treinada."
        return ", ".join(self.pericias_treinadas)
