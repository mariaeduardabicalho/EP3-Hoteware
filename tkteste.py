import tkinter as tk
import json

with open('listahospede.json') as arquivo:
 	pedidos = json.load(arquivo)


class hotel:
	
	def __init__(self,p):
		self.p=p


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
		self.menubar.add_command(label="Servico de quarto", command=self.servicodequarto)
		self.tela_user.config(menu=self.menubar)

		"""
		self.bhi=tk.Button(self.tela_user)
		self.bhi.grid()
		self.bhi.configure(text='informações')
		self.bhi.configure(command=self.)
		"""
	def servicodequarto(self):
		self.conteudo_label = tk.StringVar()
		label = tk.Label(self.tela_user)
		label.configure(textvariable=self.conteudo_label)
		label.configure(font="Courier 20 bold")
		label.grid(row=0, column=0, columnspan=2, sticky="nsew")        
		
		# Caixa de texto e StringVar para se comunicar com ela.

		self.conteudo_caixa_texto = tk.StringVar()
		
		caixa_texto = tk.Entry(self.tela_user)
		caixa_texto.configure(textvariable=self.conteudo_caixa_texto)
		caixa_texto.grid(row=1, column=0, padx=20, sticky="ew")
		
		# Binding: se apertar Enter dentro da caixa de texto, chama o callback
		# self.apertou_enter. 
		caixa_texto.bind("<Return>", self.apertou_enter)

		        
		botão = tk.Button(self.tela_user)
		botão.configure(text="Postar")
		botão.configure(command=self.postar)
		botão.grid(row=1, column=1)
		
#	def iniciar(self):
#		self.tela_user.mainloop()
	
	def apertou_enter(self, event):
		self.postar()

	
	def postar(self):
		self.conteudo_label.set(self.conteudo_caixa_texto.get())
		self.pedidos[0]=conteudo_caixa_texto

	def inform(self):

		Lb1 = tk.Listbox(self.tela_user)
		Lb1.insert(1, "Almoco: 12:00-15:00")
		Lb1.insert(2, "Perl")
		Lb1.insert(3, "C")
		Lb1.insert(4, "PHP")
		Lb1.insert(5, "JSP")
		Lb1.insert(6, "Ruby")

		Lb1.pack()

	"""	listbox = tk.Listbox(self.tela_user)
		listbox.pack()
		A=[]

		for i in range(1,len(self.lista)+1):
			A.append(i)
			listbox.insert(A[i], self.lista[i])
	"""	
	   
	
	def wfunci(self):
		self.tela_user= tk.Toplevel()
		self.tela_user.geometry("800x400+0+0")
		self.tela_user.title("Tela funcionario")
		self.botao=tk.Button(self.tela_user)
		self.botao.configure(text='Quarto 1',background='green')
		self.botao.configure(command=self.quarto)
		self.botao.grid()


	def quarto(self):
		print(self.pedidos)

app = hotel(pedidos)
app.iniciar()


with open('listahospede.json', 'w') as arquivo:
	json.dump(pedidos,arquivo)