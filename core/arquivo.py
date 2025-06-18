# core/arquivo.py

import json
from core.personagem import Personagem
from core.atributos import Atributos

def salvar_personagem(personagem: Personagem, caminho: str):
    """
    Salva os dados do personagem em arquivo JSON.
    """
    dados = {
        "nome": personagem.nome,
        "nivel": personagem.nivel,
        "proficiencia": personagem.proficiencia,
        "atributos": personagem.atributos.atributos,
        "pericias_treinadas": personagem.habilidades.pericias_treinadas,
        "salvaguardas_treinadas": personagem.habilidades.salvaguardas_treinadas,
        # Pode adicionar mais dados: magias, inventario, etc.
    }
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

def carregar_personagem(caminho: str) -> Personagem:
    """
    Carrega um personagem de arquivo JSON.
    """
    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)

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

# Exemplo rápido:
if __name__ == "__main__":
    from core.atributos import Atributos
    from core.personagem import Personagem

    atributos = Atributos(forca=15, destreza=14, constituicao=13,
                         inteligencia=12, sabedoria=10, carisma=8)

    p = Personagem("Thorin", nivel=3, atributos=atributos, proficiencia=2)
    p.adicionar_pericia_treinada("Percepção")
    p.adicionar_salvaguarda_treinada("Sabedoria")

    salvar_personagem(p, "teste_personagem.json")

    carregado = carregar_personagem("teste_personagem.json")
    print(f"Personagem carregado: {carregado.nome}, Nível {carregado.nivel}")
    print("Perícias treinadas:", carregado.habilidades.pericias_treinadas)
