import tkinter as tk
from tkinter import ttk
from firebase import firebase
from PIL import Image, ImageTk
from tkinter import font
import time
from tkinter import Tk, StringVar, ttk
f = firebase.FirebaseApplication('https://ep3-hotware.firebaseio.com', None)

class hotel:
	
	def __init__(self):
		
		# Janela de selecao dos quartos
		self.window = tk.Tk()
		self.window.title("Hotware")
		self.window.geometry("500x500")
		self.window.rowconfigure(0, minsize=150, weight=1)
		self.window.rowconfigure(1, weight=1)
		self.window.columnconfigure(0, minsize=120, weight=1)
		self.window.columnconfigure(1, weight=1)

		# Instrucao para selecionar os quartos
		self.textoq= tk.StringVar()
		self.textoq.set('Selecione seu quarto')
		escrever= tk.Label(self.window,textvariable=self.textoq,font=('Comic Sans MS',15)).place(x=80,y=20)

		# Combobox para selecionar os quartos
		self.combo=ttk.Combobox(self.window)
		self.combo.place(x=10,y=100,width=200)
		self.combo['values']=('---','1','2','3','4')
		self.combo.current(0)
		botao=tk.Button(self.window,command=self.ok, text='  ok  ', bg='pink').place(x=300,y=100)

		# Lista para armazenar os valores das comidas e as comidas 
		self.A=[]
		self.B=[]
		self.S=[]
		self.V=[]
		self.H=[]

		#Dicionario que armazena o valor de cada alimento
		self.entradas={'salame-R$2,00':2, 'batata-R$5,00':5}
		self.pratop={'Penne a Bolognesa-R$35,00':35,'Filet ao molho de mostarda-R$40,00':40}
		self.sobremesa={'Torta de Morango-R$15,00':15,'Petit Gateau-R$20,00':20}
		self.bebida={'Refrigerante-R$5,00':5,'Agua-R$3,00':3,'Suco Natural-R$8,00':8}
		self.spa1={'Unha da mão-R$15,00':15,'Unha do pé-R$20,00':20,'Massagem-R$45,00 ':45}

	def ok(self):
		if self.combo.get()=='1':
			self.q= 'Quarto1'
		if self.combo.get()=='2':
			self.q= 'Quarto2'
		if self.combo.get()=='3':
			self.q= 'Quarto3'
		if self.combo.get()=='4':
			self.q= 'Quarto4'


		self.tela_user= tk.Toplevel()
		self.tela_user.geometry("800x800")
		self.tela_user.title("Tela hospede")

		self.menubar = tk.Menu(self.tela_user)
		self.menubar.add_command(label="Informacoes", command=self.inform)
		self.menubar.add_command(label="Reportar Problemas", command=self.reportarproblemas)
		self.menubar.add_command(label="Servico de Quarto", command=self.servicodequarto)
		self.menubar.add_command(label="Spa", command=self.spa)
		self.tela_user.config(menu=self.menubar) # Como permutar entre menus?

	
	def iniciar(self):
		self.window.mainloop()

	
	def apertou(self, event):
		self.postar(p)


	def spa(self):
		self.textoo= tk.StringVar()
		self.textoo.set('Escolha um serviço do SPA')
		escrever= tk.Label(self.tela_user,textvariable=self.textoo,font=('Comic Sans MS',15)).place(x=40,y=20)

		self.texto6= tk.StringVar()
		self.texto6.set('Serviços:')
		self.texto8= tk.StringVar()
		self.texto8.set('Total:')
		self.combo6=ttk.Combobox(self.tela_user)
		self.combo6.place(x=10,y=100,width=160)
		self.combo6['values']=('Escolha um serviço','Unha da mão-R$15,00','Unha do pé-R$20,00','Massagem-R$45,00 ')
		self.combo6.current(0)
		self.combo8=ttk.Combobox(self.tela_user)
		self.combo8.place(x=300,y=100,width=200)
		self.combo8['values']=('Escolha um horario de chegada','9:00','10:00','11:00','12:00','14:00','15:00')
		self.combo8.current(0)
		botao6=tk.Button(self.tela_user,command=self.pegars, text='Adicionar').place(x=80,y=150)
		botao8=tk.Button(self.tela_user,command=self.finalizars, text='Finalizar').place(x=80,y=180)
		etiqueta6= tk.Label(self.tela_user,textvariable=self.texto6).place(x=40,y=210)
		etiqueta8= tk.Label(self.tela_user,textvariable=self.texto8).place(x=40,y=240)
		#self.ph=tk.PhotoImage(file="massagemmulher.png")
		# fazer:  image= tk.Image.open()


	def pegars(self):
		if self.combo6.get()!='Escolha um serviço':
			self.S.append(self.combo6.get())
			self.V.append(self.spa1[self.combo6.get()])
		if self.combo8.get()!='Escolha um horario':
			self.H.append(self.combo8.get())
		self.texto6.set('Serviços: ' + str(self.S))
		

	def finalizars(self):
		self.texto8.set('Total: R$'+ str(sum(self.V)) +',00')
		f.get('/spa',None)
		f.get('/totalspa',None)
		f.get('/horariospa',None)
		teste = self.q
		f.put('/spa',teste,self.S)
		f.put('/totalspa',teste,sum(self.V))
		f.put('/horariospa',teste,self.H)
		self.texto3= tk.StringVar()
		self.texto3.set('Seu horário foi reservado!')
		feedback= tk.Label(self.tela_user,textvariable=self.texto3).place(x=100,y=300)



	def servicodequarto(self):
		self.textoo= tk.StringVar()
		self.textoo.set('Escolha seu pedido. Se quiser adicionar mais de um do mesmo topico, tenha certeza de que os outros não estao selecionados.')
		escrever= tk.Label(self.tela_user,textvariable=self.textoo,font=(None,10)).place(x=40,y=20)
			
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
		self.texto.set('Pedidos: ' + str(self.A))
		

	def finalizar(self):	
		self.texto2.set('Total: R$'+ str(sum(self.B)) +',00')
		f.get('/servico',None)
		f.get('/total',None)
		teste = self.q
		f.put('/servico',teste,self.A)
		f.put('/total',teste,sum(self.B))
		self.texto3= tk.StringVar()
		self.texto3.set('Seu pedido foi feito. Estamos a caminho.')
		feedback= tk.Label(self.tela_user,textvariable=self.texto3).place(x=100,y=300)

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

		        
		botão = tk.Button(self.tela_user)
		botão.configure(text="Postar")
		botão.configure(command=self.postarprob)
		botão.grid(row=1, column=1)


	
	def postarprob(self):
		self.conteudo_label.set(self.conteudo_caixa_texto.get())

		f.get('/users',None)
		teste = self.q
		f.put('/users',teste,str(self.conteudo_label.get()))

		self.texto4= tk.StringVar()
		self.texto4.set('Estamos a caminho.')
		feedback4= tk.Label(self.tela_user,textvariable=self.texto4).place(x=100,y=250)


	def inform(self):

		Lb1 = tk.Listbox(self.tela_user,width=30,height=4)
		Lb1.place(x=0, y=0)
		now = time.strftime("%H:%M:%S")

		Lb1.insert(0, "Café da manhã:  07:00h as 10:30h")
		Lb1.insert(1, "Almoco:  12:00h as 15:00h")
		Lb1.insert(2, "Jantar:  18:00h as 22:00h")
		Lb1.insert(3, "Piscina: 08:00h as 22:00h")

		Lb2 = tk.Listbox(self.tela_user,width=30,height=2)
		Lb2.place(x=100, y=0)
		Lb2.insert(0, "Fechado")
		Lb2.itemconfig(0, bg='red',)
		Lb2.insert(1, "Aberto")
		Lb2.itemconfig(1, bg='green')



		#mudança de cor da listbox de acordo com horario de funcionamento
		if now >= time.strftime("07:00:00") and (now<time.strftime("10:30:00")) :
			Lb1.itemconfig(0, bg='green')
		else:
			Lb1.itemconfig(0, bg='red')

		if now >= time.strftime("12:00:00") and (now<time.strftime("15:00:00")) :
			Lb1.itemconfig(1, bg='green')
		else:
			Lb1.itemconfig(1, bg='red')

		if now >= time.strftime("18:00:00") and (now<time.strftime("22:00:00")) :
			Lb1.itemconfig(2, bg='green')
		else:
			Lb1.itemconfig(2, bg='red')
		if now >= time.strftime("07:00:00") and (now<time.strftime("22:00:00")) :
			Lb1.itemconfig(3, bg='green')
		else:
			Lb1.itemconfig(3, bg='red')
		
		Lb1.pack()

app = hotel()
app.iniciar()



#trocar lugar spa cmbobox
#arrumar pedidos
#clicar no ok + de 3 vzs pos pedido
#ajustar feeedback