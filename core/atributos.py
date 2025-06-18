# core/atributos.py

from core.config import ATRIBUTOS_PADRAO


class Atributos:
    """
    Gerencia os atributos principais do personagem.
    """

    def __init__(self, valores=None):
        """
        Inicializa os atributos do personagem.
        :param valores: dicionário opcional com valores iniciais
        """
        if valores is None:
            valores = {}

        # Gera os atributos com valores padrão (10) se não fornecido
        self.atributos = {
            atributo: valores.get(atributo, 10) for atributo in ATRIBUTOS_PADRAO
        }

    def definir_atributo(self, nome, valor):
        """
        Define um valor para um atributo.
        """
        if nome not in ATRIBUTOS_PADRAO:
            raise ValueError(f"Atributo '{nome}' não é válido.")
        self.atributos[nome] = valor

    def obter_atributo(self, nome):
        """
        Retorna o valor atual de um atributo.
        """
        if nome not in ATRIBUTOS_PADRAO:
            raise ValueError(f"Atributo '{nome}' não existe.")
        return self.atributos[nome]

    def modificador(self, nome):
        """
        Retorna o modificador de um atributo (padrão D&D).
        Fórmula: (atributo - 10) // 2
        """
        valor = self.obter_atributo(nome)
        return (valor - 10) // 2

    def todos(self):
        """
        Retorna um dicionário com todos os atributos e seus valores.
        """
        return self.atributos.copy()

    def __str__(self):
        """
        Retorna uma representação em string dos atributos e modificadores.
        """
        linhas = []
        for nome in ATRIBUTOS_PADRAO:
            valor = self.atributos[nome]
            mod = self.modificador(nome)
            linhas.append(f"{nome}: {valor} ({mod:+})")
        return "\n".join(linhas)
