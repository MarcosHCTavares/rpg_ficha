# core/personagem.py

from core.atributos import Atributos
from core.habilidades import Habilidades
from core.magias import Magias
from core.config import ATRIBUTOS_PADRAO


class Personagem:
    def __init__(
        self,
        nome: str,
        raca: str,
        classe: str,
        nivel: int = 1,
        atributos: dict = None,
        habilidades_treinadas: list = None,
        magias_conhecidas: list = None,
        atributo_conjuracao: str = None,
    ):
        """
        Inicializa o personagem com dados básicos e sistemas integrados.

        :param nome: Nome do personagem
        :param raca: Raça do personagem
        :param classe: Classe do personagem
        :param nivel: Nível atual
        :param atributos: dict com valores dos atributos (ex: {"Força": 15})
        :param habilidades_treinadas: lista com perícias treinadas
        :param magias_conhecidas: lista com nomes das magias conhecidas
        :param atributo_conjuracao: atributo usado para conjurar magias (ex: "Sabedoria")
        """

        self.nome = nome
        self.raca = raca
        self.classe = classe
        self.nivel = nivel

        # Inicializa atributos com valores padrão ou recebidos
        self.atributos = Atributos(atributos)

        # Inicializa habilidades (perícias)
        self.habilidades = Habilidades()
        if habilidades_treinadas:
            for pericia in habilidades_treinadas:
                self.habilidades.adicionar(pericia)

        # Inicializa magias
        self.magias = Magias()
        if magias_conhecidas:
            for magia in magias_conhecidas:
                self.magias.aprender(magia)

        # Define o atributo para conjuração
        if atributo_conjuracao and atributo_conjuracao in ATRIBUTOS_PADRAO:
            self.atributo_conjuracao = atributo_conjuracao
        else:
            # padrão para magias baseadas em Sabedoria (ex: Druidas, Rangers)
            self.atributo_conjuracao = "Sabedoria"

    def modificar_nivel(self, novo_nivel: int):
        if novo_nivel < 1:
            raise ValueError("O nível do personagem deve ser pelo menos 1.")
        self.nivel = novo_nivel

    def obter_modificador(self, atributo_nome: str) -> int:
        """
        Retorna o modificador do atributo.
        """
        return self.atributos.modificador(atributo_nome)

    def treinar_pericia(self, pericia: str):
        """
        Adiciona uma perícia treinada.
        """
        self.habilidades.adicionar(pericia)

    def aprender_magia(self, magia_nome: str):
        """
        Adiciona uma magia ao personagem.
        """
        self.magias.aprender(magia_nome)

    def __str__(self):
        return (
            f"Personagem: {self.nome}\n"
            f"Raça: {self.raca}\n"
            f"Classe: {self.classe} (Nível {self.nivel})\n"
            f"Atributos:\n{self.atributos}\n"
            f"Habilidades treinadas: {', '.join(self.habilidades.listar())}\n"
            f"Magias conhecidas: {', '.join(self.magias.listar_magias())}\n"
            f"Atributo de conjuração: {self.atributo_conjuracao}"
        )
