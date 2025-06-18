import tkinter as tk
from tkinter import messagebox, ttk
from core.personagem import Personagem
from core.atributos import Atributos
from core.arquivo import salvar_personagem, carregar_personagem
from pathlib import Path


class RPGApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RPG Ficha Digital")
        self.root.geometry("500x400")

        self.personagem = None

        self.criar_interface()

    def criar_interface(self):
        frame = ttk.Frame(self.root, padding=20)
        frame.pack(expand=True, fill="both")

        ttk.Label(frame, text="🎲 RPG Ficha Digital", font=("Arial", 18)).pack(pady=10)

        ttk.Button(frame, text="Criar Novo Personagem", command=self.criar_personagem).pack(fill="x", pady=5)
        ttk.Button(frame, text="Carregar Personagem", command=self.carregar_personagem).pack(fill="x", pady=5)
        ttk.Button(frame, text="Exibir Personagem", command=self.exibir_personagem).pack(fill="x", pady=5)
        ttk.Button(frame, text="Salvar Personagem", command=self.salvar_personagem).pack(fill="x", pady=5)
        ttk.Button(frame, text="Sair", command=self.root.quit).pack(fill="x", pady=20)

    def criar_personagem(self):
        janela = tk.Toplevel(self.root)
        janela.title("Novo Personagem")
        janela.geometry("400x500")

        campos = {}

        ttk.Label(janela, text="Preencha os dados", font=("Arial", 14)).pack(pady=10)

        for campo in ["Nome", "Classe", "Nível"]:
            ttk.Label(janela, text=campo).pack()
            entry = ttk.Entry(janela)
            entry.pack()
            campos[campo] = entry

        ttk.Label(janela, text="--- Atributos (8 a 18) ---").pack(pady=10)

        atributos = {}
        for attr in ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]:
            ttk.Label(janela, text=attr).pack()
            entry = ttk.Entry(janela)
            entry.pack()
            atributos[attr] = entry

        def confirmar():
            try:
                nome = campos["Nome"].get()
                classe = campos["Classe"].get()
                nivel = int(campos["Nível"].get())

                atr = {k: int(v.get()) for k, v in atributos.items()}

                atributos_obj = Atributos(**atr)
                self.personagem = Personagem(
                    nome=nome,
                    nivel=nivel,
                    atributos=atributos_obj,
                    classe_nome=classe
                )
                messagebox.showinfo("Sucesso", f"Personagem {nome} criado com sucesso!")
                janela.destroy()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro na criação: {e}")

        ttk.Button(janela, text="Criar", command=confirmar).pack(pady=20)

    def exibir_personagem(self):
        if not self.personagem:
            messagebox.showwarning("Aviso", "Nenhum personagem carregado.")
            return

        janela = tk.Toplevel(self.root)
        janela.title(f"Ficha de {self.personagem.nome}")
        janela.geometry("400x500")

        texto = tk.Text(janela, wrap="word")
        texto.pack(expand=True, fill="both", padx=10, pady=10)

        texto.insert("end", f"=== FICHA DE {self.personagem.nome} ===\n")
        texto.insert("end", f"Classe: {self.personagem.classe.nome}\n")
        texto.insert("end", f"Nível: {self.personagem.nivel}\n\n")

        texto.insert("end", "--- Atributos ---\n")
        for nome, valor in self.personagem.atributos.atributos.items():
            mod = self.personagem.atributos.modificador(nome)
            texto.insert("end", f"{nome}: {valor} (mod {mod:+})\n")

        texto.insert("end", "\n--- Perícias ---\n")
        for linha in self.personagem.habilidades.listar_pericias():
            texto.insert("end", f"{linha}\n")

        texto.insert("end", "\n--- Salvaguardas ---\n")
        for linha in self.personagem.habilidades.listar_salvaguardas():
            texto.insert("end", f"{linha}\n")

        texto.insert("end", "\n--- Magias ---\n")
        magias = self.personagem.listar_magias()
        if magias:
            for m in magias:
                texto.insert("end", f"- {m}\n")
        else:
            texto.insert("end", "Nenhuma magia disponível.\n")

        texto.config(state="disabled")

    def salvar_personagem(self):
        if not self.personagem:
            messagebox.showwarning("Aviso", "Nenhum personagem para salvar.")
            return

        nome_arquivo = f"{self.personagem.nome}.json"
        caminho = Path("output/fichas_salvas") / nome_arquivo
        salvar_personagem(self.personagem, str(caminho))
        messagebox.showinfo("Salvo", f"Personagem salvo em {caminho}")

    def carregar_personagem(self):
        janela = tk.Toplevel(self.root)
        janela.title("Carregar Personagem")
        janela.geometry("400x150")

        ttk.Label(janela, text="Nome do arquivo (ex: personagem.json)").pack(pady=10)
        entrada = ttk.Entry(janela)
        entrada.pack()

        def carregar():
            nome_arquivo = entrada.get().strip()
            caminho = Path("output/fichas_salvas") / nome_arquivo
            try:
                self.personagem = carregar_personagem(str(caminho))
                messagebox.showinfo("Sucesso", f"Personagem {self.personagem.nome} carregado.")
                janela.destroy()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao carregar: {e}")

        ttk.Button(janela, text="Carregar", command=carregar).pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = RPGApp(root)
    root.mainloop()
