# core/magias.py

import json
from pathlib import Path


class Magia:
    def __init__(self, nome, nivel=0, escola=None, descricao="", alcance="", componentes="", duracao=""):
        self.nome = nome
        self.nivel = nivel
        self.escola = escola
        self.descricao = descricao
        self.alcance = alcance
        self.componentes = componentes
        self.duracao = duracao

    def __str__(self):
        return f"{self.nome} (Nível {self.nivel}) - {self.escola}"


class Magias:
    def __init__(self, caminho_magias="data/magias.json"):
        self.magias_conhecidas = []
        self.magias_disponiveis = {}
        self._carregar_magias(caminho_magias)

    def _carregar_magias(self, caminho):
        path = Path(caminho)
        if not path.exists():
            raise FileNotFoundError(f"Arquivo de magias não encontrado: {caminho}")
        with open(path, "r", encoding="utf-8") as f:
            dados = json.load(f)
            for m in dados:
                magia = Magia(
                    nome=m.get("nome", "Desconhecida"),
                    nivel=m.get("nivel", 0),
                    escola=m.get("escola", ""),
                    descricao=m.get("descricao", ""),
                    alcance=m.get("alcance", ""),
                    componentes=m.get("componentes", ""),
                    duracao=m.get("duracao", ""),
                )
                self.magias_disponiveis[magia.nome] = magia

    def aprender(self, nome_magia):
        if nome_magia not in self.magias_disponiveis:
            raise ValueError(f"Magia '{nome_magia}' não está disponível.")
        if nome_magia not in self.magias_conhecidas:
            self.magias_conhecidas.append(nome_magia)

    def esquecer(self, nome_magia):
        if nome_magia in self.magias_conhecidas:
            self.magias_conhecidas.remove(nome_magia)

    def listar_magias(self):
        return self.magias_conhecidas.copy()

    def obter_magia(self, nome_magia):
        return self.magias_disponiveis.get(nome_magia)

    def __str__(self):
        if not self.magias_conhecidas:
            return "Nenhuma magia conhecida."
        return "\n".join(
            f"{self.magias_disponiveis[n].nome} (Nível {self.magias_disponiveis[n].nivel})"
            for n in self.magias_conhecidas
        )
