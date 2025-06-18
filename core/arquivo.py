# core/arquivo.py

import json
from pathlib import Path


class GerenciadorDeArquivos:
    """
    Gerencia salvar e carregar personagens em arquivos JSON.
    """

    def __init__(self, pasta="dados_personagens"):
        self.pasta = Path(pasta)
        self.pasta.mkdir(exist_ok=True)

    def salvar(self, personagem, nome_arquivo=None):
        """
        Salva o personagem em um arquivo JSON.
        """
        if not nome_arquivo:
            nome_arquivo = personagem.nome.lower().replace(" ", "_") + ".json"

        caminho = self.pasta / nome_arquivo
        dados = self.serializar_personagem(personagem)

        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

        print(f"Personagem salvo em {caminho}")

    def carregar(self, nome_arquivo):
        """
        Carrega um personagem de um arquivo JSON.
        """
        caminho = self.pasta / nome_arquivo

        if not caminho.exists():
            raise FileNotFoundError(f"O arquivo {nome_arquivo} não foi encontrado.")

        with open(caminho, "r", encoding="utf-8") as f:
            dados = json.load(f)

        from personagem import Personagem  # Importação tardia para evitar problemas circulares

        personagem = Personagem(
            nome=dados['nome'],
            classe=dados['classe'],
            nivel=dados['nivel'],
            raca=dados['raca'],
            forca=dados['atributos']['Força'],
            destreza=dados['atributos']['Destreza'],
            constituicao=dados['atributos']['Constituição'],
            inteligencia=dados['atributos']['Inteligência'],
            sabedoria=dados['atributos']['Sabedoria'],
            carisma=dados['atributos']['Carisma'],
            atributo_conjuracao=dados.get('atributo_conjuracao')
        )

        personagem.pv_atual = dados.get('pv_atual', personagem.pv_maximo)

        # Restaurar perícias e salvaguardas treinadas
        personagem.habilidades.pericias_treinadas = set(dados.get('pericias_treinadas', []))
        personagem.habilidades.salvaguardas_treinadas = set(dados.get('salvaguardas_treinadas', []))

        # Restaurar magias
        if personagem.livro_de_magias:
            personagem.livro_de_magias.slots = dados.get('slots_magia', {})
            for magia in dados.get('magias_conhecidas', []):
                from magia import Magia
                personagem.livro_de_magias.adicionar_magia(
                    Magia(
                        nome=magia['nome'],
                        nivel=magia['nivel'],
                        escola=magia['escola'],
                        descricao=magia['descricao'],
                        tipo=magia.get('tipo', 'normal'),
                        dano=tuple(magia['dano']) if magia.get('dano') else None,
                        testes_resistencia=magia.get('testes_resistencia', False)
                    )
                )

        print(f"Personagem {personagem.nome} carregado com sucesso.")
        return personagem

    def listar_arquivos(self):
        """
        Lista os arquivos de personagens salvos.
        """
        return [f.name for f in self.pasta.glob("*.json")]

    def serializar_personagem(self, personagem):
        """
        Transforma o personagem em um dicionário para salvar em JSON.
        """
        dados = {
            'nome': personagem.nome,
            'classe': personagem.classe,
            'nivel': personagem.nivel,
            'raca': personagem.raca,
            'atributo_conjuracao': getattr(personagem, 'atributo_conjuracao', None),
            'atributos': personagem.atributos.atributos,
            'proficiencia': personagem.proficiencia,
            'pv_atual': personagem.pv_atual,
            'pv_maximo': personagem.pv_maximo,
            'ca': personagem.ca,
            'pericias_treinadas': list(personagem.habilidades.pericias_treinadas),
            'salvaguardas_treinadas': list(personagem.habilidades.salvaguardas_treinadas),
        }

        if personagem.livro_de_magias:
            dados['slots_magia'] = personagem.livro_de_magias.slots
            dados['magias_conhecidas'] = [
                {
                    'nome': m.nome,
                    'nivel': m.nivel,
                    'escola': m.escola,
                    'descricao': m.descricao,
                    'tipo': m.tipo,
                    'dano': list(m.dano) if m.dano else None,
                    'testes_resistencia': m.testes_resistencia
                }
                for m in personagem.livro_de_magias.magias_conhecidas
            ]

        return dados


# 🚀 Teste rápido
if __name__ == "__main__":
    from personagem import Personagem

    # Criar personagem simples
    p = Personagem(
        nome="Testador",
        classe="Guerreiro",
        nivel=2,
        raca="Anão",
        forca=16,
        destreza=12,
        constituicao=14,
        inteligencia=10,
        sabedoria=11,
        carisma=8
    )

    arquivo = GerenciadorDeArquivos()

    # Salvar
    arquivo.salvar(p)

    # Listar
    print("Arquivos disponíveis:", arquivo.listar_arquivos())

    # Carregar
    personagem_carregado = arquivo.carregar("testador.json")
    print(personagem_carregado.ficha_resumida())
