import tkinter as tk


class MeuAplicativo:
    
    def __init__(self):
        # Criando a janela e os widgets.
        # Não precisa "guardar" todos os componentes no self, só aqueles aos
        # quais você queira se referenciar depois (e.g. em outros métodos).

        # Janela principal.
        self.window = tk.Tk()
        self.window.title("Hotware")
        self.window.geometry("300x200+100+100")
        self.window.rowconfigure(0, minsize=150, weight=1)
        self.window.rowconfigure(1, weight=1)
        self.window.columnconfigure(0, minsize=120, weight=1)
        self.window.columnconfigure(1, weight=1)
        self.botao=tk.Button(self.window)
        self.botao.grid()
        self.botao.configure(text='Servico de quarto')
        self.bo=tk.Button(self.window)
        self.bo.grid()
        self.bo.configure(text='infos')
        self.window.mainloop()

    def iniciar(self):
        self.window.mainloop()
    
    def apertou_enter(self, bo, botao):
        self.bo()
    
    def postar(self):
        self.conteudo_label.set(self.conteudo_caixa_texto.get())

app = MeuAplicativo()
app.iniciar()





"""
        # Label para mostrar mensagem e StringVar para se comunicar com ela.
        # O StringVar é como o "walkie-talkie" do componente, posso usá-lo
        # para mandar conteúdo e para receber conteúdo do componente. Coisa de
        # Tkinter isso: cada framework faz de um jeito diferente.
        # Note que eu guardo apenas o StringVar no self, pois é tudo o que eu
        # preciso.
        self.conteudo_label = tk.StringVar()
        label = tk.Label(self.window)
        label.configure(textvariable=self.conteudo_label)
        label.configure(font="Courier 20 bold")
        label.grid(row=0, column=0, columnspan=2, sticky="nsew")        
        
        # Caixa de texto e StringVar para se comunicar com ela.
        self.conteudo_caixa_texto = tk.StringVar()
        
        caixa_texto = tk.Entry(self.window)
        caixa_texto.configure(textvariable=self.conteudo_caixa_texto)
        caixa_texto.grid(row=1, column=0, padx=20, sticky="ew")
        
        # Binding: se apertar Enter dentro da caixa de texto, chama o callback
        # self.apertou_enter. 
        caixa_texto.bind("<Return>", self.apertou_enter)

        # Botão de postar mensagem.        
        botão = tk.Button(self.window)
        botão.configure(text="Postar")
        botão.configure(command=self.postar)
        botão.grid(row=1, column=1)
"""
        