# atributos.py

class Atributos:
    """
    Classe para gerenciar os 6 atributos principais de um personagem de RPG.
    """

    def __init__(self, forca=10, destreza=10, constituicao=10,
                 inteligencia=10, sabedoria=10, carisma=10):
        self.valores = {
            'Força': forca,
            'Destreza': destreza,
            'Constituição': constituicao,
            'Inteligência': inteligencia,
            'Sabedoria': sabedoria,
            'Carisma': carisma
        }

    def obter_valor(self, atributo):
        """
        Retorna o valor do atributo.
        """
        return self.valores.get(atributo, None)

    def definir_valor(self, atributo, valor):
        """
        Define um novo valor para o atributo.
        """
        if atributo in self.valores:
            self.valores[atributo] = valor
        else:
            raise ValueError(f"Atributo '{atributo}' não existe.")

    def modificador(self, atributo):
        """
        Calcula e retorna o modificador do atributo.
        Fórmula: (atributo - 10) // 2
        """
        valor = self.obter_valor(atributo)
        if valor is None:
            raise ValueError(f"Atributo '{atributo}' não existe.")
        return (valor - 10) // 2

    def todos_modificadores(self):
        """
        Retorna um dicionário com todos os modificadores dos atributos.
        """
        return {atributo: self.modificador(atributo) for atributo in self.valores}

    def __str__(self):
        """
        Retorna uma string com os atributos e seus modificadores.
        """
        linhas = []
        for atributo, valor in self.valores.items():
            mod = self.modificador(atributo)
            linhas.append(f"{atributo}: {valor} (Mod: {mod:+})")
        return "\n".join(linhas)


# 🚀 Teste rápido do módulo
if __name__ == "__main__":
    atributos = Atributos(forca=15, destreza=14, constituicao=13,
                           inteligencia=12, sabedoria=10, carisma=8)

    print("Atributos do Personagem:")
    print(atributos)

    print("\nModificador de Força:", atributos.modificador("Força"))

    atributos.definir_valor("Carisma", 16)
    print("\nApós alterar Carisma para 16:")
    print(atributos)
