import tkinter as tk
from tkinter import ttk
from firebase import firebase
f = firebase.FirebaseApplication('https://ep3-hotware.firebaseio.com', None)

from tkinter import Tk, StringVar, ttk
class hotel:
	
	def __init__(self):
		
		# Janela principal.
		self.window = tk.Tk()
		self.window.title("Hotware")
		self.window.geometry("500x500")
		self.window.rowconfigure(0, minsize=150, weight=1)
		self.window.rowconfigure(1, weight=1)
		self.window.columnconfigure(0, minsize=120, weight=1)
		self.window.columnconfigure(1, weight=1)

		self.texto= tk.StringVar()
		self.combo=ttk.Combobox(self.window)
		self.combo.place(x=10,y=100,width=160)
		self.combo['values']=('Qual o numero do seu quarto?','1','2','3','4')
		self.combo.current(0)
		botao=tk.Button(self.window,command=self.ok, text='ok').place(x=80,y=150)


		self.bo=tk.Button(self.window)
		self.bo.grid()
		self.bo.configure(text='hospede')
		self.bo.configure(command=self.whospede)
		self.A=[]
		self.B=[]
		self.entradas={'salame-R$2,00':2, 'batata-R$5,00':5}
		self.pratop={'Penne a Bolognesa-R$35,00':35,'Filet ao molho de mostarda-R$40,00':40}
		self.sobremesa={'Torta de Morango-R$15,00':15,'Petit Gateau-R$20,00':20}
		self.bebida={'Refrigerante-R$5,00':5,'Agua-R$3,00':3,'Suco Natural-R$8,00':8}

	def ok(self):
		if self.combo.get()=='1':
			self.q= 'Quarto1'
		if self.combo.get()=='2':
			self.q= 'Quarto2'
		if self.combo.get()=='3':
			self.q= 'Quarto3'
		if self.combo.get()=='4':
			self.q= 'Quarto4'
	
		
	def iniciar(self):
		self.window.mainloop()

	
	def apertou(self, event):
		self.postar(p)

	def whospede(self):
		self.tela_user= tk.Toplevel()
		self.tela_user.geometry("800x800")
		self.tela_user.title("Tela hospede")

		self.menubar = tk.Menu(self.tela_user)
		self.menubar.add_command(label="Inform", command=self.inform)
		self.menubar.add_command(label="Reportar Problemas", command=self.reportarproblemas)
		self.menubar.add_command(label="Servico de Quarto", command=self.servicodequarto)
		self.tela_user.config(menu=self.menubar) # Como permutar entre menus?



	def servicodequarto(self):
			
		self.texto= tk.StringVar()
		self.texto2=tk.StringVar()
		self.texto.set('Pedido: ')
		self.texto2.set('Total: ')
		self.combo=ttk.Combobox(self.tela_user)
		self.combo2=ttk.Combobox(self.tela_user)
		self.combo3=ttk.Combobox(self.tela_user)
		self.combo4=ttk.Combobox(self.tela_user)
		self.combo.place(x=10,y=100,width=160)
		self.combo2.place(x=200,y=100,width=200)
		self.combo3.place(x=430,y=100,width=160)
		self.combo4.place(x=630,y=100,width=160)
		self.combo['values']=('Escolha uma entrada','salame-R$2,00','batata-R$5,00')
		self.combo2['values']=('Escolha um prato principal','Penne a Bolognesa-R$35,00','Filet ao molho de mostarda-R$40,00')
		self.combo3['values']=('Escolha uma sobremesa','Torta de Morango-R$15,00','Petit Gateau-R$20,00')
		self.combo4['values']=('Escolha uma bebida','Refrigerante-R$5,00','Agua-R$3,00','Suco Natural-R$8,00')
		self.combo.current(0)
		self.combo2.current(0)
		self.combo3.current(0)
		self.combo4.current(0)
		botao=tk.Button(self.tela_user,command=self.pegar, text='Adicionar ao pedido').place(x=80,y=150)
		botao2=tk.Button(self.tela_user,command=self.finalizar, text='Finalizar pedido').place(x=80,y=180)
		etiqueta= tk.Label(self.tela_user,textvariable=self.texto).place(x=40,y=210)
		etiqueta2= tk.Label(self.tela_user,textvariable=self.texto2).place(x=40,y=240)


	def pegar(self):
		if self.combo2.get()!='Escolha um prato principal':
			self.A.append(self.combo2.get())
			self.B.append(self.pratop[self.combo2.get()])
		if self.combo.get()!='Escolha uma entrada':
			self.A.append(self.combo.get())
			self.B.append(self.entradas[self.combo.get()])
		if self.combo3.get()!='Escolha uma sobremesa':
			self.A.append(self.combo3.get())
			self.B.append(self.sobremesa[self.combo3.get()])
		if self.combo4.get()!='Escolha uma bebida':
			self.A.append(self.combo4.get())
			self.B.append(self.bebida[self.combo4.get()])
		self.texto.set('Pedidos: '+ str(self.A))
		

	def finalizar(self):	
		self.texto2.set('Total: R$'+ str(sum(self.B)) +',00')
		f.get('/servico',None)
		f.get('/total',None)
		teste = self.q
		f.put('/servico',teste,self.A)
		f.put('/total',teste,sum(self.B))

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
		botão.configure(command=self.postarprob)
		botão.grid(row=1, column=1)

	def apertou_enter(self, event):
		self.postar()

	
	def postarprob(self):
		self.conteudo_label.set(self.conteudo_caixa_texto.get())

		f.get('/users',None)
		teste = self.q
		f.put('/users',teste,str(self.conteudo_label.get()))


	def inform(self):

		Lb1 = tk.Listbox(self.tela_user)
		Lb1.insert(1, "Almoco: 12:00h as 15:00h")
		Lb1.insert(2, "Jantar: 18:00h as 22:00h")
		Lb1.insert(3, "Piscina: 11:00h as 18:00h")
		Lb1.pack()

app = hotel()
app.iniciar()
