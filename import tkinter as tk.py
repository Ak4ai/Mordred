import tkinter as tk
from tkinter import messagebox
import random

class Personagem:
    def __init__(self):
        self.vida = 50
        self.energia = 30
        self.vigor = 2
        self.intelecto = -2
        self.presenca = 3
        self.forca = 4
        self.agilidade = 1
        self.pericia_calamidade = 4
        self.pericia_luta = 16
        self.pericia_manifestacao = 6

    def reduzir_energia(self, valor):
        self.energia -= valor

    def adicionar_energia(self, valor):
        self.energia += valor

    def reduzir_vida(self, valor):
        self.vida -= valor

    def adicionar_vida(self, valor):
        self.vida += valor

    def obter_status(self):
        return f"Vida: {self.vida} | Energia: {self.energia} | Vigor: {self.vigor} | Intelecto: {self.intelecto} | Presença: {self.presenca} | Força: {self.forca} | Agilidade: {self.agilidade}"

class HabilidadeBase:
    def __init__(self, nome, personagem):
        self.nome = nome
        self.dano_total = 0
        self.personagem = personagem

    def rolar_dado(self, lados, quantidade=1):
        resultados = [random.randint(1, lados) for _ in range(quantidade)]
        return resultados, sum(resultados), lados * quantidade

    def mostrar_mensagem(self, mensagem):
        messagebox.showinfo(f"Resultado do Dado - {self.nome}", mensagem)

    def obter_dano_total(self):
        return f"Dano Total Acumulado ({self.nome}): {self.dano_total}" if self.nome == "Lucifer" else f"({self.nome}) Teste de Presença - Manifestação"

class LuciferPassiva(HabilidadeBase):
    def __init__(self, personagem):
        super().__init__("Lucifer", personagem)

    def aplicar_ataque(self):
        dados, resultado, maximo = self.rolar_dado(6, 1)
        self.dano_total += resultado
        self.mostrar_mensagem(f"Ataque recebido/causado: {dados} => +{resultado} de dano (Máximo: {maximo})")

    def aplicar_nocaute(self):
        dados, resultado, maximo = self.rolar_dado(8, 1)
        self.dano_total += resultado
        self.mostrar_mensagem(f"Inimigo Morto/Aliado Caido: {dados} => +{resultado} de dano (Máximo: {maximo})")

    def aplicar_buff_debuff(self):
        dados, resultado, maximo = self.rolar_dado(6, 2)
        self.dano_total += resultado
        self.mostrar_mensagem(f"Buff/Debuff em si: {dados} => +{resultado} de dano (Máximo: {maximo})")

    def aplicar_habilidade(self):
        dados, resultado, maximo = self.rolar_dado(8, 2)
        self.dano_total += resultado
        self.mostrar_mensagem(f"Habilidade inimiga/aliada: {dados} => +{resultado} de dano (Máximo: {maximo})")

    def aplicar_criticos(self):
        dados, resultado, maximo = self.rolar_dado(10, 1)
        self.dano_total += resultado
        self.mostrar_mensagem(f"Críticos (Aliados ou inimigo): {dados} => +{resultado} de dano (Máximo: {maximo})")

    def aplicar_aliado_morto(self):
        self.dano_total += 30
        self.mostrar_mensagem("Aliado Morto (morte permanente): +30 de dano")

class Belzebub(HabilidadeBase):
    def __init__(self, personagem):
        super().__init__("Belzebub", personagem)

    def aplicar_habilidade(self):
        if self.personagem.energia >= 25:
            self.personagem.reduzir_energia(25)

            dados_presenca = [random.randint(1, 20) for _ in range(self.personagem.presenca)]
            maior_dado = max(dados_presenca)

            self.mostrar_mensagem(f"Teste de Presença - Manifestação: {dados_presenca} => maior dado: {maior_dado}")

            mensagem = f"Teste de Presença - Manifestação (com Perícia): {maior_dado}\n"

            if maior_dado <= 10:
                mensagem += "1-10: Toma somente ½ do dano físico de todas as fontes"
            elif maior_dado <= 18:
                mensagem += "11-18: Toma somente ¼ do dano físico de todas as fontes"
            else:
                mensagem += "19+: Não toma dano físico de nenhuma fonte"

            self.mostrar_mensagem(mensagem)
        else:
            self.mostrar_mensagem("Energia insuficiente para usar Belzebub")

