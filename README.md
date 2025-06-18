## 🧙‍♂️ README.md — *RPG Ficha Digital*

```markdown
# 🎲 RPG Ficha Digital

Um gerenciador completo de fichas de RPG baseado no sistema Dungeons & Dragons 5ª edição (D&D 5e). O sistema permite criar, salvar, carregar e visualizar fichas de personagens de forma simples e eficiente, utilizando Python e dados estruturados em arquivos JSON.

---

## 🚀 Funcionalidades

- 📜 Criação de fichas de personagens com:
  - Nome, nível, classe, raça e atributos.
  - Perícias treinadas e salvaguardas.
  - Inventário básico (em desenvolvimento).
  - Listagem de magias baseada na classe do personagem.
- 💾 Salvamento e carregamento de personagens em arquivos JSON.
- 📄 Organização automática em pastas:
  - `output/fichas_salvas/` → Fichas salvas em JSON.
  - `output/pdfs_gerados/` → (futuro) geração de PDFs.
- 🎯 Sistema modular com componentes separados:
  - Atributos, Perícias, Habilidades, Magias, Combate, Inventário, Arquivo e Rolagens.
- 🔮 Leitura dinâmica de dados JSON:
  - Classes, Raças, Armas, Itens e Magias separados por classe.

---

## 🗂️ Estrutura do Projeto

```

rpg\_ficha/
│
├── core/              → Lógica central (atributos, combate, rolagens, etc.)
├── data/              → Dados JSON (classes, raças, magias, armas, itens)
├── output/            → Fichas salvas e PDFs gerados
├── ui/                → (Opcional) Interface terminal, desktop ou web
├── main.py            → Script principal com menu interativo
├── README.md          → Este arquivo
└── requirements.txt   → Dependências do projeto

````

---

## 🔧 Instalação

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/rpg-ficha-digital.git
cd rpg-ficha-digital
````

2. (Opcional) Crie um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## ▶️ Como rodar

Execute o arquivo principal:

```bash
python main.py
```

---

## 📦 Dependências

* Python 3.9 ou superior.
* `fpdf` (se desejar gerar PDFs).
* Outras bibliotecas padrão (`json`, `pathlib`, etc.).

---

## 📄 Dados incluídos (data/)

* ✅ Raças e sub-raças (`racas.json`)
* ✅ Classes e subclasses (`classes.json`)
* ✅ Armas (`armas.json`)
* ✅ Itens (`itens.json`)
* ✅ Magias organizadas por classe:

  * `magias_bardo.json`
  * `magias_bruxo.json`
  * `magias_clerigo.json`
  * `magias_druida.json`
  * `magias_feiticeiro.json`
  * `magias_mago.json`
  * `magias_paladino.json`
  * `magias_ranger.json`

---

## 🌟 Roadmap

* [x] Gerenciamento de atributos e perícias.
* [x] Sistema de magias por classe.
* [x] Salvamento e carregamento em JSON.
* [ ] Sistema de inventário avançado.
* [ ] Sistema de combate (PV, ataques, defesa).
* [ ] Geração de ficha em PDF.
* [ ] Interface Desktop (Tkinter ou PyQt).
* [ ] Interface Web (Flask/FastAPI).
* [ ] Integração com dados externos (API).

---

## 🧠 Contribuição

Sinta-se livre para abrir issues, sugestões ou contribuir com pull requests.

---

## ⚖️ Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para mais informações.

---

## ✨ Créditos

Projeto desenvolvido por **Marcos Henrique** com inspiração no sistema Dungeons & Dragons 5e.


```
