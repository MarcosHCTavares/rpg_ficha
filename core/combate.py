# combate.py

from atributos import Atributos


class Combate:
    """
    Gerencia os aspectos de combate do personagem:
    Pontos de Vida, Classe de Armadura, Iniciativa, Dados de Vida e Ataques.
    """

    def __init__(self, atributos: Atributos, nivel=1, dados_vida="d8", ca_base=10):
        """
        atributos: instância da classe Atributos
        nivel: nível atual do personagem
        dados_vida: tipo de dado de vida da classe (ex.: 'd8', 'd10')
        ca_base: base da Classe de Armadura (sem armadura)
        """
        self.atributos = atributos
        self.nivel = nivel
        self.dados_vida = dados_vida  # Ex.: 'd8', 'd10'
        self.ca_base = ca_base

        # Pontos de Vida
        self.pv_maximo = self.calcular_pv_maximo()
        self.pv_atual = self.pv_maximo
        self.pv_temporario = 0

        # Iniciativa
        self.iniciativa = self.atributos.modificador('Destreza')

        # Classe de Armadura
        self.ca = self.calcular_ca()

    # 🚩 ----- Cálculos principais -----

    def calcular_pv_maximo(self):
        """
        Calcula o PV máximo inicial (nível 1) + PV por nível.
        Fórmula simplificada: dado cheio no primeiro nível + (dado médio + mod de CON) * níveis adicionais.
        """
        dado = int(self.dados_vida[1:])  # Extrai o número do dado (ex.: 'd8' -> 8)
        mod_con = self.atributos.modificador('Constituição')

        pv = dado  # Primeiro nível é o dado cheio
        if self.nivel > 1:
            pv += ( ((dado // 2) + 1 + mod_con) * (self.nivel - 1) )
        pv += mod_con  # Bônus de Constituição no nível 1

        return max(pv, 1)

    def calcular_ca(self, armadura_bonus=0, escudo_bonus=0):
        """
        Calcula a Classe de Armadura.
        Fórmula base: 10 + Destreza + bônus de armadura + bônus de escudo.
        """
        mod_dex = self.atributos.modificador('Destreza')
        return self.ca_base + mod_dex + armadura_bonus + escudo_bonus

    # 🚩 ----- Gestão de PV -----

    def receber_dano(self, dano):
        """
        Aplica dano ao personagem.
        Primeiro reduz PV temporário, depois PV atual.
        """
        if self.pv_temporario > 0:
            if dano <= self.pv_temporario:
                self.pv_temporario -= dano
                dano = 0
            else:
                dano -= self.pv_temporario
                self.pv_temporario = 0

        self.pv_atual = max(self.pv_atual - dano, 0)

    def curar(self, quantidade):
        """
        Cura o personagem até o PV máximo.
        """
        self.pv_atual = min(self.pv_atual + quantidade, self.pv_maximo)

    def adicionar_pv_temporario(self, quantidade):
        """
        Adiciona PV temporário (não acumula com os atuais, apenas substitui se maior).
        """
        if quantidade > self.pv_temporario:
            self.pv_temporario = quantidade

    # 🚩 ----- Representação -----

    def __str__(self):
        return (f"PV: {self.pv_atual}/{self.pv_maximo} (Temp: {self.pv_temporario})\n"
                f"CA: {self.ca}\n"
                f"Iniciativa: {self.iniciativa:+}\n"
                f"Dado de Vida: {self.dados_vida} x {self.nivel}")

# 🚀 Teste rápido do módulo
if __name__ == "__main__":
    from atributos import Atributos

    atributos = Atributos(forca=15, destreza=14, constituicao=13,
                           inteligencia=12, sabedoria=10, carisma=8)

    combate = Combate(atributos, nivel=3, dados_vida='d10')

    print("=== Combate Inicial ===")
    print(combate)

    print("\nRecebe 8 de dano...")
    combate.receber_dano(8)
    print(combate)

    print("\nCura 5 PV...")
    combate.curar(5)
    print(combate)

    print("\nAdiciona 6 PV temporário...")
    combate.adicionar_pv_temporario(6)
    print(combate)

    print("\nRecebe 10 de dano...")
    combate.receber_dano(10)
    print(combate)
