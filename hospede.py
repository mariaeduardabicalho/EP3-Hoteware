import tkinter as tk
from firebase import firebase
f = firebase.FirebaseApplication('https://ep3-hotware.firebaseio.com', None)


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

		
		
	def iniciar(self):
		self.window.mainloop()

	
	def apertou(self, event):
		self.postar(p)

	def whospede(self):
		self.tela_user= tk.Toplevel()
		self.tela_user.geometry("800x400+0+0")
		self.tela_user.title("Tela hospede")

		self.menubar = tk.Menu(self.tela_user)
		self.menubar.add_command(label="Inform", command=self.inform)
		self.menubar.add_command(label="Reportar Problemas", command=self.reportarproblemas)
		self.menubar.add_command(label="Servico de Quarto", command=self.servicodequarto)
		self.tela_user.config(menu=self.menubar) # Como permutar entre menus?


	def servicodequarto(self):
		self.conteudo_label = tk.StringVar()
		label = tk.Label(self.tela_user)
		label.configure(textvariable=self.conteudo_label)
		label.configure(font="Courier 20 bold")
		label.grid(row=0, column=0, columnspan=2, sticky="nsew")   

		self.conteudo_caixa_texto = tk.StringVar()
		
		caixa_texto = tk.Entry(self.tela_user)
		caixa_texto.configure(textvariable=self.conteudo_caixa_texto)
		caixa_texto.grid(row=1, column=0, padx=20, sticky="ew")

		caixa_texto.bind("<Return>", self.apertou_enter)

		        
		botão = tk.Button(self.tela_user)
		botão.configure(text="Postar")
		botão.configure(command=self.postar)
		botão.grid(row=2, column=1)


	def reportarproblemas(self):
		self.conteudo_label = tk.StringVar()
		label = tk.Label(self.tela_user)
		label.configure(textvariable=self.conteudo_label)
		label.configure(font="Courier 20 bold")
		label.grid(row=0, column=0, columnspan=2, sticky="nsew")   

		self.conteudo_caixa_texto = tk.StringVar()
		
		caixa_texto = tk.Entry(self.tela_user)
		caixa_texto.configure(textvariable=self.conteudo_caixa_texto)
		caixa_texto.grid(row=1, column=0, padx=20, sticky="ew")

		caixa_texto.bind("<Return>", self.apertou_enter)

		        
		botão = tk.Button(self.tela_user)
		botão.configure(text="Postar")
		botão.configure(command=self.postar)
		botão.grid(row=1, column=1)

	def apertou_enter(self, event):
		self.postar()

	
	def postar(self):
		self.conteudo_label.set(self.conteudo_caixa_texto.get())

		f.get('/users',None)
		teste = 'Quarto1'
		f.put('/users',teste,str(self.conteudo_label.get()))


	def inform(self):

		Lb1 = tk.Listbox(self.tela_user)
		Lb1.insert(1, "Almoco: 12:00h as 15:00h")
		Lb1.insert(2, "Jantar: 18:00h as 22:00h")
		Lb1.insert(3, "Piscina: 11:00h as 18:00h")
		#Lb1.insert(4, "PHP")
		#Lb1.insert(5, "JSP")
		#Lb1.insert(6, "Ruby")

		Lb1.pack()

app = hotel()
app.iniciar()


