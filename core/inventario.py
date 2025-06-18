# inventario.py

from atributos import Atributos


class Item:
    """
    Representa um item genérico do inventário.
    """
    def __init__(self, nome, peso=0.0, quantidade=1, descricao=""):
        self.nome = nome
        self.peso = peso
        self.quantidade = quantidade
        self.descricao = descricao

    @property
    def peso_total(self):
        return self.peso * self.quantidade

    def __str__(self):
        return f"{self.nome} x{self.quantidade} ({self.peso_total} kg)"


class Inventario:
    """
    Gerencia os itens, armas, moedas e a carga do personagem.
    """
    def __init__(self, atributos: Atributos):
        self.atributos = atributos
        self.itens = []
        self.moedas = {'PP': 0, 'PC': 0, 'PE': 0, 'PO': 0, 'PL': 0}  # Moedas padrão D&D 5e

    # 🚩 ----- Gestão de Itens -----

    def adicionar_item(self, item: Item):
        """
        Adiciona um item ao inventário. Se já existir, soma a quantidade.
        """
        for i in self.itens:
            if i.nome == item.nome:
                i.quantidade += item.quantidade
                return
        self.itens.append(item)

    def remover_item(self, nome, quantidade=1):
        """
        Remove quantidade de um item. Remove completamente se chegar a zero.
        """
        for i in self.itens:
            if i.nome == nome:
                if i.quantidade <= quantidade:
                    self.itens.remove(i)
                else:
                    i.quantidade -= quantidade
                return
        raise ValueError(f"Item '{nome}' não encontrado no inventário.")

    # 🚩 ----- Gestão de Moedas -----

    def adicionar_moeda(self, tipo, quantidade):
        if tipo in self.moedas:
            self.moedas[tipo] += quantidade
        else:
            raise ValueError(f"Tipo de moeda '{tipo}' inválido.")

    def remover_moeda(self, tipo, quantidade):
        if tipo in self.moedas:
            if self.moedas[tipo] >= quantidade:
                self.moedas[tipo] -= quantidade
            else:
                raise ValueError(f"Moeda insuficiente ({tipo}).")
        else:
            raise ValueError(f"Tipo de moeda '{tipo}' inválido.")

    # 🚩 ----- Peso e Carga -----

    def peso_total(self):
        return sum(item.peso_total for item in self.itens)

    def carga_maxima(self):
        """
        Carga máxima = Força * 7,5 (regras simplificadas)
        """
        return self.atributos.obter_valor('Força') * 7.5

    def status_carga(self):
        peso = self.peso_total()
        carga = self.carga_maxima()

        if peso <= carga * 0.5:
            return "Leve"
        elif peso <= carga:
            return "Carregado"
        else:
            return "Sobrecarregado"

    # 🚩 ----- Visualização -----

    def listar_itens(self):
        return [str(item) for item in self.itens]

    def listar_moedas(self):
        return ", ".join([f"{v} {k}" for k, v in self.moedas.items()])

    def __str__(self):
        linhas = ["=== Inventário ==="]
        if self.itens:
            for item in self.itens:
                linhas.append(str(item))
        else:
            linhas.append("Nenhum item.")

        linhas.append(f"\nMoedas: {self.listar_moedas()}")
        linhas.append(f"Peso Total: {self.peso_total():.2f} kg")
        linhas.append(f"Carga Máxima: {self.carga_maxima():.2f} kg")
        linhas.append(f"Status de Carga: {self.status_carga()}")
        return "\n".join(linhas)


# 🚀 Teste rápido do módulo
if __name__ == "__main__":
    from atributos import Atributos

    atributos = Atributos(forca=15, destreza=14, constituicao=13,
                           inteligencia=12, sabedoria=10, carisma=8)

    inventario = Inventario(atributos)

    # Adiciona itens
    inventario.adicionar_item(Item("Espada Longa", peso=1.5, quantidade=1))
    inventario.adicionar_item(Item("Corda", peso=4.5, quantidade=1))
    inventario.adicionar_item(Item("Poção de Cura", peso=0.5, quantidade=3))

    # Adiciona moedas
    inventario.adicionar_moeda('PO', 150)
    inventario.adicionar_moeda('PC', 200)

    print(inventario)

    # Remoções
    print("\nRemovendo uma Poção de Cura...")
    inventario.remover_item("Poção de Cura")
    print(inventario)

    print("\nRemovendo 50 PO...")
    inventario.remover_moeda('PO', 50)
    print(inventario)
