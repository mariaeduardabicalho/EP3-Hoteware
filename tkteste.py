import tkinter as tk


class hotel:
	
	def __init__(self):

		# Janela principal.
		self.window = tk.Tk()
		self.window.title("Hotware")
		self.window.geometry("300x200+100+100")
		self.window.rowconfigure(0, minsize=150, weight=1)
		self.window.rowconfigure(1, weight=1)
		self.window.columnconfigure(0, minsize=120, weight=1)
		self.window.columnconfigure(1, weight=1)
		
		
		#self.conteudo_inf= tk.StringVar()
		
		self.bo=tk.Button(self.window)
		self.bo.grid()
		self.bo.configure(text='hospede')
		self.bo.configure(command=self.whospede)

		
		#caixa_texto.configure(textvariable=self.conteudo_inf)
		#caixa_texto.grid(row=1, column=0, padx=20, sticky="ew")
		
		# Binding: se apertar Enter dentro da caixa de texto, chama o callback
		# self.apertou_enter. 
		#caixa_texto.bind("<Return>", self.apertou)

		
		self.botao=tk.Button(self.window)
		self.botao.configure(text='Funcionario')
		self.botao.configure(command=self.wfunci)
		self.botao.grid()
		
		
	def iniciar(self):
		self.window.mainloop()

	
	def apertou(self, event):
		self.postar()

	def whospede(self):
		self.tela_user= tk.Toplevel()
		self.tela_user.geometry("800x400+0+0")
		self.tela_user.title("Tela hospede")

		self.menubar = tk.Menu(self.tela_user)
		self.menubar.add_command(label="Inform", command=self.inform)
		self.menubar.add_command(label="Quit", command=self.tela_user.quit)
		self.tela_user.config(menu=self.menubar)
		"""
		self.bhi=tk.Button(self.tela_user)
		self.bhi.grid()
		self.bhi.configure(text='informações')
		self.bhi.configure(command=self.)
		"""


	def inform(self):
		


	#def infos(self):
		#self.tela_infos=tk.Toplevel()
		#self.tela_infos.geometry("800x400+0+0")
		#self.tela_user.title('informações')

	   
	
	def wfunci(self):
		self.tela_user= tk.Toplevel()
		self.tela_user.geometry("800x400+0+0")
		self.tela_user.title("Tela funcionario")


	#def postar(self):
		#self.conteudo_label_inf.set(self.conteudo_inf.get())

app = hotel()
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
		