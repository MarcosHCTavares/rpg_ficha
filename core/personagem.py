# personagem.py

from atributos import Atributos
from habilidades import Habilidades
from magia import LivroDeMagias, Magia
from rolagem import Rolagem


class Personagem:
    """
    Classe principal que representa o personagem completo.
    """
    def __init__(self, nome, classe, nivel, raca,
                 forca, destreza, constituicao, inteligencia, sabedoria, carisma,
                 atributo_conjuracao=None):
        self.nome = nome
        self.classe = classe
        self.nivel = nivel
        self.raca = raca

        # Cálculo de proficiência
        self.proficiencia = self.calcular_bonus_proficiencia()

        # Atributos
        self.atributos = Atributos(
            forca=forca,
            destreza=destreza,
            constituicao=constituicao,
            inteligencia=inteligencia,
            sabedoria=sabedoria,
            carisma=carisma
        )

        # Habilidades
        self.habilidades = Habilidades(self.atributos, self.proficiencia)

        # Magias (se for conjurador)
        if atributo_conjuracao:
            modificador_conjuracao = self.atributos.modificador(atributo_conjuracao)
            self.livro_de_magias = LivroDeMagias(modificador_conjuracao, self.proficiencia)
        else:
            self.livro_de_magias = None

        # Vida e combate (básico inicial)
        self.pv_maximo = 10 + self.atributos.modificador('Constituição') * self.nivel
        self.pv_atual = self.pv_maximo
        self.ca = 10 + self.atributos.modificador('Destreza')

    def calcular_bonus_proficiencia(self):
        """
        Fórmula oficial D&D 5e
        """
        return 2 + ((self.nivel - 1) // 4)

    def status(self):
        """
        Retorna o status geral do personagem.
        """
        return {
            'Nome': self.nome,
            'Raça': self.raca,
            'Classe': self.classe,
            'Nível': self.nivel,
            'PV': f"{self.pv_atual}/{self.pv_maximo}",
            'CA': self.ca,
            'Proficiencia': self.proficiencia
        }

    def ficha_resumida(self):
        """
        Retorna uma ficha simples em texto.
        """
        linhas = []
        info = self.status()
        for k, v in info.items():
            linhas.append(f"{k}: {v}")

        linhas.append("\nAtributos:")
        for attr, valor in self.atributos.atributos.items():
            mod = self.atributos.modificador(attr)
            linhas.append(f"  {attr}: {valor} ({mod:+})")

        linhas.append("\nPerícias:")
        linhas.extend(self.habilidades.listar_pericias())

        linhas.append("\nSalvaguardas:")
        linhas.extend(self.habilidades.listar_salvaguardas())

        if self.livro_de_magias:
            linhas.append("\nMagias Conhecidas:")
            linhas.extend(self.livro_de_magias.listar_magias())

            linhas.append("\nSlots de Magia:")
            slots = self.livro_de_magias.listar_slots()
            linhas.append(str(slots))

        return "\n".join(linhas)


# 🚀 Teste rápido do módulo
if __name__ == "__main__":
    # Criar personagem mago
    personagem = Personagem(
        nome="Eldrin",
        classe="Mago",
        nivel=3,
        raca="Elfo",
        forca=8,
        destreza=14,
        constituicao=13,
        inteligencia=16,
        sabedoria=10,
        carisma=12,
        atributo_conjuracao="Inteligência"
    )

    # Treinar perícias e salvaguardas
    personagem.habilidades.treinar_pericia('Percepção')
    personagem.habilidades.treinar_pericia('Investigação')
    personagem.habilidades.treinar_salvaguarda('Inteligência')
    personagem.habilidades.treinar_salvaguarda('Sabedoria')

    # Configurar magias
    personagem.livro_de_magias.definir_slots(1, 4)
    personagem.livro_de_magias.definir_slots(2, 2)

    # Adicionar magias
    personagem.livro_de_magias.adicionar_magia(
        Magia(
            nome="Mísseis Mágicos",
            nivel=1,
            escola="Evocação",
            descricao="Dardos mágicos que acertam automaticamente.",
            dano=('d4', 3, '+3')
        )
    )

    personagem.livro_de_magias.adicionar_magia(
        Magia(
            nome="Imagem Espelhada",
            nivel=2,
            escola="Ilusão",
            descricao="Cria ilusões para confundir inimigos."
        )
    )

    personagem.livro_de_magias.adicionar_magia(
        Magia(
            nome="Bola de Fogo",
            nivel=3,
            escola="Evocação",
            descricao="Explosão de fogo causando dano em área.",
            dano=('d6', 8, '+0'),
            testes_resistencia=True
        )
    )

    # Mostrar ficha
    print(personagem.ficha_resumida())
