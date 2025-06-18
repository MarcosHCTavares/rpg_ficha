# magia.py

from rolagem import Rolagem


class Magia:
    """
    Representa uma magia individual.
    """
    def __init__(self, nome, nivel, escola, descricao, tipo='normal',
                 dano=None, testes_resistencia=False):
        """
        nome: Nome da magia
        nivel: Nível da magia (0 = truque)
        escola: Escola de magia (Evocação, Ilusão, etc.)
        descricao: Texto descritivo
        tipo: 'normal', 'concentracao' ou 'ritual'
        dano: Ex.: ('d6', 3, '+3') -> 3d6+3
        testes_resistencia: Se a magia exige que alvo faça teste
        """
        self.nome = nome
        self.nivel = nivel
        self.escola = escola
        self.descricao = descricao
        self.tipo = tipo
        self.dano = dano
        self.testes_resistencia = testes_resistencia

    def rolar_dano(self):
        """
        Rola dano se a magia tiver dano.
        """
        if not self.dano:
            return None
        dado, quantidade, bonus = self.dano
        return Rolagem.rolar_dano(dado, quantidade, int(bonus))


class LivroDeMagias:
    """
    Gerencia as magias conhecidas e os slots disponíveis.
    """
    def __init__(self, atributo_conjuracao, bonus_proficiencia):
        """
        atributo_conjuracao: Modificador do atributo chave (Ex.: INT, SAB, CAR)
        bonus_proficiencia: Bônus de proficiência do personagem
        """
        self.atributo_conjuracao = atributo_conjuracao
        self.bonus_proficiencia = bonus_proficiencia

        self.magias_conhecidas = []
        self.slots = {nivel: 0 for nivel in range(1, 10)}

    def adicionar_magia(self, magia: Magia):
        self.magias_conhecidas.append(magia)

    def definir_slots(self, nivel, quantidade):
        if nivel not in self.slots:
            raise ValueError("Nível de magia inválido (1 a 9).")
        self.slots[nivel] = quantidade

    def usar_slot(self, nivel):
        if self.slots.get(nivel, 0) > 0:
            self.slots[nivel] -= 1
            return True
        else:
            print(f"Sem slots disponíveis de nível {nivel}.")
            return False

    def restaurar_slots(self, nivel, quantidade):
        self.slots[nivel] += quantidade

    def cd_magia(self):
        """
        Calcula a CD para resistir às magias.
        Fórmula padrão D&D 5e: 8 + bônus de proficiência + modificador atributo
        """
        return 8 + self.bonus_proficiencia + self.atributo_conjuracao

    def bonus_ataque_magico(self):
        """
        Bônus para ataques mágicos.
        """
        return self.bonus_proficiencia + self.atributo_conjuracao

    def listar_magias(self):
        """
        Lista todas as magias conhecidas.
        """
        linhas = []
        for magia in self.magias_conhecidas:
            linhas.append(f"{magia.nome} (Nível {magia.nivel}) - {magia.escola}")
        return linhas

    def listar_slots(self):
        """
        Lista os slots restantes.
        """
        return {nivel: qnt for nivel, qnt in self.slots.items() if qnt > 0}


# 🚀 Teste rápido do módulo
if __name__ == "__main__":
    # Suponha que atributo de conjuração tem modificador +3, proficiência +2
    livro = LivroDeMagias(atributo_conjuracao=3, bonus_proficiencia=2)

    # Definir slots (exemplo de um mago de nível baixo)
    livro.definir_slots(1, 2)

    # Adicionar magias
    bola_de_fogo = Magia(
        nome="Bola de Fogo",
        nivel=3,
        escola="Evocação",
        descricao="Explosão de fogo causando dano em área.",
        dano=('d6', 8, '+0'),
        testes_resistencia=True
    )

    misseis_magicos = Magia(
        nome="Mísseis Mágicos",
        nivel=1,
        escola="Evocação",
        descricao="Dardos de energia mágica que acertam automaticamente.",
        dano=('d4', 3, '+3')
    )

    livro.adicionar_magia(bola_de_fogo)
    livro.adicionar_magia(misseis_magicos)

    print("=== Magias Conhecidas ===")
    for linha in livro.listar_magias():
        print(linha)

    print("\n=== Slots ===")
    print(livro.listar_slots())

    print("\nCD de Magia:", livro.cd_magia())
    print("Bônus de Ataque Mágico:", livro.bonus_ataque_magico())

    print("\nLançando Mísseis Mágicos:")
    if livro.usar_slot(1):
        r = misseis_magicos.rolar_dano()
        print(Rolagem.rolagem_texto(r))

    print("\nSlots após conjuração:")
    print(livro.listar_slots())
