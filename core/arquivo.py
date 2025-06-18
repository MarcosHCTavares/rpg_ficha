import json
from pathlib import Path
from typing import List, Optional

from core.personagem import Personagem
from core.atributos import Atributos

# Diretórios padrão de saída
PASTA_SAIDA = Path("output")
PASTA_FICHAS = PASTA_SAIDA / "fichas_salvas"
PASTA_PDFS = PASTA_SAIDA / "pdfs_gerados"

# Cria as pastas, se não existirem
for pasta in [PASTA_SAIDA, PASTA_FICHAS, PASTA_PDFS]:
    pasta.mkdir(parents=True, exist_ok=True)


def salvar_personagem(personagem: Personagem, caminho: Optional[Path] = None) -> Path:
    """
    Salva os dados do personagem em arquivo JSON.
    Se o caminho não for informado, salva em 'output/fichas_salvas/{nome}.json'.

    Retorna o Path do arquivo salvo.
    """
    if caminho is None:
        nome_arquivo = f"{personagem.nome.replace(' ', '_').lower()}.json"
        caminho = PASTA_FICHAS / nome_arquivo

    dados = {
        "nome": personagem.nome,
        "nivel": personagem.nivel,
        "proficiencia": personagem.proficiencia,
        "atributos": personagem.atributos.atributos,
        "pericias_treinadas": personagem.habilidades.pericias_treinadas,
        "salvaguardas_treinadas": personagem.habilidades.salvaguardas_treinadas,
        # TODO: adicionar magias, inventário, outras infos se precisar
    }
    try:
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)
    except Exception as e:
        raise IOError(f"Erro ao salvar personagem em {caminho}: {e}")

    return caminho


def carregar_personagem(caminho: Path) -> Personagem:
    """
    Carrega um personagem de arquivo JSON.
    Lança exceção se não conseguir ler ou o arquivo estiver corrompido.
    """
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            dados = json.load(f)
    except Exception as e:
        raise IOError(f"Erro ao carregar personagem de {caminho}: {e}")

    atributos = Atributos(**dados.get("atributos", {}))
    personagem = Personagem(
        nome=dados.get("nome", "Desconhecido"),
        nivel=dados.get("nivel", 1),
        atributos=atributos,
        proficiencia=dados.get("proficiencia", 2)
    )
    # Restaurar perícias e salvaguardas treinadas
    for pericia in dados.get("pericias_treinadas", []):
        personagem.adicionar_pericia_treinada(pericia)
    for salv in dados.get("salvaguardas_treinadas", []):
        personagem.adicionar_salvaguarda_treinada(salv)

    return personagem


def listar_fichas_salvas() -> List[Path]:
    """
    Retorna uma lista dos arquivos de ficha salvos na pasta padrão.
    """
    return list(PASTA_FICHAS.glob("*.json"))


def deletar_ficha(caminho: Path) -> bool:
    """
    Deleta o arquivo da ficha. Retorna True se deletou, False se não existia.
    """
    try:
        caminho.unlink()
        return True
    except FileNotFoundError:
        return False


# Exemplo rápido e teste do módulo
if __name__ == "__main__":
    from core.atributos import Atributos
    from core.personagem import Personagem

    atributos = Atributos(forca=15, destreza=14, constituicao=13,
                         inteligencia=12, sabedoria=10, carisma=8)

    p = Personagem("Thorin", nivel=3, atributos=atributos, proficiencia=2)
    p.adicionar_pericia_treinada("Percepção")
    p.adicionar_salvaguarda_treinada("Sabedoria")

    caminho_salvo = salvar_personagem(p)
    print(f"Personagem salvo em: {caminho_salvo}")

    carregado = carregar_personagem(caminho_salvo)
    print(f"Personagem carregado: {carregado.nome}, Nível {carregado.nivel}")
    print("Perícias treinadas:", carregado.habilidades.pericias_treinadas)
    print("Fichas salvas:", listar_fichas_salvas())
