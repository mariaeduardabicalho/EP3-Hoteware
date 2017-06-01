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
		
		# Configuração da janela de selecao dos quartos
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
		self.A=[] #itens do servico de quarto
		self.B=[] #valores do serviço de quarto
		self.S=[] #itens do spa
		self.V=[] #valores dos itens do spa
		self.H=[] #horario do spa

		#Dicionario que armazena o valor de cada alimento
		self.entradas={'salame-R$2,00':2, 'batata-R$5,00':5}
		self.pratop={'Penne a Bolognesa-R$35,00':35,'Filet ao molho de mostarda-R$40,00':40}
		self.sobremesa={'Torta de Morango-R$15,00':15,'Petit Gateau-R$20,00':20}
		self.bebida={'Refrigerante-R$5,00':5,'Agua-R$3,00':3,'Suco Natural-R$8,00':8}
		self.spa1={'Unha da mão-R$15,00':15,'Unha do pé-R$20,00':20,'Massagem-R$45,00 ':45}


		#abir a tela com a variavel do quarto selecionado
	def ok(self):
		if self.combo.get()=='1':
			self.q= 'Quarto1'
		if self.combo.get()=='2':
			self.q= 'Quarto2'
		if self.combo.get()=='3':
			self.q= 'Quarto3'
		if self.combo.get()=='4':
			self.q= 'Quarto4'

		#Criação da janela
		self.tela_user= tk.Toplevel()
		self.tela_user.geometry("800x800")
		self.tela_user.title("Tela hospede")

		self.text= tk.StringVar()
		self.text.set('Bem vindo(a) ao Hotel Laerte. Selecione um item do Menu acima.')
		escrever= tk.Label(self.tela_user,textvariable=self.text,font=(None,12)).place(x=0,y=500)

		#Informações nos menus
		self.menubar = tk.Menu(self.tela_user)
		self.menubar.add_command(label="Informacoes", command=self.inform)
		self.menubar.add_command(label="Reportar Problemas",command=self.reportarproblemas)
		self.menubar.add_command(label="Servico de Quarto",command=self.servicodequarto)
		self.menubar.add_command(label="Spa",command=self.spa)

		self.tela_user.config(menu=self.menubar)

	
	def iniciar(self):
		self.window.mainloop()
	
	def apertou(self, event):
		self.postar(p)

	#Função do menubar spa
	def spa(self):

		#Texto explicativo para o usuario
		self.textoo= tk.StringVar()
		self.textoo.set('Escolha um serviço do SPA')
		escrever= tk.Label(self.tela_user,textvariable=self.textoo,font=('Comic Sans MS',15)).place(x=40,y=20)

		#Organização das comboboxes
		self.texto6= tk.StringVar()
		self.texto6.set('Serviços:') #Itens selecionados que foram apresentados para os usuarios
		self.texto8= tk.StringVar()
		self.texto8.set('Total:') #Total apresentado para o usuario
		self.combo6=ttk.Combobox(self.tela_user)
		self.combo6.place(x=300,y=100,width=160)
		self.combo6['values']=('Escolha um serviço','Unha da mão-R$15,00','Unha do pé-R$20,00','Massagem-R$45,00 ') #valores da combobox
		self.combo6.current(0)
		self.combo8=ttk.Combobox(self.tela_user)
		self.combo8.place(x=10,y=100,width=200)
		self.combo8['values']=('Escolha um horario de chegada','9:00','10:00','11:00','12:00','14:00','15:00')
		self.combo8.current(0)
		self.botao6=tk.Button(self.tela_user,command=self.pegars, text='Adicionar') #Botão para juntar os itens selecionados em uma lista
		self.botao6.place(x=80,y=150) 
		self.botao8=tk.Button(self.tela_user,command=self.finalizars, text='Finalizar')
		self.botao8.place(x=80,y=180) #Botão para o calculo do total
		etiqueta6= tk.Label(self.tela_user,textvariable=self.texto6).place(x=40,y=210)
		etiqueta8= tk.Label(self.tela_user,textvariable=self.texto8).place(x=40,y=240)


	#Pegando os itens do spa
	def pegars(self):
		if self.combo6.get()!='Escolha um serviço':
			self.S.append(self.combo6.get())
			self.SS='  '.join(self.S)
			self.V.append(self.spa1[self.combo6.get()])
		if self.combo8.get()!='Escolha um horario':
			self.H.append(self.combo8.get())
		self.texto6.set('Serviços: ' + self.SS)
		
	#Fazendo a conta dos itens do spa e os adiconando ao firebase
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
		self.texto3.set('Seu horário foi reservado!') #feedback para o usuario
		feedback= tk.Label(self.tela_user, font=('Helvetica',10, 'bold'), textvariable=self.texto3).place(x=100,y=300)
		self.remove_button = tk.Button(self.tela_user, text="<--", command=self.destruirspa)
		self.remove_button.place(x=10,y=10)

	def destruirspa(self):
		self.textoo.set('')
		self.texto6.set('')
		self.texto8.set('')
		self.combo6.destroy()
		self.combo8.destroy()
		self.botao6.destroy()
		self.botao8.destroy()
		self.texto3.set('')
		self.remove_button.destroy()
		self.text.set('')
		

	def servicodequarto(self):

		#informação para o usuário
		self.textoo= tk.StringVar() 
		self.textoo.set('Escolha seu pedido. Se quiser adicionar mais de um do mesmo topico, tenha certeza de que os outros não estao selecionados.')
		escrever= tk.Label(self.tela_user,textvariable=self.textoo,font=(None,10)).place(x=40,y=20)
			

		self.texto= tk.StringVar()
		self.texto2=tk.StringVar()
		self.texto.set('Pedido: ') #Itens selecionados que foram apresentados para os usuarios
		self.texto2.set('Total: ') #Total apresentado para o usuario
		self.combo=ttk.Combobox(self.tela_user) #criando combobox
		self.combo2=ttk.Combobox(self.tela_user)
		self.combo3=ttk.Combobox(self.tela_user)
		self.combo4=ttk.Combobox(self.tela_user)
		self.combo.place(x=10,y=100,width=160)
		self.combo2.place(x=200,y=100,width=200)
		self.combo3.place(x=430,y=100,width=160)
		self.combo4.place(x=630,y=100,width=160)
		self.combo['values']=('Escolha uma entrada','salame-R$2,00','batata-R$5,00') #valores da combobox
		self.combo2['values']=('Escolha um prato principal','Penne a Bolognesa-R$35,00','Filet ao molho de mostarda-R$40,00')
		self.combo3['values']=('Escolha uma sobremesa','Torta de Morango-R$15,00','Petit Gateau-R$20,00')
		self.combo4['values']=('Escolha uma bebida','Refrigerante-R$5,00','Agua-R$3,00','Suco Natural-R$8,00')
		self.combo.current(0)
		self.combo2.current(0)
		self.combo3.current(0)
		self.combo4.current(0)
		self.botao=tk.Button(self.tela_user,command=self.pegar, text='Adicionar ao pedido')
		self.botao.place(x=80,y=150)
		self.botao2=tk.Button(self.tela_user,command=self.finalizar, text='Finalizar pedido')
		self.botao2.place(x=80,y=180)
		etiqueta= tk.Label(self.tela_user,textvariable=self.texto).place(x=40,y=210)
		etiqueta2= tk.Label(self.tela_user,textvariable=self.texto2).place(x=40,y=240)

		#Pegando os itens do serviço de quarto e os adicionando a lista de produto e valor
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
		self.AA='  '.join(self.A)
		self.texto.set('Pedidos: ' + self.AA)
		
	#Fazendo a conta dos itens do serviço de quarto e os adiconando ao firebase
	def finalizar(self):	
		self.texto2.set('Total: R$'+ str(sum(self.B)) +',00')
		f.get('/servico',None)
		f.get('/total',None)
		teste = self.q
		f.put('/servico',teste,self.A)
		f.put('/total',teste,sum(self.B))
		self.texto3= tk.StringVar()
		self.texto3.set('Seu pedido foi feito. Estamos a caminho.')
		feedback2= tk.Label(self.tela_user,font=('Helvetica',10, 'bold'), textvariable=self.texto3).place(x=100,y=300)
		self.remove_button2 = tk.Button(self.tela_user, text="<--", command=self.destruirserv)
		self.remove_button2.place(x=10,y=10)
		self.text1= tk.StringVar()
		self.text1.set('Para mudar de menu, clique na seta à esquerda.')
		escrever= tk.Label(self.tela_user,textvariable=self.text1,font=(None,12)).place(x=0,y=400)

	def destruirserv(self):
		self.texto.set('')
		self.textoo.set('')
		self.texto2.set('')
		self.combo.destroy()
		self.combo2.destroy()
		self.combo3.destroy()
		self.combo4.destroy()
		self.botao2.destroy()
		self.botao.destroy()
		self.texto3.set('')
		self.remove_button2.destroy()
		self.text1.set('')


	def reportarproblemas(self):

		#setando o conteudo
		self.conteudo_label = tk.StringVar()
		label = tk.Label(self.tela_user)
		label.configure(textvariable=self.conteudo_label)
		label.configure(font="Courier 20 bold")
		label.grid(row=0, column=0, columnspan=2, sticky="nsew")   

		self.conteudo_caixa_texto = tk.StringVar()
		
		#fazendo caixa de texto
		self.caixa_texto = tk.Entry(self.tela_user)
		self.caixa_texto.configure(textvariable=self.conteudo_caixa_texto)
		self.caixa_texto.grid(row=1, column=0, padx=20, sticky="ew")

		#fazendo botao para comprar  
		self.botão = tk.Button(self.tela_user)
		self.botão.configure(text="Postar")
		self.botão.configure(command=self.postarprob)
		self.botão.grid(row=1, column=1)


	
	def postarprob(self):
		self.conteudo_label.set(self.conteudo_caixa_texto.get())

		#adicionar ao firebase
		f.get('/users',None)
		teste = self.q
		f.put('/users',teste,str(self.conteudo_label.get()))

		#feedback para o usuario
		self.texto4= tk.StringVar()
		self.texto4.set('Estamos a caminho.')
		feedback3= tk.Label(self.tela_user, font=('Helvetica',10, 'bold'),textvariable=self.texto4).place(x=100,y=250)
		self.remove_button3 = tk.Button(self.tela_user, text="<--", command=self.destruirpost)
		self.remove_button3.place(x=10,y=10)
		self.text3= tk.StringVar()
		self.text3.set('Para mudar de menu, clique na seta à esquerda.')
		escrever= tk.Label(self.tela_user,textvariable=self.text3,font=(None,12)).place(x=0,y=400)

	def destruirpost(self):
		self.texto4.set('')
		self.remove_button3.destroy()
		self.botão.destroy()
		self.caixa_texto.destroy()
		self.conteudo_label.set('')
		self.text3.set('')


	def inform(self):

		self.Lb1 = tk.Listbox(self.tela_user,width=30,height=4) #criando listbox
		self.Lb1.place(x=300, y=0)
		now = time.strftime("%H:%M:%S") #pegando o tempo para determinar cor pelo horário

		#informações nas listboxes
		self.Lb1.insert(0, "Café da manhã:  07:00h as 10:30h")
		self.Lb1.insert(1, "Almoco:  12:00h as 15:00h")
		self.Lb1.insert(2, "Jantar:  18:00h as 22:00h")
		self.Lb1.insert(3, "Piscina: 08:00h as 22:00h")

		#listbox de legenda de cor
		self.Lb2 = tk.Listbox(self.tela_user,width=30,height=2)
		self.Lb2.place(x=100, y=0)
		self.Lb2.insert(0, "Fechado")
		self.Lb2.itemconfig(0, bg='red',)
		self.Lb2.insert(1, "Aberto")
		self.Lb2.itemconfig(1, bg='green')

		self.remove_button4 = tk.Button(self.tela_user, text="<--", command=self.destruirinfo)
		self.remove_button4.place(x=10,y=10)
		self.text4= tk.StringVar()
		self.text4.set('Para mudar de menu, clique na seta à esquerda.')
		escrever= tk.Label(self.tela_user,textvariable=self.text4,font=(None,12)).place(x=10,y=300)

		#mudança de cor da listbox de acordo com horario de funcionamento
		if now >= time.strftime("07:00:00") and (now<time.strftime("10:30:00")) :
			self.Lb1.itemconfig(0, bg='green')
		else:
			self.Lb1.itemconfig(0, bg='red')

		if now >= time.strftime("12:00:00") and (now<time.strftime("15:00:00")) :
			self.Lb1.itemconfig(1, bg='green')
		else:
			self.Lb1.itemconfig(1, bg='red')

		if now >= time.strftime("18:00:00") and (now<time.strftime("22:00:00")) :
			self.Lb1.itemconfig(2, bg='green')
		else:
			self.Lb1.itemconfig(2, bg='red')
		if now >= time.strftime("07:00:00") and (now<time.strftime("22:00:00")) :
			self.Lb1.itemconfig(3, bg='green')
		else:
			self.Lb1.itemconfig(3, bg='red')

	def destruirinfo(self):
		self.Lb1.destroy()
		self.Lb2.destroy()
		self.text4.set('')



		

app = hotel()
app.iniciar()