class AjusteEnergiaVida:
  def __init__(self, root, personagem):
      self.root = root
      self.personagem = personagem

      self.label_ajuste_energia = tk.Label(root, text="Ajuste Energia:")
      self.label_ajuste_energia.pack()

      self.entry_ajuste_energia = tk.Entry(root)
      self.entry_ajuste_energia.pack()

      self.botao_adicionar_energia = tk.Button(root, text="Adicionar Energia", command=self.adicionar_energia)
      self.botao_adicionar_energia.pack()

      self.botao_reduzir_energia = tk.Button(root, text="Reduzir Energia", command=self.reduzir_energia)
      self.botao_reduzir_energia.pack()

      self.label_ajuste_vida = tk.Label(root, text="Ajuste Vida:")
      self.label_ajuste_vida.pack()

      self.entry_ajuste_vida = tk.Entry(root)
      self.entry_ajuste_vida.pack()

      self.botao_adicionar_vida = tk.Button(root, text="Adicionar Vida", command=self.adicionar_vida)
      self.botao_adicionar_vida.pack()

      self.botao_reduzir_vida = tk.Button(root, text="Reduzir Vida", command=self.reduzir_vida)
      self.botao_reduzir_vida.pack()

  def adicionar_energia(self):
      self.ajustar_energia(1)

  def reduzir_energia(self):
      self.ajustar_energia(-1)

  def ajustar_energia(self, multiplicador):
      try:
          valor_ajuste = int(self.entry_ajuste_energia.get()) * multiplicador
          self.personagem.adicionar_energia(valor_ajuste)
          self.atualizar_status()
      except ValueError:
          messagebox.showwarning("Erro", "Digite um valor válido para o ajuste de energia")

  def adicionar_vida(self):
      self.ajustar_vida(1)

  def reduzir_vida(self):
      self.ajustar_vida(-1)

  def ajustar_vida(self, multiplicador):
      try:
          valor_ajuste = int(self.entry_ajuste_vida.get()) * multiplicador
          self.personagem.adicionar_vida(valor_ajuste)
          self.atualizar_status()
      except ValueError:
          messagebox.showwarning("Erro", "Digite um valor válido para o ajuste de vida")

  def atualizar_status(self):
      messagebox.showinfo("Status Atualizado", self.personagem.obter_status())

class InterfaceSelecaoHabilidade:
    def __init__(self, root, personagem, callback):
        self.root = root
        self.personagem = personagem
        self.callback = callback

        self.label_selecao = tk.Label(root, text="Escolha uma habilidade:")
        self.label_selecao.pack(pady=10)

        self.habilidades = {
            "LuciferPassiva": LuciferPassiva,
            "Belzebub": Belzebub,
        }

        for nome_habilidade, classe_habilidade in self.habilidades.items():
            botao_habilidade = tk.Button(root, text=nome_habilidade, command=lambda c=classe_habilidade: self.escolher_habilidade(c))
            botao_habilidade.pack(pady=5)

        # Adiciona um botão para acessar a interface de ajustes
        botao_ajustes = tk.Button(root, text="Ajustes", command=self.abrir_interface_ajustes)
        botao_ajustes.pack(pady=10)

        self.aba_ajuste = None  # Inicializa a aba de ajuste como None

    def escolher_habilidade(self, classe_habilidade):
        habilidade_escolhida = classe_habilidade(self.personagem)
        self.callback(habilidade_escolhida)
        self.root.destroy()

    def abrir_interface_ajustes(self):
        # Abre a interface de ajustes
        self.aba_ajuste = AjusteEnergiaVida(self.root, self.personagem)

class InterfaceGrafica:
    def __init__(self, root, habilidade, personagem):
        self.root = root
        self.root.title(f"Habilidade: {habilidade.nome}")
        self.habilidade = habilidade
        self.personagem = personagem

        self.label_dano_total = tk.Label(root, text="")
        self.label_dano_total.pack(pady=10)

        self.label_status = tk.Label(root, text="")
        self.label_status.pack(pady=10)

        for nome_metodo in dir(self.habilidade):
            if nome_metodo.startswith("aplicar_"):
                botao_habilidade = tk.Button(root, text=nome_metodo.replace("aplicar_", ""), command=lambda m=nome_metodo: self.executar_metodo(m))
                botao_habilidade.pack(pady=5)

        botao_sair = tk.Button(root, text="Sair", command=root.destroy)
        botao_sair.pack(pady=10)

        self.atualizar_label_dano_total()
        self.atualizar_label_status()

    def executar_metodo(self, nome_metodo):
        getattr(self.habilidade, nome_metodo)()
        self.atualizar_label_dano_total()
        self.atualizar_label_status()

    def atualizar_label_dano_total(self):
        self.label_dano_total.config(text=self.habilidade.obter_dano_total())

    def atualizar_label_status(self):
        self.label_status.config(text=self.personagem.obter_status())

def abrir_interface_principal(habilidade_escolhida):
    root = tk.Tk()
    interface_principal = InterfaceGrafica(root, habilidade_escolhida, personagem)
    root.mainloop()

if __name__ == "__main__":
    personagem = Personagem()
    root = tk.Tk()
    interface_selecao = InterfaceSelecaoHabilidade(root, personagem, abrir_interface_principal)
    root.mainloop()
