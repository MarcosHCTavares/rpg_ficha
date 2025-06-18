# pericias.py

from atributos import Atributos


class Pericias:
    """
    Gerencia as perícias e testes de resistência de um personagem.
    Calcula os bônus com base nos atributos e na proficiência.
    """

    # 🎯 Tabela de perícias e seus atributos associados
    PERICIAS_ATRIBUTO = {
        'Acrobacia': 'Destreza',
        'Arcanismo': 'Inteligência',
        'Atletismo': 'Força',
        'Atuação': 'Carisma',
        'Blefar': 'Carisma',
        'Furtividade': 'Destreza',
        'História': 'Inteligência',
        'Intimidação': 'Carisma',
        'Intuição': 'Sabedoria',
        'Investigação': 'Inteligência',
        'Lidar com Animais': 'Sabedoria',
        'Medicina': 'Sabedoria',
        'Natureza': 'Inteligência',
        'Percepção': 'Sabedoria',
        'Persuasão': 'Carisma',
        'Prestidigitação': 'Destreza',
        'Religião': 'Inteligência',
        'Sobrevivência': 'Sabedoria'
    }

    # 🎯 Testes de resistência (Saving Throws)
    TESTES_RESISTENCIA = ['Força', 'Destreza', 'Constituição', 'Inteligência', 'Sabedoria', 'Carisma']

    def __init__(self, atributos: Atributos, bonus_proficiencia=2):
        """
        atributos: instância da classe Atributos
        bonus_proficiencia: bônus atual de proficiência do personagem
        """
        self.atributos = atributos
        self.bonus_proficiencia = bonus_proficiencia

        # 🟩 Marcar proficiências nas perícias e nos testes de resistência
        self.pericias_proficientes = set()
        self.resistencias_proficientes = set()

    # 🚩 ----- Gestão de proficiências -----

    def adicionar_pericia_proficiente(self, pericia):
        if pericia in self.PERICIAS_ATRIBUTO:
            self.pericias_proficientes.add(pericia)
        else:
            raise ValueError(f"Perícia '{pericia}' não existe.")

    def adicionar_resistencia_proficiente(self, atributo):
        if atributo in self.TESTES_RESISTENCIA:
            self.resistencias_proficientes.add(atributo)
        else:
            raise ValueError(f"Atributo '{atributo}' não é um teste de resistência válido.")

    # 🚩 ----- Cálculos -----

    def bonus_pericia(self, pericia):
        """
        Retorna o bônus total para uma perícia.
        """
        atributo = self.PERICIAS_ATRIBUTO.get(pericia)
        if not atributo:
            raise ValueError(f"Perícia '{pericia}' não existe.")

        mod = self.atributos.modificador(atributo)
        if pericia in self.pericias_proficientes:
            return mod + self.bonus_proficiencia
        return mod

    def bonus_resistencia(self, atributo):
        """
        Retorna o bônus total para um teste de resistência.
        """
        if atributo not in self.TESTES_RESISTENCIA:
            raise ValueError(f"Atributo '{atributo}' não é válido para resistência.")

        mod = self.atributos.modificador(atributo)
        if atributo in self.resistencias_proficientes:
            return mod + self.bonus_proficiencia
        return mod

    # 🚩 ----- Listagem -----

    def listar_pericias(self):
        """
        Retorna um dicionário com todas as perícias e seus bônus.
        """
        return {pericia: self.bonus_pericia(pericia) for pericia in self.PERICIAS_ATRIBUTO}

    def listar_resistencias(self):
        """
        Retorna um dicionário com todos os testes de resistência e seus bônus.
        """
        return {atributo: self.bonus_resistencia(atributo) for atributo in self.TESTES_RESISTENCIA}

    def __str__(self):
        linhas = ["Perícias:"]
        for pericia, bonus in self.listar_pericias().items():
            prof = "*" if pericia in self.pericias_proficientes else ""
            linhas.append(f" - {pericia}: {bonus:+} {prof}")

        linhas.append("\nTestes de Resistência:")
        for atributo, bonus in self.listar_resistencias().items():
            prof = "*" if atributo in self.resistencias_proficientes else ""
            linhas.append(f" - {atributo}: {bonus:+} {prof}")

        return "\n".join(linhas)


# 🚀 Teste rápido do módulo
if __name__ == "__main__":
    from atributos import Atributos

    atributos = Atributos(forca=15, destreza=14, constituicao=13,
                           inteligencia=12, sabedoria=10, carisma=8)

    pericias = Pericias(atributos, bonus_proficiencia=2)

    # Adicionando proficiências
    pericias.adicionar_pericia_proficiente("Atletismo")
    pericias.adicionar_pericia_proficiente("Percepção")
    pericias.adicionar_resistencia_proficiente("Força")
    pericias.adicionar_resistencia_proficiente("Constituição")

    print(pericias)
