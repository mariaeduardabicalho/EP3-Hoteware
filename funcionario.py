import tkinter as tk
import time
from firebase import firebase
f = firebase.FirebaseApplication('https://ep3-hotware.firebaseio.com', None)


class hotel:
	
	def __init__(self):
		
		# Definindo a janela principal
		self.tela_user= tk.Tk()
		self.tela_user.geometry("{0}x{1}+0+0".format(self.tela_user.winfo_screenwidth(),self.tela_user.winfo_screenheight()))
		self.tela_user.title("Tela funcionario")
		self.tela_user.columnconfigure(0, minsize=120, weight=1)
		self.tela_user.columnconfigure(1, weight=1)
		self.tela_user.columnconfigure(2, weight=1)
		self.tela_user.columnconfigure(3, weight=1)

		#Instruções para o funcionário
		self.textoo= tk.StringVar()
		self.textoo.set('Clique nos quartos azuis para ver notificações')
		escrever= tk.Label(self.tela_user,textvariable=self.textoo,font=(None,15)).place(x=40,y=600)


		#Criação dos botões para cada quarto
		self.botao=tk.Button(self.tela_user)
		self.botao.configure(text='Quarto 1',background='green')
		self.botao.configure(command=lambda : self.quarto('Quarto1',0,0))

		self.botao2=tk.Button(self.tela_user)
		self.botao2.configure(text='Quarto 2',background='green')
		self.botao2.configure(command=lambda : self.quarto('Quarto2',1,370))

		self.botao3=tk.Button(self.tela_user)
		self.botao3.configure(text='Quarto 3',background='green')
		self.botao3.configure(command=lambda : self.quarto('Quarto3',2,680))

		self.botao4=tk.Button(self.tela_user)
		self.botao4.configure(text='Quarto 4',background='green')
		self.botao4.configure(command=lambda : self.quarto('Quarto4',3,1000))

		self.botao.grid(row=0,column=0)
		self.botao2.grid(row=0,column=1)
		self.botao3.grid(row=0,column=2)
		self.botao4.grid(row=0,column=3)

		self.mvar=tk.IntVar()
		
		self.update_clock()


	def iniciar(self):
		self.tela_user.mainloop()



	def update_clock(self): 
		g=f.get('/', None)
		now = time.strftime("%H:%M:%S")
		self.tela_user.after(1000, self.update_clock)	#atualizar o firebase	

		#modificar a cor se tiver alguma atualização do usuario
		if (g['users']['Quarto1'])=="0" and (g['servico']['Quarto1'])=="0" and (g['total']['Quarto1'])=="0" and (g['spa']['Quarto1'])=="0" and (g['totalspa']['Quarto1'])=="0" and (g['horariospa']['Quarto1'])=="0":
			self.botao.configure(background='green')
		else:
			self.botao.configure(background='blue')
		if (g['users']['Quarto2'])=="0" and (g['servico']['Quarto2'])=="0" and (g['total']['Quarto2'])=="0" and (g['spa']['Quarto2'])=="0" and (g['totalspa']['Quarto2'])=="0" and (g['horariospa']['Quarto2'])=="0":
			self.botao2.configure(background='green')
		else:
			self.botao2.configure(background='blue')
		if (g['users']['Quarto3'])=="0" and (g['servico']['Quarto3'])=="0" and (g['total']['Quarto3'])=="0" and (g['spa']['Quarto3'])=="0" and (g['totalspa']['Quarto3'])=="0" and (g['horariospa']['Quarto3'])=="0":
			self.botao3.configure(background='green')
		else:
			self.botao3.configure(background='blue')
		if (g['users']['Quarto4'])=="0" and (g['servico']['Quarto4'])=="0" and (g['total']['Quarto4'])=="0" and (g['spa']['Quarto4'])=="0" and (g['totalspa']['Quarto4'])=="0" and (g['horariospa']['Quarto4'])=="0":
			self.botao4.configure(background='green')
		else:
			self.botao4.configure(background='blue')


	def quarto(self,q,c,p):
		g=f.get('/', None)

		#saber a quantidade de informações de cada item para organizar os checkboxes na ordem
		le=len(g['servico'][q])
		le3=len(g['spa'][q])

		if g['users'][q] != '0': #se algum problema for reportado

			self.textoprob= tk.StringVar()
			self.textoprob.set('Problema reportado: ') #escrever na tela problema
			escrever= tk.Label(self.tela_user,textvariable=self.textoprob,font=(None,10)).place(x=100+p,y=30) 
			self.check=tk.Checkbutton(self.tela_user,text=g['users'][q],variable=self.mvar,offvalue=0,command=lambda : self.apagarinfou(q)).place(x=110+p,y=60)
			self.mvar=tk.IntVar() #criar checkbutton do problema, mas se clicar colocar a informação no firebase como 0
			if self.check==1:
				f.put('/users',q,'0')

		if g['servico'][q] != '0':
			self.textoserv= tk.StringVar()
			self.textoserv.set('Servico de quarto: ')
			escrever= tk.Label(self.tela_user,textvariable=self.textoserv,font=(None,10)).place(x=100+p,y=80)
			for i in range(len(g['servico'][q])): #mesmo modelo que o anterior, mas pegar cada termo do pedido
				x=g['servico'][q][i]
				self.mvar3=tk.IntVar()
				self.check=tk.Checkbutton(self.tela_user,text=x,variable=self.mvar3,command= lambda : self.apagarinfos(q)).place(x=110+p,y=90+(i*20+30))
				if self.check==1:
					f.put('/servico',q,x,'0')

		self.mvar=tk.IntVar()
		if g['total'][q]!= '0':
		
			self.check3=tk.Checkbutton(self.tela_user,text='Total: R$' + str(g['total'][q])+ ',00',font=(None,10,'bold'),variable=self.mvar,command=lambda : self.apagarinfot(q)).place(x=110+p,y=110+le*30)
			if self.check3==1:
				f.put('/total',q,'0')


		if g['spa'][q]!= '0':
			self.textospa= tk.StringVar()
			self.textospa.set('Spa: ')
			escrever= tk.Label(self.tela_user,textvariable=self.textospa,font=(None,10)).place(x=110+p,y=180+le*30)
			
			for i in range(len(f.get('/spa',None)[q])):
				x=g['spa'][q][i]
				self.mvar=tk.IntVar()
				self.check=tk.Checkbutton(self.tela_user,text=x,variable=self.mvar,command=lambda : self.apagarinfospa(q)).place(x=110+p,y=220+le*30)
				if self.check==1:
					f.put('/spa',q,x,'0')

		self.mvar=tk.IntVar()
		if g['horariospa'][q]!= '0':
			self.check3=tk.Checkbutton(self.tela_user,text='Horário no spa:' + str(g['horariospa'][q]),variable=self.mvar,command=lambda : self.apagarinfosh(q)).place(x=110+p,y=200+le*30)
			if self.check3==1:
				f.put('/horariospa',q,'0')

		self.mvar=tk.IntVar()
		if g['totalspa'][q]!= '0':
			
			self.check3=tk.Checkbutton(self.tela_user,text='Total: R$' + str(g['totalspa'][q])+ ',00',font=(None,10,'bold'),variable=self.mvar,command=lambda : self.apagarinfots(q)).place(x=110+p,y=250+le*30+le3*20)
			if self.check3==1:
				f.put('/totalspa',q,'0')

	#Trasformar as informações do firebase em 0
	def apagarinfou(self,q):
		f.put('/users',q,'0')

	def apagarinfos(self,q):
		f.put('/servico',q,'0')

	def apagarinfot(self,q):
		f.put('/total',q,'0')

	def apagarinfots(self,q):
		f.put('/totalspa',q,'0')

	def apagarinfospa(self,q):
		f.put('/spa',q,'0')

	def apagarinfosh(self,q):
		f.put('/horariospa',q,'0')
		
		
app = hotel()
app.iniciar()