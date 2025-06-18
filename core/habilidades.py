# habilidades.py

from atributos import Atributos
from rolagem import Rolagem


# 📜 Lista padrão de perícias D&D 5e
PERICIAS = {
    'Acrobacia': 'Destreza',
    'Arcanismo': 'Inteligência',
    'Atletismo': 'Força',
    'Atuação': 'Carisma',
    'Enganação': 'Carisma',
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


class Habilidades:
    """
    Gerencia perícias, testes de atributos e salvaguardas.
    """
    def __init__(self, atributos: Atributos, proficiencia=2):
        """
        atributos: instância de Atributos
        proficiencia: bônus de proficiência (nível do personagem)
        """
        self.atributos = atributos
        self.proficiencia = proficiencia

        # Perícias treinadas
        self.pericias_treinadas = []

        # Salvaguardas treinadas (resistências)
        self.salvaguardas_treinadas = []

    # 🚩 ----- Gestão de perícias e salvaguardas -----

    def treinar_pericia(self, nome):
        if nome in PERICIAS:
            self.pericias_treinadas.append(nome)
        else:
            raise ValueError(f"Perícia '{nome}' não existe.")

    def treinar_salvaguarda(self, atributo):
        if atributo in self.atributos.atributos:
            self.salvaguardas_treinadas.append(atributo)
        else:
            raise ValueError(f"Atributo '{atributo}' inválido.")

    # 🚩 ----- Rolagens -----

    def teste_pericia(self, nome, vantagem=None):
        """
        Rola um teste de perícia.
        """
        if nome not in PERICIAS:
            raise ValueError(f"Perícia '{nome}' não existe.")

        atributo = PERICIAS[nome]
        bonus = self.atributos.modificador(atributo)

        if nome in self.pericias_treinadas:
            bonus += self.proficiencia

        resultado = Rolagem.rolar_ataque(bonus, vantagem)
        return resultado

    def teste_atributo(self, atributo, vantagem=None):
        """
        Teste bruto de atributo (sem perícia).
        """
        if atributo not in self.atributos.atributos:
            raise ValueError(f"Atributo '{atributo}' inválido.")

        bonus = self.atributos.modificador(atributo)
        resultado = Rolagem.rolar_ataque(bonus, vantagem)
        return resultado

    def salvaguarda(self, atributo, vantagem=None):
        """
        Teste de resistência (salvaguarda).
        """
        if atributo not in self.atributos.atributos:
            raise ValueError(f"Atributo '{atributo}' inválido.")

        bonus = self.atributos.modificador(atributo)
        if atributo in self.salvaguardas_treinadas:
            bonus += self.proficiencia

        resultado = Rolagem.rolar_ataque(bonus, vantagem)
        return resultado

    # 🚩 ----- Visualização -----

    def listar_pericias(self):
        """
        Lista perícias e seus bônus atuais.
        """
        linhas = []
        for nome, atributo in PERICIAS.items():
            mod = self.atributos.modificador(atributo)
            bonus = mod + (self.proficiencia if nome in self.pericias_treinadas else 0)
            linhas.append(f"{nome} ({atributo}): {bonus:+}")
        return linhas

    def listar_salvaguardas(self):
        """
        Lista salvaguardas e seus bônus.
        """
        linhas = []
        for atributo in self.atributos.atributos.keys():
            mod = self.atributos.modificador(atributo)
            bonus = mod + (self.proficiencia if atributo in self.salvaguardas_treinadas else 0)
            linhas.append(f"{atributo}: {bonus:+}")
        return linhas


# 🚀 Teste rápido do módulo
if __name__ == "__main__":
    from atributos import Atributos

    atributos = Atributos(forca=14, destreza=12, constituicao=13,
                           inteligencia=10, sabedoria=16, carisma=8)

    habilidades = Habilidades(atributos, proficiencia=2)

    habilidades.treinar_pericia('Percepção')
    habilidades.treinar_pericia('Furtividade')
    habilidades.treinar_salvaguarda('Sabedoria')
    habilidades.treinar_salvaguarda('Constituição')

    print("=== Perícias ===")
    for linha in habilidades.listar_pericias():
        print(linha)

    print("\n=== Salvaguardas ===")
    for linha in habilidades.listar_salvaguardas():
        print(linha)

    print("\nTeste de Percepção (com vantagem):")
    r = habilidades.teste_pericia('Percepção', vantagem=True)
    print(Rolagem.rolagem_texto(r))

    print("\nTeste de Salvaguarda de Constituição:")
    r = habilidades.salvaguarda('Constituição')
    print(Rolagem.rolagem_texto(r))
