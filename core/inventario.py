# core/inventario.py

class Item:
    def __init__(self, nome: str, peso: float = 0.0, quantidade: int = 1):
        self.nome = nome
        self.peso = peso
        self.quantidade = quantidade

    def peso_total(self):
        return self.peso * self.quantidade

    def __str__(self):
        q = f"x{self.quantidade}" if self.quantidade > 1 else ""
        return f"{self.nome} {q} (Peso total: {self.peso_total():.2f} kg)"


class Inventario:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item: Item):
        # Se o item já existe, soma as quantidades
        for existente in self.itens:
            if existente.nome == item.nome:
                existente.quantidade += item.quantidade
                return
        self.itens.append(item)

    def remover_item(self, nome: str, quantidade: int = 1):
        for item in self.itens:
            if item.nome == nome:
                if item.quantidade > quantidade:
                    item.quantidade -= quantidade
                elif item.quantidade == quantidade:
                    self.itens.remove(item)
                else:
                    raise ValueError(
                        f"Tentando remover mais {quantidade} de '{nome}' do que existe ({item.quantidade})"
                    )
                return
        raise ValueError(f"Item '{nome}' não encontrado no inventário.")

    def peso_total(self) -> float:
        return sum(item.peso_total() for item in self.itens)

    def listar_itens(self):
        return [str(item) for item in self.itens]

    def __str__(self):
        if not self.itens:
            return "Inventário vazio."
        linhas = [str(item) for item in self.itens]
        linhas.append(f"Peso total: {self.peso_total():.2f} kg")
        return "\n".join(linhas)
