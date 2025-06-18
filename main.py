from core.atributos import Atributos
from core.personagem import Personagem
from core.arquivo import salvar_personagem, carregar_personagem
from pathlib import Path


def criar_personagem():
    print("\n=== Criação de Personagem ===")
    nome = input("Nome do personagem: ").strip()
    classe = input("Classe (ex: Mago, Guerreiro, Druida): ").strip().capitalize()
    nivel = int(input("Nível do personagem: ").strip())

    print("\nDistribua os atributos (valor entre 8 e 18)")
    atributos = {}
    for attr in ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]:
        while True:
            try:
                valor = int(input(f"{attr}: "))
                if 8 <= valor <= 18:
                    atributos[attr] = valor
                    break
                else:
                    print("Valor inválido. Insira entre 8 e 18.")
            except:
                print("Valor inválido. Tente novamente.")

    atributos_obj = Atributos(**atributos)

    personagem = Personagem(
        nome=nome,
        nivel=nivel,
        atributos=atributos_obj,
        proficiencia=2,  # Pode ser calculado por nível depois
        classe_nome=classe
    )

    print("\nPerícias treinadas (digite 'fim' para parar)")
    while True:
        p = input("Perícia: ").strip()
        if p.lower() == 'fim':
            break
        try:
            personagem.habilidades.treinar_pericia(p)
            print(f"✔ {p} adicionada.")
        except Exception as e:
            print(f"❌ Erro: {e}")

    print("\nSalvaguardas treinadas (digite 'fim' para parar)")
    while True:
        s = input("Atributo para salvaguarda: ").strip()
        if s.lower() == 'fim':
            break
        try:
            personagem.habilidades.treinar_salvaguarda(s)
            print(f"✔ {s} adicionada.")
        except Exception as e:
            print(f"❌ Erro: {e}")

    print("\nPersonagem criado com sucesso!")
    return personagem


def mostrar_personagem(personagem: Personagem):
    print(f"\n==== FICHA DE {personagem.nome} ====")
    print(f"Classe: {personagem.classe.nome}")
    print(f"Nível: {personagem.nivel}")
    print("\n--- Atributos ---")
    for nome, valor in personagem.atributos.atributos.items():
        mod = personagem.atributos.modificador(nome)
        print(f"{nome}: {valor} (mod {mod:+})")

    print("\n--- Perícias ---")
    for linha in personagem.habilidades.listar_pericias():
        print(linha)

    print("\n--- Salvaguardas ---")
    for linha in personagem.habilidades.listar_salvaguardas():
        print(linha)

    print("\n--- Magias Disponíveis ---")
    magias = personagem.listar_magias()
    if magias:
        for m in magias:
            print(f"- {m}")
    else:
        print("Nenhuma magia disponível.")


def menu():
    personagem = None

    while True:
        print("\n==== RPG Ficha Digital ====")
        print("1. Criar novo personagem")
        print("2. Carregar personagem")
        print("3. Mostrar ficha do personagem")
        print("4. Salvar personagem")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            personagem = criar_personagem()

        elif opcao == "2":
            nome_arquivo = input("Nome do arquivo (ex: personagem.json): ").strip()
            caminho = Path("output/fichas_salvas") / nome_arquivo
            try:
                personagem = carregar_personagem(str(caminho))
                print(f"✔ Personagem '{personagem.nome}' carregado com sucesso!")
            except Exception as e:
                print(f"❌ Erro ao carregar personagem: {e}")

        elif opcao == "3":
            if personagem:
                mostrar_personagem(personagem)
            else:
                print("❗ Nenhum personagem carregado.")

        elif opcao == "4":
            if personagem:
                nome_arquivo = input("Nome do arquivo para salvar (ex: personagem.json): ").strip()
                caminho = Path("output/fichas_salvas") / nome_arquivo
                salvar_personagem(personagem, str(caminho))
                print(f"✔ Personagem salvo em {caminho}")
            else:
                print("❗ Nenhum personagem para salvar.")

        elif opcao == "5":
            print("Saindo do RPG Ficha Digital...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
