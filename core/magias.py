import json
from pathlib import Path


class Magia:
    """
    Representa uma magia individual.
    """
    def __init__(self, dados):
        self.nome = dados.get("nome")
        self.nivel = dados.get("nivel")
        self.escola = dados.get("escola")
        self.tempo_conjuracao = dados.get("tempo_conjuracao")
        self.alcance = dados.get("alcance")
        self.componentes = dados.get("componentes", [])
        self.materiais = dados.get("materiais", "")
        self.duracao = dados.get("duracao")
        self.descricao = dados.get("descricao")
        self.classes = dados.get("classes", [])

    def __str__(self):
        comp = ", ".join(self.componentes)
        materiais = f" (Materiais: {self.materiais})" if self.materiais else ""
        return (
            f"🪄 {self.nome} (Nível {self.nivel} - {self.escola})\n"
            f"Conjuração: {self.tempo_conjuracao}\n"
            f"Alcance: {self.alcance}\n"
            f"Componentes: {comp}{materiais}\n"
            f"Duração: {self.duracao}\n"
            f"Descrição: {self.descricao}\n"
            f"Classes: {', '.join(self.classes)}"
        )


class BibliotecaMagias
